#3missingint.py
#nick powers
#13 giugno 2019
#
#daily coding problem #4
#Labeled Hard 
#
#problem description: Given an array of integers, 
#	find the 1st missing positive integer in O(n) & constant space.
#	I.e. find the lowest positive integer not in the array.
#	The array can contain duplicates and negatives
#
#	E.g. [3,4,-1,1] -> 2
#	E.g. [1,2,0] -> 3
#
#approached from one described here:
#https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/
# "We use array elements as index. To mark presence of an element x, 
# we change the value at the index x to negative. But this approach 
# doesn’t work if there are non-positive (-ve and  numbers. So we 
# segregate positive from negative numbers as first step and then apply the approach."
#

#swap()
#simple swap for two indices a,b of an array
#returns updated array
def swap(array, a, b):
	temp_a = array[a]
	array[a] = array[b]
	array[b] = temp_a
	return array
#end swap()

#update_irrel()
#returns the newly updated index just before the irrelevant value section
def update_irrel(array, irrel):
	while (array[irrel] < 1) or (array[irrel] > len(array)) : 
		if irrel == 0:
			break
		else:   
			irrel = irrel - 1
	return irrel
#end irrel

#partial_sort(array)
#first pass of the array to partially sort relevant values from irrelevant ones:
#a relevant value is a positive integer < len(array) + 1: O(n)
#
#input: original array to check
#postconditions: array is partially sorted, returns last index before irrel section
#
#this could be optimized more by making another pass and pushing more values to the irrel section;	
#since we now know the lengths of the relevant and irrelevant sections, values > len(rel_section)
#are no longer relevant: e.g, [2,1,6,1,-3,-3,-2,1]
#at first, only -3,-2 are irrelevant; after the first pass, we see the len of rel section < 6, 
#and it is shown to be irrelevant at this point
def partial_sort(array):
	i = 0 
	irrel = len(array) - 1 #last index before the irrel section starting from the end
	irrel = update_irrel(array,irrel) #if the last is irrel, update until reaching an index with +rel

	#move i from beginning to until it reaches the irrel section, 
	#swapping irrels's, and updating the irrel...
	while i < irrel:
		if (array[i] < 1) or (array[i] > len(array)): #if a swap is needed
			swap(array,i,irrel)	
			irrel = update_irrel(array,irrel) #update the dividing index
		if i == irrel:  #if i is at the at the last relevant value (bc of the updating)
			pass
		else:
			i = i + 1
	
	if i == len(array) - 1:
		i = -1  #code for all rels's
	elif (i == 0) and (array[i] < 1):
		i = -2 #code for all irrel's
	
	#array is partially sorted
	return i #i is the index where the irrels's start
#end partial_sort()


#find_int(array_irrel)
#
#Using the technique described above, we'll use the index to look for the missing int
#go through rel list (i.e. vals within index of array), and change:
#array[i-1] = -(array[i-1]), i.e. the negative indicates the value for that index is present
#at the end, the lowest index with a positive value (in the rel section), is the missing value.
#If all are negative, the array contains all consecutive pos ints from 1 -> len(array), 
#and the next value is that + 1.
#this could be optimized more by making another pass and pushing more values to the irrel section;
#since we now know the lengths of the relevant and irrelevant sections, values > len(rel_section)
#are no longer relevant: e.g, [2,1,6,1,-3,-3,-2,1]
#at first, only -3,-2 are irrelevant; after the first pass, we see the len of rel section < 6, 
#and it is shown to be irrelevant at this point
#
def find_int(array, irrel):
	end = 0
	if irrel == -1: #all values in the array are relevant
		end = len(array) - 1
	elif irrel == -2: #all irrels
		return 1 #the first missing int is 1
	else:
		end = irrel 

	i = 0
	while i <= end:
		#e.g. a = [3,1,4,-1]; a[a[0]-1] == a[3-1] == 4 to be neg (the third slot is marked)...	
		if array[abs(array[i]) - 1] < 0:
			pass
		else:
			array[abs(array[i]) - 1] = -(array[abs(array[i]) - 1]) 
		i = i + 1
	
	#traverse the array and the first index with an unmarked val is the missing number.
	i = 0
	while i <= end:
		if array[i] > 0:
			return i + 1
		i = i + 1
	#if all slots were marked, missing int = len(array) + 1
	return end + 2
#end find_int()


#wrapper for the two primary functions
#handles a couple corner cases...
def wrapper(array):

	print("")
	print("Original array:", array)
	if len(array) == 0:#didn't handle this well in the other functions...
		print("empty array... lowest missing +int == 1\n")	
	elif len(array) == 1: #didnt't handle this well in the other functions...
		if array[0] != 1:
			print("lowest missing +int == 1\n") 
		else:
			print("lowest missing +int == 2\n")	
	else:
		irrel = partial_sort(array)
		print("after partial sort:", array)
		if irrel == -2:
			print("all values <= 0...")
		elif irrel == -1:
			print("all values are relevant i.e. +ints <= len(array)")
		else:
			print("relevant index section ends after index", irrel)
		missing = find_int(array, irrel)
		print("lowest missing +int ==", missing,'\n')

#end wrapper

def main():

	#test cases
	ex1 = [3, 4, -1, 1] #answ == 2
	ex2 = [1,2,0] #answ == 3
	ex3 = [1,7,2,11,-3,12,0,-1,2,13,3,4,-2,-1] # answ = 5
	ex4 = [-3,-4,0,-5,-1,-6,0,-3]
	ex5 = [2,3,7,1,2,1,2,50,100,8,4,6,5,9,11,40,12,30] #all +, answ == 10
	ex6 = [0, -2, 30, 15, -5] #irrels
	ex7 = [1,1,3,1,3,2,4,1] #all rels with repeats
	ex8 = [-2,-4,4,1,9,-2,-5,400,53,2,6,3,1,9,-2,0,10]
	ex9 = [1,2,3,4,5]
	ex10 = [0]
	ex11 = []
	ex12 = [4,5,4,3,5,3,2,3,5,6,3]
	ex13 = [0,0]
	ex14 = [2]
	ex15 = [1]
	ex16 = [2,2]

	tests = [ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11,ex12,ex13,ex14,ex15,ex16]
	
	for i in tests:
		wrapper(i)	

	return 0
#end main

main()
