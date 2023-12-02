num = int(input("enter the number: "))
prime = true


for i in range(2,num):
    if(num%i == 0):
        prime = false
        break
if prime:
    print("this number is prime")
else:
    print("this number is not prime")


