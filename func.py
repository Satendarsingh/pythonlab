def func1(k):
	print("hii",k)
func1("man")	

def func(a,b,c):
	d=a+b+c 
	print(a,b,c,d)
func(3,4,1)	

def func2(a,b):
	print("hii other function")
	c=a+b
	return c

def func3():
	print("hello, i am going to call the function")	
	s=func2(2,7)
	print("addition is",s)
func3()
		