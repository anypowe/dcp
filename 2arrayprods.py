#2arrayprod.py
#nick powers
#10 giugno 2019
#
#daily coding problem #2
#Labeled Hard
#
#problem description: Given an array of integers, return a new array
#	such that each element at index i of the new array is the
#	product of all the numbers in the original array except at i
#
#e.g.: a = [1,2,3,4,5], output should be: [120,60,40,30,24]
#e.g.: b = [3,2,1], output should be: [2,3,6]
#
#1 Simple solution: multiply all numbers and then divide by each array[i]
#Follow-up: What if you can't use division? 
#
#2 Brute force solution time complexity of O(n^2), space O(1): start from scratch each time
#
#3 my solution (not complete): find the products of all adjacent pairs and store.
#
#4 solution (found online): find the cumulative products of all vals starting from the left and 
#       again from the right in two different arrays. For a given array[i], multiply left[i-1]*right[i+1]
#	e.g. a = [3, 7,  4,  2,   1,   6,    5]
#	  left = [3, 21, 84, 168, 168, 1008, 5040]
#	  right = [5040, 1680, 240, 60, 30, 30, 5]
#	  a[2] = 4, output = left[1] * right[3] --> 21*60 == 1260; 5040/4 == 1260 (correct)
#	Time complexity: O(n)*3
#	Space complexity: ... could get very large with large values 	
#	

def arrprods(array):
	if len(array) < 3:
		return array
	#calculate cumulative products ascending from left to right for each i in array
	left2right = []
	total = 1
	for i in array:
		total = total * i    #find cumulative product for this spot
		left2right.append(total)#put product in this list
	# ... from right to left ... 
	right2left = []
	ct  = len(array) - 1
	total = 1
	while ct >= 0:
		total = total * array[ct]
		right2left.insert(0,total) #starting from the end, so always add to the front
		ct = ct - 1 
	#calculate the product of all numbers in the array except for i,
	#insert product in the index of the new array
	prods = []
	ct = 0
	while ct < len(array):
		if ct == 0: #corner case: first element
			prods.append(right2left[ct + 1])
		elif ct == len(array) - 1: #last element
			prods.append(left2right[ct - 2])
		else: #general case: cumulative product of numbers leading up to array[ct] from the left * 
		      # * that from the right, then append it to the new list
			val = left2right[ct - 1] * right2left[ct + 1]
			prods.append(val)
		ct = ct + 1 		
	return prods
#end arrprods()

def main():
	a = [3,7,4,2,1,6,5]
	print("\nInput:",a,"\nOutput:",arrprods(a),"\n")
#end main

main()


