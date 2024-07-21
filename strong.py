def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def strong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += factorial(digit)
        temp //= 10
    return sum

number = int(input("Enter a number: "))
res=strong(number)
if res==number:
    print('strong number')
else:
    print('not a strong number')


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def sum_of_digit_factorials(num):
#     if num == 0:
#         return 0
#     else:
#         digit = num % 10
#         return factorial(digit) + sum_of_digit_factorials(num // 10)

# def is_strong_number(num):
#     return sum_of_digit_factorials(num) == num

# number = int(input("Enter a number: "))
# if is_strong_number(number):
#     print(f"{number} is a strong number.")
# else:
#     print(f"{number} is not a strong number.")




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
