M, N, a = map(int, input().split())
count = 0
x = M / a 
if M % a != 0:
    x = int(x + 1)
    
y = N / a
if N % a != 0:
    y = int(y + 1)
if y > 2:
    num = x * y
else:
    num = x * y

print(int(num))