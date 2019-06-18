def numberprimeFactors(n):
    count=0
    if isprime(n):
        return 1
    else:
        for i in range (2,n//2+1):
            if  n%i== 0 and isprime(i):
                count+=1
        return count
def isprime(n):
    flag=1
    if n==2:
        return True
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                flag=0
                return False
        if flag==1:
            return True