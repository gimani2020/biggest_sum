
def biggest_sum(list):
    if list:                   # to cover empty list
        first_inx = 0
        last_inx = 0
        current_inx = 0
        master_sum = list[0]   # to cover list of all negative numbers
        current_sum = 0
		
        for i in range(len(list)):
            current_sum = current_sum + list[i]
            if current_sum < list[i]:
                current_sum = list[i]
                current_inx = i
            if master_sum < current_sum:
                master_sum = current_sum
                first_inx = current_inx
                last_inx = i
				
        print('The max sum in the list is "{}",  '
              'starting at index "{}" till index "{}"'.format(master_sum, first_inx, last_inx))
    else:
        print('list is Empty')


if __name__ == '__main__':

    # a= []
    # a = [8]
    # a = [0, 0, 0, 0, 0, 0]
    # a = [-15, -3, -14, -1, -1, -2, -30, -15]
    a = [-15, 9, 6, -2, 12, 1, -10, 30, 2, 10, -22]
    # a = [1, 6, 4, 2, 9, 7, 13, 7, 1, 4, 30, 5, 5, 5, 5]
    # a = [1, 5, -12, 8, -15, 6, 8, 9, -100, 3, 4294967318345383933, 10, 9]
    biggest_sum(a)
