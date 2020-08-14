def check(n):
    if(n<2):
        return False
    if(n==2 or n==3 or n==5 or n==7):
        return True
    if(n%2==0 or n%3==0 or n%5==0 or n%7==0):
        return False
    return True
    
def detachedSemiPrime(n):
    answer=[]
    k=0
    if (n<4 or check(n)):
        answer.append(-1)
        return answer
    else:
        a=2
        b=2
        while a<=n/2:
            if(check(a)):
                b=int(n/a)
                if (check(b) and a*b==n):
                    answer.append(a)
                    answer.append(b)
                    k=1
                    return answer
            a +=1
        if k==0:
            answer.append(-1)
            return answer
test= detachedSemiPrime(565)
print(test)

    
