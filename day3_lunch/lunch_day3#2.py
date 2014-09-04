#!/usr/bin/env python

"""
For each alignment, print the longest stretch of fully aligned bases in that alignment
"""

import sys

output = []
length_max = 0
x = 0

"""while True:
    line = sys.stdin.readline()
    if line.startswith("Query="):
        fly_name1 = line.rstrip("\r\n").split(" ")
        fly_name = fly_name1[2]
    if line.startswith(">"):
        hum_name1 = line[1:].rstrip("\r\n").split(" ")
        hum_name = hum_name1[1]
        print fly_name, hum_name   
    if line == "":
        break   """     
        


while True:
    line = sys.stdin.readline()
    if line.startswith("Query "):    
        d_line = sys.stdin.readline()
        b_line = sys.stdin.readline()
        dash1 = d_line.rstrip("\r\n").split(" ")
        for i in dash1:
            length = len(i)
            #print i
            if length >= length_max:
                length_max = length
                x += 1
            else:
                pass
    if line.startswith(">"):
        pass
        #do it over again
        """d_line = sys.stdin.readline()
        b_line = sys.stdin.readline()
        dash1 = d_line.rstrip("\r\n").split(" ")
        for i in dash1:
            length = len(i)
            #print i
            if length >= length_max:
                length_max = length
            else:
                pass"""                 
    if line == "":
        break
print length_max    
#print x



                #top_line = line.rstrip("\r\n").split(" ")
                #top = top_line[2]
                #bottom_line = b_line.rstrip("\r\n").split(" ")
                #bottom = bottom_line[2]  