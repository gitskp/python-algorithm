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

