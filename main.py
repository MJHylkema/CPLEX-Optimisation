import os
import sys
import timeit
import re

SOURCE = []
TRANSIT = []
DESTINATION = []
H = {}


def initializeConstants(argv):
	for i in range(int(argv[1])):
		SOURCE.append(i+1)
	for k in range(int(argv[2])):
		TRANSIT.append(k+1)
	for j in range(int(argv[3])):
		DESTINATION.append(j+1)
	
	for i in SOURCE:
		for j in DESTINATION:
			H[str(i)+str(j)] = i+j


def writeMinimize(file):
	file.write("Minimize\n")
	file.write("     r\n")
	return file


def writeConstraints(file):
	file.write("Subject to\n")
	
	for i in SOURCE:
		for j in DESTINATION:
			file.write("     demandflow{}{}:   ".format(i, j))
			for k in TRANSIT:
				file.write("x{}{}{}".format(i, k, j))
				if k != TRANSIT[len(TRANSIT)-1]:
					file.write(" + ")
			file.write(" = {}\n".format(H[str(i)+str(j)]))
	
	for i in SOURCE:
		for k in TRANSIT:
			file.write("     cap{}{}X:         ".format(i, k))
			for j in DESTINATION:
				file.write("x{}{}{}".format(i, k, j))
				if j != DESTINATION[len(DESTINATION)-1]:
					file.write(" + ")
			file.write(" - c{}{} <= 0\n".format(i, k))
	
	for k in TRANSIT:
		for j in DESTINATION:
			file.write("     capX{}{}:         ".format(k, j))
			for i in SOURCE:
				file.write("x{}{}{}".format(i, k, j))
				if i != SOURCE[len(SOURCE)-1]:
					file.write(" + ")
			file.write(" - d{}{} <= 0\n".format(k, j))
	
	for i in SOURCE:
		for j in DESTINATION:
			for k in TRANSIT:
				file.write("     flow{}{}{}:        ".format(i, k, j))
				file.write("3 x{0}{1}{2} - {3} U{0}{1}{2} = 0\n".format(i, k, j, H[str(i)+str(j)]))
	
	for i in SOURCE:
		for j in DESTINATION:
			file.write("     nbFlows{}{}:      ".format(i, j))
			for k in TRANSIT:
				file.write("U{}{}{}".format(i, k, j))
				if k != TRANSIT[len(TRANSIT)-1]:
					file.write(" + ")
			file.write(" = 3\n")
	
	for k in TRANSIT:
		file.write("     TRANSIT{}:       ".format(k))
		for i in SOURCE:
			for j in DESTINATION:
				file.write(" x{}{}{}".format(i, k, j))
				if not (i == SOURCE[len(SOURCE)-1] and j == DESTINATION[len(DESTINATION)-1]):
					file.write(" + ")
		file.write(" - r <= 0\n")
	return file


def writeBounds(file):
	file.write("Bounds\n")
	
	file.write("     0 <= r\n")
	
	for i in SOURCE:
		for k in TRANSIT:
			for j in DESTINATION:
				file.write("     0 <= x{}{}{}\n".format(i, k, j))
	return file


def writeBinary(file):
	file.write("Binary\n")
	
	for i in SOURCE:	
		for j in DESTINATION:
			for k in TRANSIT:
				file.write("     U{}{}{}\n".format(i, k, j))
	return file


def executeLP(lpfilename):
	os.system('cplex -c "read ' + lpfilename + '" "optimize" "display solution variables -" >> ./Solution.txt')


def findResult(lines):
	cap=0
	caps = []
	count = 0
	
	for line in lines:
		if line.startswith("r"):
			r = float(line[1:-1])
		if line.startswith("c") or line.startswith("d"):
			count += 1
			if float(line[3:-1]) > cap:
				cap = float(line[3:-1])
				caps = []
				caps.append(line[:3])
			elif float(line[3:-1]) == cap:
				caps.append(line[:3])
	return count, r, cap, caps



def main():
	
	if len(sys.argv) != 4:
		sys.exit("Wrong number of arguments: " + str(len(sys.argv)))
	
	initializeConstants(sys.argv)
	
	lpfilename = "main.lp"
	file = open(lpfilename, 'w')
	
	file = writeMinimize(file)
	file = writeConstraints(file)
	file = writeBounds(file)
	file = writeBinary(file)
	file.write("End")
	file.close()
	
	file = open("Solution.txt", 'w')
	file.close()
	
	start_time = timeit.default_timer()
	executeLP(lpfilename)
	elapsed = timeit.default_timer() - start_time
	
	print("Execution for " + sys.argv[2] + " transit nodes:")
	print("Time of execution: " + str(elapsed) + " secs")
	
	file = open("Solution.txt")
	lines = file.readlines()
	file.close()
	
	count, r, cap, caps = findResult(lines)
	
	print("Minimized transit load = " + str(r))
	print("Number of links with non-zero capacities: " + str(count))
	print("Highest capacity: " + str(cap) + " held by " + str(caps) + "\n")
		


main()
