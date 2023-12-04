#def greet(name):
 #   print("Good Day, "+ name)

#def mySum(num1,num2):
 #   return num1+num2 
#greet("naman")
#s = mySum(6,32)
#print(s)



#n! = 1*2*3*4..*n
#n=0
#n=4
#for i in range(n):
 #   product = product*(i+1)
 
# print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_iter(5)
print(f)
