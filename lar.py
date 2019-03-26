def max(x,y,z):
	if x>y and x>z:
		return x
	elif y>x and y>z:	
		return y
	else:
		return z
print("enter three numbers")
x=input()
y=input()
z=input()			
print("the largest of three numbers is=",max(x,y,z))
