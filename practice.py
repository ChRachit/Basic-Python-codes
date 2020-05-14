#merging two arrays
def merge_sort(array1, array2):
	i = 0
	j = 0
	k = 0
	n1 = len(array1)
	n2 = len(array2)
	merged_array = [None] * (n1 + n2)

	if array1 == []:
		return array2
	if array2 == []:
		return array1

	while i < n1 and j < n2:
		print(array1, array2)
		print(merged_array)
		if array1[i] < array2[j]:
			merged_array[k] = array1[i]
			k = k + 1
			i = i + 1
		elif array1[i] == array2[j]:
			merged_array[k] = array1[i]
			k = k + 1
			i = i + 1
		else:
			merged_array[k] = array2[j]
			k = k + 1
			j = j + 1

	return merged_array
#geekforgeeks code
def mergeArrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0

    # Traverse both array
    while i < n1 and j < n2:

        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1


    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = arr1[i];
        k = k + 1
        i = i + 1

    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = arr2[j];
        k = k + 1
        j = j + 1
    print("Array after merging")
    for i in range(n1 + n2):
        print(str(arr3[i]), end = " ")
        
#array rotation
def array_rotate(array, d):
    n = len(array)
    for i in range(d):
        left_rotate(array)
        
def left_rotate(array):
    temp = array[0]
    for i in range(len(array) - 1):
        array[i] = array[i + 1]
    array[len(array) - 1] = temp

def print_array(array):
    for i in range(len(array)):
        print(array[i])

#splitting array and adding it to the end 
def split_array(array, k):
    for i in range(0, k):
        temp = array[0]
        for j in range(0, len(array) - 1):
            array[j] = array[j + 1]
        array[len(array) - 1] = temp
    for i in range(0, len(array)):
        print(array[i])
split_array([1, 3, 5, 7], 2)

#monotonic arrays
def monotonic_array(array):
	increasing = True
	decreasing = True
	for i in range(len(array) - 1):
		if array[i] > array[i + 1]:
			increasing = False
		if array[i] < array[i + 1]:
			decreasing = False

	return increasing or decreasing
#geeksforgeeks
def isMonotonic(A):

    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

#multiplication of array elements and div by n
        def array_multiply(array, n):
                l = len(array)
                product = 1
                for i in range(l):
                        product = array[i] * product
                total = product % n
                print(total)

#delete nth occurence of a given word
def delete(l, w, n):
	count = 0
	for i in range(len(l)):
		if l[i] == w:
			count += 1
		if count == n:
			del l[i]
			
	return l
#multiply list elements
def mul_list(l):
	product = 1
	for i in range(len(l)):
		product = product * l[i]
	return product

def min(l):
	#smallest element in a list
	l.sort()
	return l[0]
	"""smallest = 0
	for i in range(len(l)):
		if smallest > l[i]:
			smallest = l[i]

	return smallest"""

def max(l):
	#max element in a list
	l.sort()
	return l[-1]

def sec_max(l):
	#max element in a list
	l.sort()
	print(l)
	return l[-2]

def n_max(l, n):
	l.sort(reverse = True)
	elements = [None] * n
	for i in range(n):
		elements[i] = l[i]
	print(elements)
	return elements
def n_max(l, n):
	#find N max elements from a list
	l.sort(reverse = True)
	elements = [None] * n
	for i in range(n):
		elements[i] = l[i]
	print(elements)
	return elements
def even(l):
	#even numbers in alist
	even = []
	for i in range(len(l)):
		if l[i] % 2 == 0:
			even.append(l[i])
	return even
def odd(l):
	#odd numbers in a list
	odd = []
	for i in range(len(l)):
		if l[i] % 2 != 0:
			odd.append(l[i])
	return odd






