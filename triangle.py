#Triangle

a=1
for i in range(10,0,-1):
	print(i)
	print(" "*(i)+"*"*a)
	print(a)
	a+=2


#Indian Flag
def print_horizontal(number_of_stars=25):
	print("*"*number_of_stars)

def print_vertical(number_of_stars=5):
	for i in range(number_of_stars):
		print( "*"+" "*23+ "*")

def print_vertical_mid(number_of_stars=7):
	for i in range(2,number_of_stars):
		if i<=3:
		print( "*"+  " "*14+ "*"*2 + " "*23+ "*")

def print_circle():
	pass

print_horizontal()
print_vertical()
print_horizontal()
print_vertical_mid()
print_horizontal()
print_vertical()
print_horizontal()
