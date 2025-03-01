# Concepts, Features, Types and Pros and Cons

Organize concepts, features, types and Pros and Cons

## iOS, Swift

- iOS의 주요 아키텍처와 컴포넌트 설명
  - iOS의 주요 아키텍처 개요
    - iOS 애플리케이션은 크게 5계층(5-Tier Architecture) 으로 구성

  - 주요 아키텍쳐
    - Core OS
	  - iOS의 가장 하위 계층, 하드웨어 및 시스템 수준의 기능을 제공
	  - 핵심 역할: 메모리 관리, 파일 시스템, 네트워크 보안, Bluetooth, 암호화 등
	  - 관련 프레임워크
	    - Kernel (XNU): iOS의 Unix 기반 커널
	    - Security Framework: 암호화 및 보안 관련 기능
	    - Core Bluetooth: 블루투스 통신 지원

    - Core Services
	  - 앱 개발에서 가장 많이 사용되는 기본 서비스 제공 계층
	  - 핵심 역할: 데이터 저장, 네트워크 통신, 로케이션 서비스 제공
	  - 관련 프레임워크:
	    - Foundation Framework: 컬렉션(Array, Dictionary 등), 파일 입출력, 날짜 및 시간 처리.
	    - Core Data: 객체 기반 데이터 저장소 (ORM 역할)
	  - CloudKit: iCloud 연동
      - Core Location: GPS 및 위치 기반 서비스

    - Media
	  - 멀티미디어 처리 및 UI 표현을 담당
	  - 핵심 역할: 그래픽, 오디오, 비디오 재생 및 이미지 처리
	  - 관련 프레임워크
	    - AVFoundation: 오디오 및 비디오 처리
	    - Core Animation: UI 애니메이션 효과 제공
	    - Core Graphics: 2D 그래픽 렌더링
	    - Metal: GPU 최적화 그래픽 프로그래밍

    - Cocoa Touch (UIKit)
	  - 사용자 인터페이스(UI) 및 사용자 경험(UX) 제공 계층
	  - 핵심 역할: 버튼, 텍스트 필드, 테이블 뷰, 제스처 등을 제공하여 UI 구현
	  - 관련 프레임워크
	    - UIKit: iOS의 기본 UI 프레임워크
	    - SwiftUI: 선언형 UI 프레임워크 (iOS 13부터 지원)
	    - EventKit: 캘린더 및 일정 관리
	    - Contacts: 주소록 데이터 관리

    - Application Layer
	  - 실제 앱이 동작하는 계층
	  - 개발자가 구현하는 비즈니스 로직, UI 레이아웃, 데이터 처리 등이 포함

  - iOS 주요 디자인 패턴 (아키텍처 패턴)
    - 개요
      - iOS 개발에서는 코드의 재사용성, 유지보수성, 테스트 용이성을 높이기 위해 아키텍처 패턴을 적용
    - MVC (Model-View-Controller)
      - iOS의 기본 아키텍처 패턴
      - Apple이 공식적으로 권장하지만, ViewController에 너무 많은 로직이 집중되는 문제가 있음 (Massive View Controller 문제)
      - 구성요소 및 설명
        - Model: 데이터 및 비즈니스 로직 담당
        - View: UI 및 사용자 인터페이스 표시
        - Controller: View와 Model을 연결하는 중간 역할 (UIViewController)
    - MVVM (Model-View-ViewModel)
      - UI 로직을 ViewModel로 분리하여 테스트 가능성을 높이고 유지보수를 쉽게 하는 패턴
      - SwiftUI 및 Combine과 함께 사용하기 적합
      - 구성요소 및 설명
        - Model: 데이터 구조 및 비즈니스 로직
        - ViewModel: UI에서 사용할 데이터를 가공하여 View에 전달
        - View: UI를 담당 (SwiftUI 또는 UIViewController)
    - VIPER (View-Interactor-Presenter-Entity-Router)
      - iOS에서 가장 분리도가 높은 구조로, 대규모 프로젝트에 적합
      - 테스트가 용이하고 유지보수가 쉬운 구조
      - 구성요소 및 설명
        - View: UI 표시
        - Interactor: 비즈니스 로직 및 데이터 처리
        - Presenter: View와 Interactor 간 데이터 변환
        - Entity: 데이터 모델
        - Router: 화면 이동 (네비게이션 관리)
  - iOS 주요 컴포넌트
    - ViewController (UIViewController)
	  - 화면을 구성하는 가장 기본적인 컴포넌트.
	  - 라이프사이클 (viewDidLoad, viewWillAppear, viewDidDisappear) 관리.
    - TableView & CollectionView (UITableView, UICollectionView)
	  - 리스트 UI를 구성할 때 사용.
	  - UITableView → 단순 리스트
	  - UICollectionView → 그리드 형태 리스트
    - UserDefaults & Core Data
	  - UserDefaults → 간단한 데이터 저장 (예: 설정 값)
	  - Core Data → ORM 기반 로컬 데이터 저장소
    - URLSession
	  - 네트워크 통신을 위한 API (GET, POST 요청 처리)
    - Combine & SwiftUI
	  - Combine → 비동기 데이터 스트림 관리 (Publisher, Subscriber)
	  - SwiftUI → 선언형 UI 프레임워크

