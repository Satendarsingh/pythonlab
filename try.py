try:
	a=int(input("enter the value"))
	if a==5:
		raise NameError
	elif a>5:
		raise TypeError

except NameError:
	print("error the value is equal to 5")			
except TypeError:
	print("error the value is greater than 5")
else:
	print("no error",a)		
finally:
	print("execution successfull")