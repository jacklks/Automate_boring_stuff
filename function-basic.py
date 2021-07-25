# 定義函式
def multiply(n1, n2):
    print(n1*n2)
    return n1*n2
# 呼叫函式
value = multiply(323,321)
print(value)

# 程式的包裝
sum = 0
for n in range(11):
    sum = sum + n
print(sum)

def calculate(max):
    sum = 0 
    for n in range(1, max+1):
        sum = sum +n
    print(sum)

calculate(20)