- Swift의 주요 특징은?
    - 개요
        - Apple이 개발한 프로그래밍 언어로, iOS, macOS, watchOS, tvOS 애플리케이션을 개발하기 위해 사용
        - 안전성, 성능, 간결성을 고려하여 설계된 언어로, 기존 Objective-C보다 더 직관적이고 효율적인 코드 작성을 지원
    - Swift의 목표
        - 안전한(Safe) 코드 → 메모리 충돌 방지, 타입 안정성
        - 빠른(Fast) 실행 속도 → LLVM 기반 컴파일러 사용
        - 간결한(Simple) 문법 → 개발자가 쉽게 배울 수 있도록 설계
    - Swift 주요 활용 분야
	       - iOS 앱 개발 (iPhone, iPad)
	       - macOS 앱 개발
	       - watchOS, tvOS 앱 개발
	       - 서버 개발 (Vapor, Kitura 프레임워크 활용)
    - 주요 특징
        - 간결, 직관적인 문법
        - 타입 안정성(Type Safety) 및 타입 추론(Type Inference)
            - 엄격한 타입 시스템을 적용하여 오류를 줄이고, 타입을 자동으로 추론
        - 옵션(Optional) 타입 - Null Safety 지원
            - Null 값(= nil) 사용을 엄격하게 제한하여 런타임 오류를 방지
								    - 옵셔널(Optional)을 사용하여 값이 존재할 수도 있고, 존재하지 않을 수도 있는 상황을 명확하게 처리
        - 함수형 프로그래밍 지원 (Functional Programming)
            - 고차 함수(Higher-Order Functions) 를 제공하여 함수형 프로그래밍 패러다임을 지원
        - 메모리 안전성 (Automatic Memory Management - ARC)
            - ARC(Automatic Reference Counting) 를 사용하여 메모리를 자동으로 관리하므로, 개발자가 직접 메모리를 해제할 필요가 없음
        - 프로토콜 지향 프로그래밍 (Protocol-Oriented Programming, POP)
            - 객체 지향 프로그래밍(OOP)보다 프로토콜 지향 프로그래밍(POP)을 강조하여 코드의 유연성과 확장성을 높임
        - 안전한 에러 처리 (Error Handling)
            - do-try-catch 구문을 사용하여 예외를 명확하게 처리할 수 있도록 함
        - 강력한 확장 기능 (Extensions)
            - 확장(Extension) 기능을 사용하면 기존 클래스, 구조체, 열거형에 새로운 기능을 추가 가능
        - 멀티스레딩 및 동시성(Concurrency) 지원
            - 비동기 프로그래밍을 쉽게 구현할 수 있도록 async/await을 지원
    - 결론
        - Swift는 Apple의 공식 프로그래밍 언어로 iOS, macOS, watchOS, tvOS 앱 개발에 사용됨
        - 간결하고 직관적인 문법, 타입 안정성, 옵셔널, 함수형 프로그래밍 지원
        - ARC를 통한 자동 메모리 관리, 프로토콜 지향 프로그래밍(POP) 지원
        - 비동기 프로그래밍(Concurrency), 에러 처리, 확장성(Extension) 기능 제공
        - Objective-C보다 성능이 뛰어나며, 최신 Apple 생태계에 최적화된 언어
        - Swift는 안전하고 빠르며, 개발자 친화적인 최신 프로그래밍 언어

