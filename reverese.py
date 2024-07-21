# def Reverese(n,rev):
#     if n==0:
#         return rev
#     rem=n%10
#     rev=(rev*10)+rem
#     n//=10
#     return Reverese(n,rev)
# n=int(input('enter a number'))
# res=Reverese(n,0)
# print(res)




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
# n=int(input('entra number'))
# count=CountD(n,0)
# res=Amstrong(n,0,count)
# if n==res:
#     print('amstrng')
# else:
#     print('not a amstrng')    


    
    
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
# n=int(input('entera numer'))    
# count=CountD(n,0)
# res=Amstrong(n,0,count)
# if res==n:
#     print('amstrng')
# else:
#     print('not a amstrng')    




def CountD(n,count):
    if n==0:
        return count
    return CountD(n//10,count+1)
def Amstrong(n,sum,power):
    if n==0:
        return sum
    rem=n%10
    sum=(sum+rem**power)
    return Amstrong(n//10,sum,power)
n=int(input('enter anumber'))
count=CountD(n,0)
res=Amstrong(n,0,count)
if res==n:
    print('amstrng')
else:
    print('not a amstrng')    