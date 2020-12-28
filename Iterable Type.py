##1. map과 sum 함수의 argument는 iterable 타입
##
a, b, c = map(float, input().split())

print(a + b + c)
print(sum((a,b,c)))
print(sum([a,b,c]))
print(sum([a,b,c], 100))


##2.
x = map(int, input().split())
print(type(x)) #<class 'map'>
print(x)

##3.
x= input().split()
print(type(x)) #<class 'list'>

##4.

##(1)
t = map(int, input().split())
print(sum(t))

## (2)
print(sum(map(int, input().split())))

##5.

l = [1, 3.14, 'name']
l.append("song")
print(l)
l.insert(2, 33)
print(l)
s = {1, 3, 4, 5}
s.add(15)
print(s)
k = {10:1, 'id':14, 'song':3.14}
print(k)
k[10]=55
print(k)
print(l[-1])
t1 = 1, 2, 3
a, b, c = t1
print( a, b, c)
a, b, c = 'kim'
print(a, b, c)

##6.

d = {'a':1, 'b':2, 'c':3 }
d1, d2, d3 =  {'a':1, 'b':2, 'c':3 }
print(d1, d2, d3) ## a b c
a1, a2, a3 = d.values()
b1, b2, b3 = d.keys()
c1, c2, c3 = d.items()
print(a1, a2, a3, b1, b2, b3, c1, c2, c3)
 1 2 3 a b c ('a', 1) ('b', 2) ('c', 3)

##7.
t = (10, 20, 30, 40, 50, 60, 70)
a, *b = t ##*로 남은 아이템들을 받은 변수의 타입은? list
print(a, b) ##10 [20, 30, 40, 50, 60, 70]
a, *m, b = t
print(a, m, b) ##10 [20, 30, 40, 50, 60] 70

##8.
import sys

print(range(5)) ##range(0,5)
print(type(range(5))) ##<class 'range'>
print(sys.getsizeof(range(100))) ##48
print(sys.getsizeof(range(10000000))) ##48

##9. range 함수의 속성

a = range(1, 5)
b, c = range(2)
d, *e, f = a

print(a[1], b, c) ## 2 0 1
print(d, e, f) ## 1 [2, 3] 4
print(a) ## range(1, 5)
print(*a) ## 1 2 3 4

print(*range(5)) ## 0 1 2 3 4
print(*range(2, 5)) ## 2 3 4
print(*range(0, 6, 2)) ## 0 2 4
print(*range(4, -1, -1)) ## 4 3 2 1 0
