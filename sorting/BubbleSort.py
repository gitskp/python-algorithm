def BubbleSort(arr,n):
	swap=0
	for i in range(n):
		for j in range(n-i-1):
			if arr[j]>arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				swap+=1
	print(swap)
	return arr




arr = [60,50,40,30,20,10,]
n = len(arr)
print(BubbleSort(arr,n))



"""


Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

Auxiliary Space: O(1)

Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

Sorting In Place: Yes

Stable: Yes

"""
