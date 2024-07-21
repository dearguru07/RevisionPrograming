# def CountD(n,count):
#     if n==0:
#         return count
#     return CountD(n//10,count+1)
# n=int(input('entra nunneb'))
# res=CountD(n,0)
# print(res)


# def Reverese(n,rev):
#     if n==0:
#         return rev
#     rem=n%10
#     rev=(rem+rev*10)
#     n//=10
#     return Reverese(n,rev)
# n=int(input('eter'))
# res=Reverese(n,0)
# print(res)


# def Fact(n):
#     if n==0:
#         return 1
#     return n*Fact(n-1)
# n=int(input('enter '))
# res=Fact(n)
# print(res)


# def Sum(n):
#     if n==0:
#         return n
#     return n+Sum(n-1)
# n=int(input('enter anumebr'))
# res=Sum(n)
# print(res)


# def polyndrom(n,rev):
#     if n==0:
#         return rev
#     rem=n%10
#     rev=(rev*1)+rem
#     n//=10
#     return polyndrom(n,rev)
# n=int(input('enter anumebr'))
# res=polyndrom(n,0)
# if res==n:
#     print('poilyndrom')
# else:
#     print('not a pluy')    
    
    
    
# def CountD(n,count):
#     if n==0:
#         return count
#     return CountD(n//10,count+1)
# def Amstrong(n,sum,power):
#     if n==0:
#         return sum
#     rem=n%10
#     sum=(sum+rem**power)
#     n//=10
#     return Amstrong(n,sum,power)
# n=int(input('entr'))    
# count=CountD(n,0)
# res=Amstrong(n,0,count)
# if res==n:
#     print('amsrng')
# else:
#     print('not a amstrnh')    
    
    

# def Reversal_loop(nstr, i, s1):
#     if i == len(s1):
#         return nstr
#     nstr = s1[i] + nstr
#     return Reversal_loop(nstr, i + 1, s1)
# s1 = input("enter a new string : ")
# result = Reversal_loop("", 0, s1)
# print(result)


# def CountWords(s):
#     return len(s)
# str=input()
# res=CountWords(str)
# print(res)    

def Reverese(nstr,i,s1):
    if i==len(s1):
        return nstr
    nstr =s1[i]+nstr
    return Reverese(nstr,i+1,s1)
s1=input('sebf')
res=Reverese('',0,s1)
print(res)