def greatestnumber(a,b,c):

	if a>b:
		if a>c:
			print("A is great!")
		elif a == c:
	 		print("A and C are equal and great!")
		else:
			print("C is great!")
	elif b>c:
		if b>a:
			print("B is great!")
		else:
			print("A is great!")
	elif a==b:
			print("A and B are equal and great1")
	elif b==c:
		print("B and C are equal and great!")
	else:
		print("c is great!")

greatestnumber(5,5,2)




