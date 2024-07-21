# def Reverese(nstr,i,s1):
#     if i==len(s1):
#         return nstr
#     nstr=s1[i]+nstr
#     return Reverese(nstr,i+1,s1)
# s1=input('enter snum')
# res=Reverese('',0,s1)
# print(res)


# def CountD(n):
#     count=0
#     for i in n:
#         count+=1
#     return count
# s=input('ekj')    
# res=CountD(s)
# print(res)


# def Reverese(nstr,n,s1):
#     if n==len(s1):
#         return nstr
#     nstr=s1[n]+nstr
#     return Reverese(nstr,n+1,s1)
# s1=input('entre')
# res=Reverese('',0,s1)
# print(res)



# class Animal():
#     def Food(self):
#         print("Animal is eating")
#     def Jump(self):
#         print("Animal is jumping")  
#     def Breath(self):
#         print("Animal is breathing") 
#     def Sleep(self):
#         print("Animal is Sleeping") 
                   
# class Lion(Animal): 
#     def eat(self):
#         print("tiger will hunt&eat")
            
# class Deer(Animal):
#     def eat(self):
#         print("deer will grase&eat") 
# class Monkey(Animal): 
#     def eat(self):
#         print("Monkey will steal and eat")  

# T=Lion()
# D=Deer()
# M=Monkey()

# T.eat()
# T.Jump()



class Plane():
    def takeoff(self):
        print("plane takeoff")
    def fly(self):
        print("plane flying")  
    def land(self):
        print("plane landing") 
               
class CPlane(Plane): 
    def carryc(self):
        print("Plane carrying cargo")        
class PPlane(Plane):
    def carryp(self):
        print("Plane carrying passenger")  
class FPlane(Plane): 
    def carryw(self):
        print("Plane carrying weapens")  

C=CPlane()
P=PPlane()
F=FPlane()

C.takeoff()
C.fly()
C.carryc()
C.land()

P.takeoff()
P.fly()
P.carryp()
P.land()

F.takeoff()
F.fly()
F.carryw()
F.land()



# def reverse_string(s):
#     reversed_s = ''
#     for char in s:
#         reversed_s = char + reversed_s
#     return reversed_s
# input_string = "Reverse this string"
# reversed_string = reverse_string(input_string)
# print(reversed_string)

