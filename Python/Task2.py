#This program generates a password taking characters & symbols randomly from a string

import random

def PassGen(n):
	chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$&"
	result = [random.choice(chars) for _ in range(n)]
	print(f"{''.join(result)}")

def main():
	n = int(input("Enter the length of your password : "))
	PassGen(n)	

if __name__ == "__main__":
	main()
