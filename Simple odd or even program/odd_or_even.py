import sys
import os

def main():
	os.system('cls')
	print("\t\tDetermine an odd or even number\n\n")
	dev = int(input("hello please insert number : "))
	while True:
		try:
			if dev == 0:
				print("numer is 0")
			elif dev % 2 == 0:
				print("number is even")
			elif dev % 2 != 0:
				print("number is odd")
			
			while True:
				x = str(input("Try again (y/n) ? : "))
				if x == 'y':
					main()
				elif x == 'n':
					sys.exit()
				else:
					print('Invalid , wanna try again ?')
					if x == 'y':
						main()
					elif x == 'n':
						sys.exit()
		except ValueError:
			print("Please insert a number")
			sys.exit()
main()
