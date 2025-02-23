# -----------------------------------------------------------------------------------------
# 6001 ~ 6008, 출력 연습
# 분석: 단순 출력, 따옴표 출력 방법, 특수문자 출력, 슬래시 표현
# -----------------------------------------------------------------------------------------
print("Hello")
print("Hello World")
print("Hello")
print("World")
print("'Hello'")
print('"Hello World"')
print("\"!@#$%^&*()\'")
print("\"C:\\Download\\\'hello\'.py\"")
print("print(\"Hello\\nWorld\")")

# -----------------------------------------------------------------------------------------
# 6009 ~ 6017, 입력받고 (변환 후) 출력 연습
# 분석: 입력 받기, 정수/실수 변환, 여러 인자 입력받기 (input().split())
# 분석2: print 문 사용법
# -----------------------------------------------------------------------------------------
value=input()
print(value)

value=input()
value=int(value)
print(value)

f=input()
f=float(f)
print(f)

a=input()
b=input()
a=int(a)
b=int(b)
print(a)
print(b)

a=input()
b=input()
print(b)
print(a)

f=input()
f=float(f)
print(f)
print(f)
print(f)

a,b=input().split()
a=int(a)
b=int(b)
print(a)
print(b)

a,b=input().split()
print(b,a)

s=input()
print(s,s,s)

# -----------------------------------------------------------------------------------------
# 6018 ~ 6019, 출력 연습 (Separator)
# 분석: Separator, print 내 sep 사용, 스트링 안에 값 표현
# -----------------------------------------------------------------------------------------
a,b=input().split(":")
print(a,b,sep=":")

y, m, d = input().split('.')
print(f"{d}-{m}-{y}")

# -----------------------------------------------------------------------------------------
# 6020 ~ 6021, 문자열 내 일부 문자 변환
# 분석: replace 사용법, 문자열 배열 방식 처리
# -----------------------------------------------------------------------------------------
id_number = input()
print(id_number.replace('-', ''))

s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# -----------------------------------------------------------------------------------------
# 6022, 입력 데이터 쪼개기
# 분석: slicing 처리 (:), 슬라이싱 시 범위 개념 (0:2) -> 0, 1 index
# -----------------------------------------------------------------------------------------
s = input()
print(s[0:2])
print(s[2:4])
print(s[4:6])

# -----------------------------------------------------------------------------------------
# 6023, 시분초 입력받아 분만 출력하기
# 분석: 문자열 split 후 배열처럼 사용 방법
# -----------------------------------------------------------------------------------------
time = input()  # 시:분:초 형식으로 입력받기
print(time.split(':')[1])

# -----------------------------------------------------------------------------------------
# 6024, 단어 2개 입력받아 이어 붙이기
# 분석: 문자열 연결 방법, input().split() 시 구분 방식(공백)
# -----------------------------------------------------------------------------------------
w1, w2 = input().split()
result = w1 + w2 
print(result)

# -----------------------------------------------------------------------------------------
# 6025, 정수 2개 입력받아 합 계산하기
# 분석: 정수 변환, 정수 합 표현
# -----------------------------------------------------------------------------------------
a, b = input().split()
c = int(a) + int(b)
print(c)

# -----------------------------------------------------------------------------------------
# 6026, 실수 2개 입력받아 합 계산하기
# 분석: input() 따로 작성 시 동작 방식 파악, 실수 변환, 실수 합 표현
# -----------------------------------------------------------------------------------------
a = float(input())
b = float(input())
print(a + b)

# -----------------------------------------------------------------------------------------
# 6027 ~ 6031, 10/8/16진 데이터 표현
# 분석: 출력 방법 숙지 (print('%x' % value)), 대/소문자 표현법
# 분석2: 유니코드 변환방법(ord), 유니코드 > 문자 변환(chr)
# -----------------------------------------------------------------------------------------
a = input()
n = int(a)
print('%x'% n)
print('%o'% n)

a = input()
n = int(a)
print('%X'% n)

a = input()
n = int(a, 16)
print('%o' % n)

n = ord(input())
print(n)

c = int(input())
print(chr(c))

# -----------------------------------------------------------------------------------------
# 6032, 입력된 정수의 부호를 바꾸어 출력, 정수 1개 입력받아 부호 바꾸기
# 분석: - 부호 사용
# -----------------------------------------------------------------------------------------
a = input()
a = int(a)
print(-a)

