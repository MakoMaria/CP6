print("введите количество элементов массива:")
n = int(input())
print("введите элементы массива")
p = 1000000
h=0
A=[]
A= [ int(input()) for i in range(n) ]
print("введите переменную delta")
d = int(input())
for i in range(0, n):
    if A[i]<p:
        p=A[i]
for i in range(0, n):
    if A[i]==(p+d):
        h=h+1
print(h)