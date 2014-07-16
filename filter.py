#!/usr/bin/python

import sys

f = open(sys.argv[1])
lines = f.readlines()

f1 = open('unigram', 'a')
f2 = open('bigram', 'a')
for line in lines:
	line = line.strip()
	if line.find(' ') == -1:
		f1.write(line + '\n')
	else:
		f2.write(line + '\n')


f1.close()
f2.close()
f.close()