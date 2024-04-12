#Print "Hello World" as user want.
'''
num = int(input("Enter an integer: "))
i = 0
while (i<num):
    print("Hello World")
    i+=1
    '''

#Take 10 integers from the user using a while loop and calculate their average.
'''
sum = 0
i = 0
while (i<5):
    num = int(input("Enter a number: "))
    sum +=num
    i +=1
average = sum / 4
print("The average of the numbers are ", average)
'''

#Finding prime number
'''
num = int(input("Enter a number: "))
prime = 0
i = 2
while (i<10):
    x = i
    prime01 = num % i
    if(prime01 == 0):
        prime +=1
        break
    else:
        i += 1
if (prime == 1):
    print("The entered number is not prime.")
    print("The number is divisible by", x)
else:
    print("The entered number is prime.")
'''

#print the all prime numbers til user input using for loop
'''
num = int(input("Enter a number: "))
i = 2
while (i<=num):
    prime = 0
    for var in range(2,i):
        if(i%var==0):
            prime = 1
            break
    if(prime == 0):
        print(i,end="")
    i+=1
'''

#print count on numbers b/w two integers divisble by third integer
'''
num1 = int(input("Enter a number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
count = 0
while (num1<=num2):
    if(num1%num3==0):
        print(num1,"divisible by ",num3)
        count += 1
    num1+=1
print(count, "divisible by ",num3)
'''

#Profile picture uploading on facebook account
len = int(input("Enter photo dimension:"))
num = int(input("Enter number of photos:"))
i = 1
while (i<=num):
    width = int(input("Enter width of photo: "))
    length = int(input("Enter length of photo:"))
    if (width < len or length < len):
        print("Upload Another one")
    elif (width > len or length > len):
        print("Crop it.")
    else:
        print("Accepted")
    i += 1
