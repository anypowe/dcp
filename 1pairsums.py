#pairsums.py
#nick powers
#8 giugno 2019
#
#daily coding problem #1
#Labeled: EASY
#
#problem description:  	Give a list of numbers 'A' and a number 'k',
#		return whether there is a pair from A 
#		whose sum is k. 
#		Bonus for a one-pass solution
#	e.g. A = [10,15,3,7], k == 17
#	--> A[0]+A[3] == k, True
#input:  array of integers, A
#output: return a pair of indices from A whose sum == k, or (-1,-1) 
#
#solution description:	
#  Assume there can be negatives, repeats. In one pass,
#  keep a dictionary whose values are the indices of A,
#  and whose keys are k - A[i]. When iterating over A,
#  check to see if A[i] completes a pair with a previous index-value.
#  Return the first pair found or False at the end.
#
#  Start from A[0],check if the value is already present 
#  in a (k-A[i])-index dictionary B; if so, return the index at that value
#  with the current index bc their values' sum == k.
#  Otherwise, calculate k-A[i] & store in B with its index 
#
#CURRENTLY WORKS on:
#
#k = 7,  array = [6,3,87,-4,7,5,2,10,15]
#
#
#

import sys

def main():
	#if len(sys.argv) != 2:     #check for correct usage of the program 
	#	print("usage: python3 pairsums.py [source data file]\n")
	#	return 0
	#if wrong arg number, exit
	#
	#print('\n', "File entered:", sys.argv[1], '\n') #echo the argument for user to see in terminal
	#infile = io.open(sys.argv[1], 'r')              #let io method handle other file errors
	
	k = 7
	array = [6,3,87,-4,7,5,2,10,15]
	
	print("testing on: k ==", k,"; array ==", array, "\n")	
	dictB = {} #dictionary: keys == {str(k - array[i]) : i
	#each entry is a pair of k - value, and the index
	#when iterating over the array, the sought-for value may already be in dictB
	
	i = 0
	while i < len(array):
		index2 = dictB.get(array[i])
		if index2 == None: #if the sum-complement is not in the dictionary 
			if dictB.get(k - array[i]) != None: #if this value has already been handled 
				pass #ignore repeats for now
			else:  #add new key-val to the dict
				newpair = {k - array[i] : i}
				dictB.update(newpair)
		else: # array[i] + array[index2] == k 
			print("array[", index2,"], array[",i,"] :")
			print("Values:",array[index2],"+",array[i],"==",k)
			print("")
		i = i + 1
#end main

main()
