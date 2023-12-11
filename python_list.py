
#this question consists of 5 parts pertaining to the following Python 2.x code snippet:
def generate_sample_list(limit = 100):
    sample_list = []
    for i in range(1, limit):
        if i * (i - 2) % 3 == 0:
            sample_list.append(i**2)
    return sample_list

l = generate_sample_list()


#generate string  via list comprehension
new_list = [i**2 for i in range(1,100) if i*(i-2)%3 == 0]
print new_list

a = "12345"
def list_reverse(input_list):

	input_list = list(input_list)
	loop_len = int(len(input_list)/2)
	list_len = len(input_list) -1
	for i in range(loop_len):
		input_list[i],input_list[list_len] = input_list[list_len],input_list[i]
		list_len = list_len -1
	input_list= "".join(input_list)
	return input_list
def fib(n):
    if n <= 1:
        return 1
    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


def fib1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)
if __name__ == '__main__':
	print list_reverse(new_list)
