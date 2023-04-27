print("안녕하세요:)")

#greeting이라고 하는 변수 선언
#이 변수에 문자열 값을 할당
greeting = "안녕하세요:)"
print(greeting)

#변수는 데이터를 변경해서 할당할 수 있는 공간
greeting = "반갑습니다"
print(greeting)


#Naming convention(명명 규칙)
#1. 변수 사이에 공백 허용되지 않음
#2. 단어 사이는 _(언더스코어)를 사용하여 연결
#3. 변수를 선언하기 위한 문자열은 숫자/특수문자로 시작이 불가
#4. 예약어 변수로 선언 불가
#5. 가급적 소문자 사용
#6. 오타 주의


#문자열(Strings) = 문자의 나열

city="seoul"
print(city)

city.upper()
print(city.upper())
print(city.lower())


occupation = "developer   "
print(occupation)

occupation.rstrip()
print(occupation.rstrip())
print(occupation.lstrip())
print(occupation.strip())

print("INFP\nENFP\nISTJ\nESTJ")


#숫자(numbers)

a=2
b=3

print(a+b) #더하기
print(a-b) #빼기
print(a*b) #곱하기
print(a/b) #나누기
print(a**b) #지수
print(a//b) #몫
print(a%b) #나머지


#실수(Float)- 십진 부동 소수점

x=0.6
y=0.3
z=1

print(x+y)
print(x-y)
print(x*y)
print(x/y)

#실수와 연산하는 수는 그 결과가 모두 실수이다


#논리형(Bool, Boolean)
#대문자로 시작하는 키워드

# True
# False

print(3>2)
print(3==3)
print(3 == 3.0)
print(3 is 3.0)

#명령 프롬프트(prompt)
"""
input("설치를 계속 진행하시겠습니다?(y/n)")
text = input("출력할 텍스트를 입력해주세요: ")
print(text)
"""

#주석(comments)
#한 줄 주석/ 여러 줄 주석

"""
여러 줄 주석입니다. 
주석입니다. 
"""


# 조건문

if True:
    print("True")
else:
    print("False")


#입력값을 string 타입으로 처리
"""
value = input("값을 입력해주세요: ")

if int(value) > 10:
    print("a")
else:
    print("b")


value = value.upper()

if value == "INFP":
    print("INFP")
else:
    print("nothing")
"""


#반복문(loops)

i = 0
sum = 0

#for i in range(1,101):
#    print(i)

for i in range(1,101):
    sum = sum + i
print(sum)


#리스트(lists)

mbti = ['INFP','ENFP','ISTJ','ISTP']
print(mbti)
print(mbti[0])

mbti[0] = 'INFJ'

print(mbti)
print(mbti[0])


# 튜플(Tuples)

tup=(1,20,40)
print(tup[0])

# tup[0] = 100 ---- 불가능



# 딕셔너리(Dictionaries)

student = {
    "student_no":"202301234",
    "major":"English",
    "grade":1
}

print(student)
print(student["student_no"])

#추가
student["gpa"] = 4.5
print(student)

#수정
student["gpa"] = 4.3
print(student)

#삭제
del student["grade"]
print(student)


#데이터 접근
print (student.get("major"))

#딕셔너리의 키를 반환
print(list(student.keys()))
#딕셔너리의 값을 반환
print(list(student.values()))