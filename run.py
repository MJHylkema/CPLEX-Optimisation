import os

def main():
	file = open("Results.txt", "w")
	file.close()
	for y in range(3,8):
		os.system("python3 main.py 7 " + str(y) + " 7 >> Results.txt")

main()
