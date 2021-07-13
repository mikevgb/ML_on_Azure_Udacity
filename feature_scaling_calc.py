# Scaling data means transforming it so that the values fit within some range or
# scale, such as 0–100 or 0–1. There are a number of reasons why it is a good 
# idea to scale your data before feeding it into a machine learning algorithm.

import math
import statistics

#parse imput, remove empty elements and make a list
u_input = input("Enter values ")
u_input = list(map(int, u_input.split()))

#standarization
print ("\nStandarization")
mean = sum(u_input) / len(u_input)
standar_deviation = statistics.stdev(u_input)
for x in u_input:
	y = (x - mean) / standar_deviation
	print (y)

#normalization
print ("\nNormalization")
min_n = min(u_input)
max_n = max(u_input)

for x in u_input:
	y = (x - min_n) / (max_n - min_n)
	print (y)