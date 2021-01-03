##자리수 분리하기

n= 1234
s = str(n)
m = map(int, s)
print(*m)



##한 번의 exec만 사용하여 입력 받은 세 문장 코드를 실행하려면?
exec(input() + ';' + input() + ';' + input())
