#!/usr/bin/env python3

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = []

for filename in filenames:
	index = filename.index(".")
	if (filename[index:] == ".hpp"):
		allhppfiles = filename[:index] + filename[index:index+2]
		newfilenames.append(allhppfiles)
	elif (filename[index:] != ".hpp"):
		newfilenames.append(filename)

print(newfilenames) 