#This program basically works as a Calulator by taking two numbers at a time and performs...
#desired operation

x,y = input("Enter two numbers separated by a space : ").split()
operator = input("Enter the operation you want to do : ")
x = int(x)
y = int(y)

if(operator == '*'):
	result = x*y

elif(operator == '+'):
	result = x+y

elif(operator == '-'):
	result = x-y
	result = abs(result)

elif(operator == '/'):
	result = x/y

else:print("You have entered the wrong operation. Please try again")

print(f"{result}")