- struct와 class의 차이점
    - 개요
        - struct(구조체)와 class(클래스)의 주요 차이점은 값 타입과 참조 타입의 차이
    - 값 타입, 참조 타입
        - Struct: 값 타입
            - 값을 직접 저장하며, 변수에 할당하거나 함수의 인자로 전달될 때 복사됨
            - 각각의 인스턴스가 독립적인 데이터를 가짐
        - Class: 참조 타입
            - 인스턴스를 변수에 할당하거나 함수의 인자로 전달할 때 참조(주소)가 전달됨
            - 같은 인스턴스를 여러 변수에서 공유할 수 있음
        - 예제
          ```Swift
          struct UserStruct {
              var name: String
          }

          class UserClass {
              var name: String
              
              init(name: String) {
                  self.name = name
              }
          }

          var struct1 = UserStruct(name: "Alice")
          var struct2 = struct1  // 값 복사
          struct2.name = "Bob"

          var class1 = UserClass(name: "Alice")
          var class2 = class1  // 참조 전달
          class2.name = "Bob"

          print(struct1.name)  // "Alice" (독립적인 값), struct2.name을 Bob으로 변경해도 struct1의 name은 변경되지 않음
          print(class1.name)   // "Bob" (같은 객체 참조), class2.name을 변경했는데 class1.name 도 변경, 참조관계
          ```
    - 메모리 관리
        - Struct
            - 스택 메모리에 저장됨
            - 빠르고 자동으로 메모리에서 제거됨(ARC 영향 없음)
        - Class
            - 힙 메모리에 저장됨 (자바와 동일)
            - ARC(Automatic Reference Counting)에 의해 메모리를 관리함
            - 순환 참조(Retain Cycle)가 발생할 수 있음
    - 상속(Inherirance) 
        - Struct 상속 불가능
        - Class 상속 가능
    - Mutability (불변성)
        - Struct
            - let 키워드로 선언된 struct 인스턴스는 내부 속성도 변경 불가
            - 내부 속성 변경하려면 mutating 키워드 사용 필수
              ```Swift
              struct Car {
                  var model: String
                  // mutating keyword
                  mutating func changeModel(to newModel: String) {
                      self.model = newModel
                  }
              }
              var myCar = Car(model: "BMW")
              myCar.changeModel(to: "Tesla") 
              ```
        - Class
            - let 키워드로 선언된 class 인스턴스라도 내부 속성 변경 가능
    - Protocol Conformance
        - Struct & Class 모두 프로토콜을 채택 가능
        - struct는 상속이 불가능하므로 프로토콜 기반의 확장을 더 많이 활용
          ```Swift
          protocol Driveable {
              func drive()
          }
          struct Bike: Driveable {
              func drive() {
                  print("Riding a bike")
              }
          }
          ```
    - 사용 사례
        - Struct 사용
            - 값이 독립적이고 변경이 적은 경우
            - 데이터 중심(모델)
            - SwiftUI에서 ViewModel
            - Codable 데이터 모델 
        - Class 사용 
            - 상태를 변경하거나 공유해야 하는 경우
            - 객체 지향 프로그래밍(OOP) 필요
            - UIKit 기반 UI 코드
            - 네트워크, 데이터베이스, 싱글톤 패턴
    - 결론
        - 값 타입(struct)은 복사되어 독립적인 데이터를 가짐 > SwiftUI 등에서 많이 사용됨
        - 참조 타입(Class)은 참조되어 여러 객체에서 공유됨 > UIKit 기반 개발에 유용
        - Struct가 기본적으로 더 안전하고 성능이 좋음 > 기본적으로 Struct를 사용하고 필요할 때 Class 를 사용
        - Swift에서는 가능하면 Struct를 기본으로 사용하고, 상속이나 참조가 필요할 때 Class를 고려하는 것이 좋은 방향
 
