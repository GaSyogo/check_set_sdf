#20201018

"""
check_set_sdf.py
This file implements functions that given a sdf file with many chemical graphs, 
checks and reports the set Lambda of atoms of the given sdf file 
"""


import sys, getopt, os


def getSdfString(inFile):
	ans = str()
	ll = "somestring"
	while ll != "" and ll.find("$$$$") == -1:
		ll = inFile.readline()
		ans += ll
	return ans


def checkSet(sdfString):
	lines = sdfString.splitlines()
	try:
		numVerts = int(lines[3][:3])
	except:
		print(
			'''
			There is something strange with the sdf format.
			Could not read number of vertices 
			''')
		quit()
	vrtxLineBegin = 4
	vertexlist = list()
	for line in lines[vrtxLineBegin : vrtxLineBegin + numVerts]:
		try:
			info = line.split()
			vLabel = info[3] # the atom type in the SDF format
			vertexlist.append(vLabel)
		except:
			print(
				'''
				There was an error in processing
				the connection table
				{}
				'''.format(line))
	return vertexlist


def main(argv):
	inf = argv[1]
	out = set()
	with open(inf) as f:
		sdfString = getSdfString(f)
		#print(sdfString)
		while (sdfString):
			atoms = set(checkSet(sdfString))
			out = out|atoms
			sdfString = getSdfString(f)
	print(out)


main(sys.argv)
