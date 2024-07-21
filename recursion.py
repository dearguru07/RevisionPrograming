# def Fibb(n,n1,n2):
#     if n==0:
#         return n
#     print(n1)
#     Fibb((n-1),n2,(n1+n2))
# n=int(input('enter anumber'))    
# Fibb(n,0,1)




def Fibb(n):
    n1=0
    n2=1
    for i in range(1,n+1):
        print(n1)
        n3=n1+n2
        n1,n2=n2,n3
n=int(input('enter a numbr'))
Fibb(n)



def Fibb(n,n1,n2):
    if n==0:
        return n
    print(n1)
    Fibb((n-1),n2,(n1+n2))
n=int(input('enter a nuu ebr'))    
Fibb(n,0,1)


# import sys
# sys.setrecursionlimit(1005)
# print(sys.getrecursionlimit())


# def Fact(n):
#     if n==0:
#         return 1
#     return n*Fact(n-1)
# res=Fact(5)
# print(res)



# def Sum(n):
#     if n==0:
#         return 0
#     return n+Sum(n-1)
# n=int(input('ente a nunmebr'))
# res=Sum(n)
# print(res)


# def Multi(n):
#     if n==0:
#         return 1
#     return n*Multi(n-1)
# n=int(input('enter a number'))
# res=Multi(n)
# print(res)



# def CountD(n,count):
#     if n==0:
#         return count
#     n//=10
#     count+=1
#     return CountD(n,count)
# n=int(input('enter anubber'))
# res=CountD(n,0)
# print(res)



def Reverese(n,rev):
    if n==0:
        return rev
    rem=n%10
    rev=(rev*10)+rem
    n//=10
    return Reverese(n,rev)
n=int(input('enter a number'))
res=Reverese(n,0)
print(res)



# def CountD(n,count):
#     if n==0:
#         return count
#     n=n//10
#     count+=1
#     return CountD(n,count)
# n=int(input('enter a number'))
# res=CountD(n,0)
# print(res)