- optional이란 무엇이고, !와 ?의 차이
    - 개요
        - Swift에서 Optional은 값이 있을 수도 있고 없을 수도 있는 변수를 나타내는 타입
    - Optional 정의
        - Optional은 값이 nil일 가능성이 있는 변수나 상수를 안전하게 다루기 위해 사용
        - 일반적으로 ?를 붙여서 선언
    - ?와 !의 차이
        - ? (Optional)
            - ?는 값이 있을 수도 있고 없을 수도 있음을 나타냄
            - 값을 직접 사용하려면 언래핑이 필요합니다.
    - 안전한 언래핑
        ```swift
        var name: String? = "Aiden"
        print(name) // Optional("Aiden")
        // 안전한 언래핑 (Optional Binding)
        if let unwrappedName = name {
            print(unwrappedName) // Aiden
        }
        // Nil-Coalescing Operator (기본값 제공)
        print(name ?? "Unknown") // Aiden
        ```
    - ! (Forced Unwrapping)
        - !는 강제로 언래핑하여 값을 가져오는 방법
        - nil이면 앱이 크래시 발생
    - 언제 ?와 ! 사용
        - ? → 값이 nil일 수도 있는 경우, 안전한 처리 필요
        - ! → 값이 nil이 될 수 없다고 확신하는 경우 (하지만 주의해서 사용해야 함)
            - 가능하면 ?를 사용하고, if let 또는 guard let을 활용하여 안전하게 언래핑하는 것이 좋은 방향

- guard와 if let의 차이
    - 개요
        - Swift에서 옵셔널 바인딩(Optional Binding)을 사용할 때, guard let과 if let은 모두 옵셔널 값을 안전하게 언래핑하는 방법

    - if let
        - if let은 옵셔널 값이 존재할 경우 블록 내에서 안전하게 사용할 수 있도록 바인딩하는 방식
        - 예제
            - 설명
                - if let unwrappedName = name에서 name이 nil이 아닐 경우 unwrappedName에 값을 할당하고, 블록 내에서 사용 가능
	            - nil이면 else 블록이 실행됨.
                - 옵셔널 값이 있을 경우 블록 내에서만 사용 가능.
	            - 중첩된 로직이 많아질 경우 가독성이 떨어질 수 있음.
            - 코드
                ```swift
                let name: String? = "Swift"
                if let unwrappedName = name {
                    print("이름은 \(unwrappedName)입니다.")
                } else {
                    print("이름이 없습니다.")
                }
                ```

    - guard let
        - 옵셔널 값이 없을 경우 즉시 함수를 빠져나가거나 오류를 반환하는 방식
        - 예제
            - 설명
                - guard let을 사용하면 nil일 경우 즉시 return을 실행하여 코드의 흐름을 빠르게 정리할 수 있음.
	            - unwrappedName은 guard let 이후의 코드 블록에서 계속 사용 가능
                - 함수 초기에 nil을 검사하고 조기 반환(Early Exit)하여 가독성을 높임
	            - 이후의 코드에서 unwrappedName을 계속 사용할 수 있음
            - 코드
                ```swift
                func greet(name: String?) {
                    guard let unwrappedName = name else {
                        print("이름이 없습니다.") // `nil`이면 즉시 종료
                        return
                    }
                    
                    print("안녕하세요, \(unwrappedName)님!") // 옵셔널 값이 있을 때 실행
                }
                reet(name: "Swift")     // 출력: 안녕하세요, Swift님!
                greet(name: nil)        // 출력: 이름이 없습니다.
                ```

    - if let vs guard let 선택 기준
        - 옵셔널 값이 존재할 때만 특정 작업을 수행해야 하는 경우: if let 사용
        - 옵셔널 값이 없을 경우 빠르게 종료해야 하는 경우 (Early Exit): guard let 사용
        - 중첩을 줄이고 가독성을 높이고 싶은 경우: guard let 사용
        - else 블록에서 return, throw, fatalError() 등을 호출해야 하는 경우: guard let 사용

    - 결론
        - if let은 옵셔널 값이 존재할 경우 특정 블록 내에서만 사용할 때 적합
        - guard let은 옵셔널 값이 없을 경우 즉시 함수나 루프를 종료할 때 적합 (Early Exit 패턴)
        - Swift에서는 가독성과 유지보수를 고려할 때, 대부분 guard let을 선호하는 경우가 많음

