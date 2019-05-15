def SelectionSort(arr,n):
	for i in range(n):
		min_element = i
		for j in range(i+1,n):
			if arr[min_element]>arr[j]:
				min_element = j
		arr[i],arr[min_element] = arr[min_element],arr[i]
		


	return arr



arr = [50,40,30,10,1]
n = len(arr)
print(SelectionSort(arr,n))


"""
Time Complexity: O(n2) as there are two nested loops.


Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is a costly operation.

Exercise :
Sort an array of strings using Selection Sort

Stability : The default implementation is not stable. However it can be made stable. Please see stable selection sort for details.

In Place : Yes, it does not require extra space.

"""
