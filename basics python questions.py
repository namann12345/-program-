#Basic Questions

# write a program print "Hello World".
print("Hello World")


#2.write a program that converts a given number of days into weeks and days

num = int(input("enter number of days"))
year = int(num/365)
week = int(num%365)/7
days = int(num%365)%7


print("total number of years:")
print(year)

print("total number of week(s):")
print(week)

print("total number of day(s):")
print(days)



#3.develop a temperature convert program that cconverts between celcius ,fahrenheit,and kelvin

celcius = float(input('enter temperature in celcius:'))
fahrenheit = 1.8*celcius +32
kelvin = 273.15*celcius


print(fahrenheit)
print(kelvin)



#3.create a program that calculates and and display the area of a triangle using the  base and height provided by the user

a = int(input())
b = int(input())

area = 0.5*a*b
print('area')