- weak, strong, unowned의 차이는?
- ARC(Automatic Reference Counting)란 무엇인가?
- protocol과 extension의 역할과 활용 사례는?
- enum과 associated value를 활용하는 방법은?
- closure란 무엇이며, 캡처 리스트([weak self])를 사용하는 이유는?
- UIKit과 SwiftUI의 차이는?
- UIView와 CALayer의 차이는?
- Auto Layout과 Constraint의 원리 및 사용 방법은?
- frame과 bounds의 차이는?
- TableView와 CollectionView의 차이점과 사용 사례는?
- SwiftUI에서 State, Binding, ObservedObject, EnvironmentObject의 차이는?
- UIKit에서 ViewController 생명주기는?
- SwiftUI에서 View의 생명주기는?
- NavigationView와 TabView의 기본 동작 원리는?
- UIKit에서 커스텀 셀을 만들 때 고려해야 할 사항은?
- iOS에서 네트워킹을 처리하는 방법은?
- URLSession을 활용한 네트워킹 구현 방법은?
- JSON을 파싱하는 방법과 Codable의 역할은?
- 비동기 네트워킹을 처리할 때 async/await과 completion handler의 차이는?
- Core Data와 Realm의 차이는?
- UserDefaults, Keychain, File System의 차이와 각각의 사용 사례는?
- REST API와 GraphQL의 차이는?
- iOS에서 메모리 누수가 발생하는 원인과 해결 방법은?
- DispatchQueue.main.async을 사용하는 이유는?
- Grand Central Dispatch(GCD)와 OperationQueue의 차이는?
- iOS에서 성능 최적화를 위해 고려해야 할 사항은?
- 앱의 메모리 사용량을 줄이는 방법은?
- Instruments에서 메모리 릭을 탐지하는 방법은?
- 스레드 안전성을 보장하는 방법은?
- iOS에서 자주 사용되는 디자인 패턴은?
- MVC, MVVM, VIPER의 차이점과 장단점은?
- 의존성 주입(Dependency Injection)이란?
- Singleton 패턴이 가지는 문제점과 해결 방법은?
- Combine 프레임워크를 활용하는 방법은?
- Swift에서 Delegate 패턴과 Notification 패턴의 차이는?
- iOS 앱을 App Store에 배포하는 과정은?
- Ad Hoc, Enterprise, App Store 배포 방식의 차이는?
- iOS 앱의 테스트 종류(Unit Test, UI Test 등)와 활용 방법은?
- XCTest에서 UI 테스트를 구현하는 방법은?
- TestFlight를 이용한 베타 테스트 방법은?
- Crashlytics를 활용하여 크래시 로그를 분석하는 방법은?
- Keychain을 활용하여 민감한 데이터를 저장하는 방법은?
- iOS에서 HTTPS를 강제하는 방법은?
- 앱의 보안을 강화하는 방법은?
- Face ID 및 Touch ID를 활용하는 방법은?
- Dynamic Type과 VoiceOver를 지원하는 방법은?
- iOS 앱에서 사용자 데이터를 보호하기 위한 방법은?
- iOS 최신 버전에서 추가된 주요 기능은?
- Swift Concurrency(async/await)와 기존 GCD의 차이점은?
- Apple Silicon에서 iOS 앱이 어떻게 동작하는가?
- WidgetKit, App Clips, Swift Charts 등 최신 프레임워크를 활용하는 방법은?
- Vision, ARKit, CoreML 등 최신 기술을 프로젝트에서 어떻게 활용할 수 있는가?
- Swift에서 copy-on-write(COW)란? 어떤 자료형에서 활용되는가?
- Swift에서 dynamic 키워드는 언제 사용되는가?
- associatedtype을 활용한 제네릭 프로토콜을 정의하는 방법은?
- Swift의 Property Wrapper를 활용하는 방법과 사용 사례는?
- lazy var와 computed property의 차이점은?
- Swift에서 Equatable, Comparable 프로토콜을 직접 구현하는 방법은?
- async let과 Task {}의 차이점은?
- Swift의 Result<T, Error> 타입을 활용하는 방법은?
- actor와 기존 DispatchQueue.sync를 비교하면 어떤 차이가 있는가?
- Memory Layout<T>을 활용하여 메모리 구조를 확인하는 방법은?
- UIBezierPath와 CAShapeLayer를 활용하여 커스텀 UI를 만드는 방법은?
- UIView 애니메이션에서 spring damping이란 무엇이며 어떻게 활용하는가?
- CALayer에서 shadowPath를 직접 설정하면 성능이 왜 향상되는가?
- SwiftUI에서 PreferenceKey를 활용하는 방법과 사례는?
- GeometryReader의 역할과 성능 최적화 방안은?
- UIKit에서 layoutSubviews()와 draw(_:)의 차이는?
- UIStackView가 실제로 내부에서 어떻게 동작하는가?
- SwiftUI에서 ViewBuilder는 어떻게 작동하는가?
- URLSessionDataTask, URLSessionDownloadTask, URLSessionUploadTask의 차이점은?
- HTTP/2와 HTTP/3의 차이는?
- URLCache를 활용하여 네트워크 응답을 캐싱하는 방법은?
- WebSocket과 HTTP Long Polling의 차이점은?
- multipart/form-data 요청을 iOS에서 처리하는 방법은?
- Core Data의 NSPersistentContainer와 NSPersistentStoreCoordinator의 차이는?
- Core Data의 merge policy 옵션이란?
- Core Data에서 NSFetchedResultsController는 언제 사용되는가?
- Realm을 사용할 때 @Persisted와 기존 List<>의 차이점은?
- CloudKit을 활용한 데이터 동기화의 원리는?
- RunLoop의 개념과 활용 사례는?
- autoreleasepool이 필요한 경우는?
- malloc과 free는 iOS에서 어떻게 동작하는가?
- Object Graph와 Reference Counting의 관계는?
- NSCache와 UserDefaults의 차이는?
- NSOperationQueue와 DispatchQueue의 차이점과 적절한 사용 사례는?
- Swift의 UnsafePointer<T>와 OpaquePointer의 차이는?
- iOS에서 Lazy Loading을 구현하는 방법은?
- NSThread와 pthread의 차이는?
- iOS에서 Backtrace를 활용하여 메모리 릭을 찾는 방법은?
- Clean Architecture를 iOS 프로젝트에서 적용하는 방법은?
- Interactor, Presenter, Repository는 각각 어떤 역할을 하는가?
- RxSwift와 Combine의 차이점은?
- Coordinator Pattern이 필요한 이유는?
- Dependency Injection을 활용하여 ViewController의 의존성을 관리하는 방법은?
- SOLID 원칙을 iOS 개발에서 적용하는 방법은?
- Protocol-Oriented Programming(POP)이 객체 지향 프로그래밍(OOP)과 비교했을 때 가지는 장점은?
- Higher-Order Function이란 무엇이며 Swift에서 어떤 예제가 있는가?
- State Restoration이란 무엇이며, iOS에서 어떻게 적용하는가?
- Bitcode의 개념과 iOS 앱 빌드 과정에서의 역할은?
- dSYM 파일의 역할과 Crash 로그 분석 방법은?
- Xcode의 Build Phases에서 Run Script를 활용하는 방법은?
- XCTestCase에서 setUp()과 tearDown()은 각각 언제 호출되는가?
- iOS에서 Fastlane을 활용한 자동 배포 방법은?
- iOS 앱의 크기를 최적화하는 방법은?
- In-App Purchase에서 Receipt Validation을 처리하는 방법은?
- iOS의 On Demand Resources (ODR)란?
- Xcode Cloud와 기존 CI/CD 도구(GitHub Actions, Bitrise) 비교 분석
- App Transport Security (ATS)란?
- Keychain을 활용하여 민감한 데이터를 저장할 때 고려해야 할 사항은?
- iOS에서 Secure Enclave를 활용하는 방법은?
- JWT (JSON Web Token)을 활용한 인증 방식은?
- Biometric Authentication을 적용할 때 LocalAuthentication 프레임워크의 역할은?
- 앱이 Background 상태에서 네트워크 통신을 보안적으로 유지하는 방법은?
- iOS Sandboxing이란?
- iOS Privacy Manifest와 앱 개인정보 보호 정책 작성 방법은?
- Swift 5.9에서 추가된 주요 기능은?
- Swift Concurrency의 structured concurrency 개념이 무엇인가?
- Metal을 활용하여 iOS 앱에서 그래픽 성능을 최적화하는 방법은?
- ARKit과 RealityKit의 차이점은?
- iOS에서 Passkeys를 지원하는 방법은?
- Live Activities를 구현하는 방법은?
- Dynamic Island에서 실시간 업데이트를 처리하는 방법은?
- Swift의 주요 특징과 Objective-C와의 차이점은 무엇인가요?
- iOS 앱의 생명주기에 대해 설명해주세요.
- SwiftUI와 UIKit의 차이점은 무엇인가요?
- Swift의 ARC(Automatic Reference Counting)와 메모리 관리 방법을 설명해주세요.
- Combine 프레임워크 사용 경험을 설명해주세요.
- Swift의 Result Builder와 Property Wrapper의 사용 사례를 설명해주세요.
- Swift의 Concurrency 모델(Async/Await)에 대해 설명해주세요.
- Swift에서 struct와 class의 차이점은?
- Swift에서 Combine과 RxSwift의 차이점은?
- Swift에서 Result 타입을 사용하는 이유는?
- Swift의 Codable과 JSONSerialization의 차이점은?
- SwiftUI에서 @State, @ObservedObject, @EnvironmentObject의 차이점은?
- SwiftUI에서 LazyVStack과 LazyHStack을 사용하는 이유는?
- Swift의 guard와 if let의 차이는?
- ARC(Automatic Reference Counting)란 무엇인가?
- Swift의 Protocol-Oriented Programming(POP)이란 무엇인가?
- Swift의 Result 타입은 어떤 용도로 사용되는가?
- Grand Central Dispatch(GCD)와 OperationQueue의 차이점은?
- UIViewController의 라이프사이클을 설명하라.
- weak와 unowned의 차이는?
- Swift의 Combine 프레임워크를 사용해본 경험이 있는가?
- iOS의 Core Data와 Realm의 차이점과 성능 비교는?
- Swift의 Property Wrappers(@State, @Binding, @ObservedObject)는 어떻게 동작하는가?
- Swift에서 Key-Value Observing (KVO)의 동작 방식과 한계는?
- iOS의 SceneDelegate와 AppDelegate의 차이점과 역할은?
- Combine 프레임워크에서 Publisher와 Subscriber의 동작 방식은?
- Swift의 Memory Management와 ARC에서 Retain Cycle을 방지하는 방법은?
- iOS 앱에서 Background Execution이 필요한 경우와 구현 방식은?
- Swift에서 Result Builder를 활용하는 방법은?
- Swift에서 some 키워드는 언제 사용되는가?
- Noncopyable 프로토콜이 무엇이며, 언제 활용할 수 있는가? (Swift 5.10 이상)
- Swift에서 defer 문을 활용하는 경우는?
- Swift에서 Codable과 Decodable, Encodable의 차이는?
- Swift에서 KeyPath와 @dynamicMemberLookup을 활용하는 방법은?
- Swift에서 Set과 Array의 차이점은?
- Hashable 프로토콜을 직접 구현하는 방법과 그 용도는?
- Swift의 Lazy Sequence는 무엇이며 언제 사용하는가?
- Swift에서 Mirror API를 활용하여 런타임에 객체 정보를 조회하는 방법은?
- Swift의 SPM(Swift Package Manager)을 활용하여 모듈을 관리하는 방법은?
- Swift에서 Opaque Types(some keyword)과 Generics의 차이는?
- Swift에서 throw, rethrows, try?, try!의 차이점은?
- Swift에서 Equatable과 Identifiable을 구현해야 하는 경우는?
- Swift에서 Capture List([weak self])을 사용해야 하는 경우는?
- Swift에서 @autoclosure의 역할과 활용 방법은?
- Swift에서 Copy-on-Write(COW)가 적용되는 자료형과 동작 방식은?
- Swift에서 Memory Layout<T>을 활용하여 메모리 구조를 확인하는 방법은?
- Swift에서 UnsafePointer<T>와 OpaquePointer의 차이는?
- autoreleasepool을 사용해야 하는 경우는?
- Swift의 Pointer와 Buffer를 활용하여 성능을 최적화하는 방법은?
- Swift의 Concurrency (비동기 프로그래밍)
- async let과 Task {}의 차이점은?
- TaskGroup과 AsyncStream을 활용하여 비동기 작업을 처리하는 방법은?
- Global Actor(@MainActor)와 Detached Task의 차이점은?
- Swift에서 CheckedContinuation을 활용하여 기존의 Completion Handler 패턴을 변환하는 방법은?
- Swift의 Task Priority 설정이 실행 성능에 미치는 영향은?
- Swift에서 Continuations을 활용한 비동기 API 래핑 방법은?
- Swift에서 Parallel Execution을 효율적으로 처리하는 방법은?
- LazyVStack과 LazyHStack의 차이점과 성능 최적화 사례는?
- SwiftUI에서 PreferenceKey를 활용하는 방법과 사례는?
- GeometryReader를 사용할 때 성능을 최적화하는 방법은?
- UIHostingController와 UIViewControllerRepresentable의 차이는?
- UIViewController와 SwiftUI View 간 데이터 바인딩을 최적화하는 방법은?
- SwiftUI에서 Transaction과 Animation의 차이는?
- SwiftUI에서 @StateObject와 @ObservedObject의 차이는?
- Swift에서 multipart/form-data 요청을 처리하는 방법은?
- iOS에서 NSURLSessionWebSocketTask을 활용하여 WebSocket을 처리하는 방법은?
- iOS에서 URLSession의 HTTP/2 및 HTTP/3 지원 여부와 그 차이는?
- iOS에서 GraphQL을 활용한 네트워크 요청을 처리하는 방법은?
- CoreData와 Realm에서 Schema Migration을 수행하는 방법은?
- UserDefaults, Keychain, File System, CloudKit의 차이점과 사용 사례는?
- URLSessionDataTask, URLSessionDownloadTask, URLSessionUploadTask의 차이는?
- iOS 앱에서 메모리 사용량을 줄이는 방법은?
- RunLoop의 개념과 활용 사례는?
- iOS에서 Background Task를 활용하여 네트워크 요청을 최적화하는 방법은?
- CALayer에서 shadowPath를 직접 설정하면 성능이 왜 향상되는가?
- iOS에서 프레임 드롭(Frame Drop)을 방지하기 위한 성능 최적화 기법은?
- NSCache와 UserDefaults의 차이는?
- Image Rendering Mode를 설정하면 성능이 어떻게 최적화되는가?
- Core Animation과 Metal을 활용하여 UI 성능을 최적화하는 방법은?
- iOS 앱을 App Store에 배포하는 과정을 설명하시오.
- Xcode Cloud와 기존 CI/CD 도구(GitHub Actions, Bitrise)의 차이는?
- TestFlight를 활용한 베타 테스트 프로세스는?
- iOS에서 Fastlane을 활용하여 자동 배포를 설정하는 방법은?
- App Transport Security (ATS)란?
- Bitcode가 iOS 앱 배포 과정에서 가지는 역할은?
- iOS에서 Secure Enclave를 활용하는 방법은?
- iOS 앱에서 Face ID 및 Touch ID를 활용하는 방법은?
- iOS에서 JWT (JSON Web Token)을 활용한 인증 방식은?
- App Privacy Manifest와 앱 개인정보 보호 정책을 작성하는 방법은?
- iOS Sandboxing이란?
- iOS 앱에서 In-App Purchase의 보안을 강화하는 방법은?
- iOS 최신 버전에서 추가된 주요 기능은?
- Live Activities를 구현하는 방법은?
- Dynamic Island에서 실시간 업데이트를 처리하는 방법은?
- iOS에서 Passkeys를 지원하는 방법은?
- Swift 5.10에서 추가된 새로운 기능은?
- RealityKit과 ARKit의 차이는?
- iOS에서 Metal을 활용하여 그래픽 성능을 최적화하는 방법은?
- WidgetKit을 활용하여 iOS 위젯을 만드는 방법은?