# -----------------------------------------------------------------------------------------
# 6033, 입력된 정수의 부호를 바꾸어 출력, 정수 1개 입력받아 부호 바꾸기
# 분석: chr (유니코드 > 문자 변환) / ord (문자 > 유니코드 변환)
# -----------------------------------------------------------------------------------------
char = input()
print(chr(ord(char) + 1))

# -----------------------------------------------------------------------------------------
# 6034, 정수 2개 입력받아 차 계산하기
# 분석: 일반적인 뺄셈
# -----------------------------------------------------------------------------------------
a,b = input().split()
a = int(a)
b = int(b)
print(a-b)

# -----------------------------------------------------------------------------------------
# 참고) 문자열 거꾸로 출력하기
# 분석: [::-1] 슬라이싱 기법 사용, 문자열[start:end:step] 기본 구조 확인
# 분석2: ::-1 -> start, end 생략 -> 처음부터 끝까지의 의미, -1은 역순 의미
# -----------------------------------------------------------------------------------------
string = 'Welcome SJKOding!'
print(string[::-1])

# -----------------------------------------------------------------------------------------
# 참고) 중복 제거하기
# 분석: 중복 없는 Set에 대한 이해
# 분석2: 리스트를 집합 자료형으로 변환, Set은 중복을 자동으로 제거하는 특징
# 분석3: set(temp) -> {1,2,3,4,5}
# 분석4: list(set(temp)) -> [1,2,3,4,5
# 분석5: set은 요소의 순서 보장하지 않으므로 결과 리스트의 순서는 달라질 수 있음
# 참고 정보) 순서보장 희망 시 > list(dict.fromkeys(temp))
# -----------------------------------------------------------------------------------------
temp = [1, 1, 2, 2, 3, 4, 4, 5]
print(list(set(temp)))

# -----------------------------------------------------------------------------------------
# 참고) list(dict.fromkeys(temp)) 의 동작원리
# 분석: dict.fromkeys(iterable)은 주어진 반복 가능 객체의 요소들을
# 딕셔너리의 키로 사용하여 딕셔너리를 생성하는 함수
# 분석2: 딕셔너리는 중복 키 허용하지 않아서 자동으로 중복 제거되며 삽입 순서 유지됨
# 분석3: dict.fromkeys(temp) -> {1: None, 2: None, 3: None, 4: None, 5: None}
# 분석4: None은 기본 할당 값이며 중요하지 않음
# 분석5: dict.fromkeys(temp) -> {1,2,3,4,5}
# 분석6: list(dict.fromkeys(temp)) -> [1,2,3,4,5]
# -----------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------
# 6035, 실수 2개 입력받아 곱 계산하기
# 분석: float(f1) 방식의 형변환
# -----------------------------------------------------------------------------------------
f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
print(f1 * f2)

# -----------------------------------------------------------------------------------------
# 6036, 단어 여러 번 출력하기
# 분석: 문자 * 횟수 연산
# -----------------------------------------------------------------------------------------
w, n = input().split()
n = int(n)
result = w * n
print(result)

# -----------------------------------------------------------------------------------------
# 6037, 문장 여러번 출력하기
# 분석: 문자열 * 횟수 연산, 횟수 먼저 입력 후 줄바꿈 후 여러번 출력할 문장 입력 순
# -----------------------------------------------------------------------------------------
number = input()
myString = input()
print(myString * int(number))

# -----------------------------------------------------------------------------------------
# 6038, 정수 2개 입력받아 거듭제곱 계산하기
# 분석: 거듭제곱근 표현법
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
i1 = int(i1)
i2 = int(i2)
print(i1**i2)

# -----------------------------------------------------------------------------------------
# 6039, 실수 2개 입력받아 거듭제곱 계산하기
# 분석: 거듭제곱근 표현법
# -----------------------------------------------------------------------------------------
f1, f2 = input().split()
print(float(f1)**float(f2))

# -----------------------------------------------------------------------------------------
# 6040, 정수 2개 입력받아 나눈 몫 계산하기
# 분석: 몫 계산 표현법
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
print(int(i1)//int(i2))

# -----------------------------------------------------------------------------------------
# 6041, 정수 2개 입력받아 나눈 나머지 계산하기
# 분석: 나머지 계산 표현법
# -----------------------------------------------------------------------------------------
i1, i2 = input().split()
print(int(i1)%int(i2))