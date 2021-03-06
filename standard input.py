##1. input 함수

##- 형식 : input(message)
##- Enter 전까지 숫자, 문자, 공백을 모두 입력 받으며 결과는 문자열(str) 타입

##EX) 예제
############################################################
a = int(input())
b = int(input())
print( a + b )

##[입력예시]
##10
##20
##[출력예시]
##30
##
##
##2. split을 이용한 이름 3개 입력 받기
##
##- split의 결과는 문자열로 된 리스트(list)
a, b, c = input().split()
print(a, b, c)
############################################################
##3. map 함수
##
##- 집합의 요소(item)들을 하나씩 지정한 함수에 mapping

a, b, c, d = map(int, input().split())
print(a + b + c + d)

##4. 분리 기호로 입력받기

a, b, c = map(int, input().split(sep=','))
print(a+b+c)

##[입력예시]
##20, -3, 25
##[출력예시]
##42
##
##5. 3개의 양의 정수를 입력 받아 합계와 평균 계산
a, b, c = map(int, input().split())
s = a + b + c
print(s,  s/3)
