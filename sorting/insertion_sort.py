def insertion_sort(arr,n):
	if n ==0:
		return
	if n==1:
		return arr[0]
	for i in range(1,n):
		key = arr[i]
		j = i-1
		while(j>=0 and arr[j]>key):
			arr[j+1] = arr[j]
			j=j-1
		arr[j+1] = key
		
	return arr




arr = [7,8,5,4,3,2]
n = len(arr)
print(insertion_sort(arr,n))
