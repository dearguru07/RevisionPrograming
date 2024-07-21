# def CountD(n,count):
#     if n==0:
#         return count
#     return CountD(n//10,count+1)
# n=int(input('enter a number'))
# res=CountD(n,0)
# print(res)


# def Reverese(n,rev):
#     if n==0:
#         return rev
#     rem=n%10
#     rev=(rev*10)+rem
#     n//=10
#     return Reverese(n,rev)
# n=int(input('enter anumbre'))
# res=Reverese(n,0)
# print(res)



# def Poly(n,rev):
#     if n==0:
#         return rev
#     rem=n%10
#     rev=(rev*10)+rem
#     n//=10
#     return Poly(n,rev)
# n=int(input('enter a number'))
# res=Poly(n,0)
# if res==n:
#     print('polyndrom')
# else:
#     print('not a polyndrom')    


# def Sum(n):
#     if n==0:
#         return n
#     return n+Sum(n-1)
# n=int(input('emter a number'))
# res=Sum(n)
# print(res)



# def Product(n):
#     if n==0:
#         return 1
#     return n*Product(n-1)
# n=int(input('emter a number'))
# res=Product(n)
# print(res)


# def Fibb(n,n1,n2):
#     if n==0:
#         return n
#     print(n1)
#     return Fibb((n-1),n2,n1+n2)
# n=int(input('enter a numebr'))
# Fibb(n,0,1)



# def CountD(n,count):
#     if n==0:
#         return count
#     return CountD(n//10,count+1)
# def Amstrong(n,sum,power):
#     if n==0:
#         return sum
#     rem=n%10
#     sum=(sum+rem**power)
#     return Amstrong(n//10,sum,power)
# n=int(input('enter a nu ebr'))
# count=CountD(n,0)
# res=Amstrong(n,0,count)
# if n==res:
#     print('amstrng')
# else:
#     print('not a amaten')    


# str="hello"
# print(str[len(str)-1])



def Reversal_loop(nstr,i,s1):
    if i==len(s1):
        return nstr
    nstr=s1[i]+nstr
    return  Reversal_loop(nstr,i+1,s1)
s1=input('enter a number')
res=Reversal_loop("",0,s1)
print(res)
