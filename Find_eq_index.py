"""
Find an eq index of an array.
An eq index is defined as an index where the sum of the values on both sides are equal.
If no such index exists, return -1

Example: [1,2,4,3] has an eq index of 2. Since sum([1,2] == sum([3]))

Runtime O(n)
Space O(n)
"""

def find_eq_index(a_list, num_elements):
    if len(a_list) == 0:
        return -1
    if len(a_list) == 1:
        return 0
        
    running_sum = [a_list[0]]

    # populate forward
    for i in xrange(1, num_elements):
        cur_total = running_sum[-1]
        running_sum.append(a_list[i]+cur_total)
    
    # run backwards and stop if match
    end_cur_total = a_list[-1]
    if end_cur_total == running_sum[-1]:
        return num_elements-1
    for j in xrange(num_elements-1, 0, -1):
        end_cur_total = end_cur_total + a_list[j-1]
        if end_cur_total == running_sum[j-1]:
            return j-1
    
    # if no match, there are no eq indices
    return -1
    
# Tests
assert find_eq_index([-1], 1) == 0

assert find_eq_index([-1,3], 2) == -1

assert find_eq_index([-1,3,-4], 3) == -1

assert find_eq_index([-1,3,-4,5], 4) == -1

assert find_eq_index([-1,3,-4,5,1], 5) == -1

assert find_eq_index([-1,3,-4,5,1,-6], 6) == -1

assert find_eq_index([-1,3,-4,5,1,-6,2], 7) == 2
