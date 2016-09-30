import time

def get_n_digit_grouping_dict(num_digits, constant):
    grouping_dict = {}
    max_index = len(constant)-num_digits
    for i in xrange(max_index + 1):
        n_digit_grouping = ""
        for digit_offset in xrange(num_digits):
            n_digit_grouping += constant[i+digit_offset]

        num_secs_to_print_grouping = i+num_digits
        # only record first occurence
        if n_digit_grouping not in grouping_dict:  
            grouping_dict[n_digit_grouping] = [num_secs_to_print_grouping]
    
    return grouping_dict

def get_digits_from_file(file_name):
    with open(file_name, 'r') as pi_digits:
        digits = ""
        for line in pi_digits:
            if line[-1] == '\n':
                digits += line[:-1]
            else:
                digits += line
    return digits

#pi = "314159265358979323846"
#e = "271828182845904523536"
#root_two = "14142135623730"

pi = get_digits_from_file("pi_digits.txt")
e = get_digits_from_file("e_digits.txt")
root_two = get_digits_from_file("root_two_digits.txt")


num_digits = 5

pi_dict = get_n_digit_grouping_dict(num_digits, pi)
e_dict = get_n_digit_grouping_dict(num_digits, e)
root_two_dict = get_n_digit_grouping_dict(num_digits, root_two)

common_digit_groupings = set(pi_dict.keys()) & set(e_dict.keys()) & set(root_two_dict.keys())

lowest_print_time = 10**10
best_num_to_pick = 0
for g in common_digit_groupings:
    total_print_time = sum(pi_dict[g] + e_dict[g] + root_two_dict[g])
    if total_print_time < lowest_print_time:
        lowest_print_time = total_print_time
        best_num_to_pick = g
        
        print best_num_to_pick, time.strftime("%H:%M:%S", time.gmtime(lowest_print_time))

print "Five digit num to select: {}".format(best_num_to_pick)
print "Length of time to win: {}".format(time.strftime("%H:%M:%S", time.gmtime(lowest_print_time)))

