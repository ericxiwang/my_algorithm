#list sort


def list_sort(input_list):
	print input_list
	input_list = sorted(input_list)
	return "build in",input_list

def bubble_sort(input_list):
	loop_len = len(input_list)
	for i in range(loop_len):
		for j in range(0,loop_len-i-1):
			if input_list[j] > input_list[j+1]:
				input_list[j],input_list[j+1] = input_list[j+1],input_list[j]
	return "bubble",input_list

def quick_sort(input_list):
	if len(input_list) <= 1:
		return input_list
	pivot = input_list[len(input_list)/2]
	left = [x for x in input_list if x < pivot]
	print "left",pivot,left
	middle = [x for x in input_list if x == pivot]
	print "middle",pivot
	right = [x for x in input_list if x > pivot]
	print "right",pivot,right
	return quick_sort(left) + middle + quick_sort(right)

if __name__ == '__main__':
	new_list = [12,34,32,12,45,67,87,4,5,9999,220]
	print list_sort(input_list = new_list)
	print bubble_sort(input_list = new_list)
	print quick_sort(input_list = new_list)