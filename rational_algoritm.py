
def GetCoef():
    coef = []
    for i in input():
        if (i!='  '):
            coef.append(i.split('*'))
    print(coef)
n = GetCoef()

def Rational_calc(n):
    for i in n:
        if n == '+':
            return n[i-1] + n[i+1]
        elif n == '-':
            return n[i-1] - n[i+1]
        elif n == '*':
            return n[i-1] * n [i+1]
        elif n == '/':
            return n[i-1] / n [i+1]
        
res = Rational_calc(n)
print(res)
    

