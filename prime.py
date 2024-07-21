# def Prime(n):
#     er=n//2
#     tem=True
#     for i in range(2,er+1):
#         if n%i==0:
#             tem=False
#             break
#     if tem==True:
#         print('prime')
#     else:
#         print('not a prime')        
# n=int(input('enter a number'))        
# Prime(n)



# def Prime(n):
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             return False
#     return True
# sr=int(input('enter a number'))    
# ee=int(input('enter a number'))  
# for i in range(sr,ee+1):
#     if i>1:
#         float=Prime(i)
#         if float==True:
#             print(i)


# def Count(n):
#     CountD=0
#     while n!=0:
#         n//=10
#         CountD+=1
#     return CountD
# n=int(input('enter a nuumere'))    
# res=Count(n)
# print(res)


# def CountD(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
# sr=int(input('enter a number'))    
# er=int(input('enter a number'))   
# for i in range(sr,er+1):
#     res=CountD(i)
#     print(i,"count of digits is",res) 



# def Reverese(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# n=int(input('enter a nymgre'))    
# res=Reverese(n)
# print(res)



# def Reverese(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# sr=int(input('entera v'))    
# er=int(input('entera v'))    
# for i in range(sr,er+1):
#     res=Reverese(i)
#     print(i,"revse valye is ",res)



# def Leep(n):
#     tem=True
#     if (n%100!=0 and n%4==0) or n%400==0:
#         tem=True
#     else:
#         tem=False
#     if tem==True:
#         print('leep year') 
#     else:
#         print('not a leep')       
# n=int(input('enter a number')) 
# Leep(n)


# def Polyndrom(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n=n//10
#     return rev
# n=int(input('ente a numbe')) 
# res=Polyndrom(n)          
# if n==res:
#     print('poly')
# else:
#     print('not a polu')    



# def polu(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=(rev*10)+rem
#         n//=10
#     return rev
# sr=int(input('entera number'))    
# er=int(input('entera number'))    
# tem=True
# for i in range(sr,er+1):
#     res=polu(i)
#     if i==res:
#         print(i)
    
    
    
# def Fibb(n):
#     n1=0
#     n2=1
#     for i in range(1,n+1):
#         print(n1)
#         n3=n1+n2
#         n1,n2=n2,n3 
        
# n=int(input('ente a nunmevbre'))           
# Fibb(n)



# def CountD(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
# def Amstrong(n):
#     tem=n 
#     sum=0
#     power=CountD(n)
#     while n!=0:
#         rem=n%10
#         sum=(sum+rem**power)
#         n//=10
#     return sum
# n=int(input('ente a number'))
# res=Amstrong(n)       
# if res==n:
#     print('amstong')
# else:
#     print('not a smdlf')    
    
    

# def CountD(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
# def Amstrong(n):
#     tem=n 
#     sum=0
#     power=CountD(n)
#     while n!=0:
#         rem=n%10
#         sum=(sum+rem**power)
#         n//=10
#     return sum
# ne=int(input('ente a number'))
# r=int(input('ente a number'))
# res=True  
# for i in range(ne,r+1):
#     tem=Amstrong(i)
#     if tem==True:
#         print(i)
