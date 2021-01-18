import random


def longest_increasing_subsequence(a_list, smallest_pile_search_function):
    """Returns the longest increasing subsequence within the a_list array
    note, there could be many sequences of the same length, only one arbitrary sequence will be returned.
    Uses the Patience Sorting algorithm: https://en.wikipedia.org/wiki/Patience_sorting"""
    if len(a_list) == 0:
        return []
    if len(a_list) == 1:
        return a_list[::]

    piles = [[a_list[0]]]
    pointers = {(0, 0): (-1, -1)}  # key: from tuple index, value: to tuple index
    for val in (a_list[1:]):
        # if val larger than top value of last pile, make new pile
        if val > piles[-1][-1]:
            piles.append([val])
            from_pointer_pile_index = len(piles)-1

        # else put value in leftmost eligible pile (find via binary search?)
        else:
            from_pointer_pile_index = smallest_pile_search_function(piles, val)
            piles[from_pointer_pile_index].append(val)

        # make pointer to top value on pile immediately left (if there is one)
        index_of_pile_left_of_from_value = from_pointer_pile_index-1
        if index_of_pile_left_of_from_value < 0:
            to_pointer_index = (-1, -1)
        else:
            to_pointer_index = (index_of_pile_left_of_from_value, len(piles[index_of_pile_left_of_from_value])-1)
        from_pointer_val_index = len(piles[from_pointer_pile_index])-1
        pointers[(from_pointer_pile_index, from_pointer_val_index)] = to_pointer_index
    # trace through the pointers from top of the last pile to the first point
    # reverse the numbers in this path
    index_of_top_value_final_pile = (len(piles)-1, len(piles[-1])-1)
    val_of_top_value_final_pile = piles[-1][-1]
    reversed_vals_of_longest_increasing_subsequence = [val_of_top_value_final_pile]
    index_of_next_pile = pointers[index_of_top_value_final_pile]
    while index_of_next_pile != (-1, -1):
        pile_index, val_index = index_of_next_pile
        reversed_vals_of_longest_increasing_subsequence.append(piles[pile_index][val_index])
        index_of_next_pile = pointers[index_of_next_pile]
    vals_of_longest_increasing_subsequence = reversed_vals_of_longest_increasing_subsequence[::-1]
    return vals_of_longest_increasing_subsequence


def get_from_pointer_pile_index(piles, val):
    # starts at left most pile, iterates until valid pile found
    for pile_index in range(len(piles)):
        if val <= piles[pile_index][-1]:
            return pile_index
    return -1


def get_from_pointer_pile_index_binary_search(piles, val):
    # 4 times faster for 100,000 values
    # 20 times faster for 1,000,000 values
    num_piles = len(piles)
    low = 0
    high = num_piles-1

    while low <= high:
        mid = int((high+low)/2)
        if val < piles[mid][-1]:
            high = mid - 1
        elif val > piles[mid][-1]:
            low = mid + 1
        else:
            return mid

    # val not found in list, but now we know where it should go.
    if low > high:
        return low
    return high


assert([0, 2, 6, 9, 11, 15] == longest_increasing_subsequence(
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
    get_from_pointer_pile_index))
assert ([18, 26, 31, 33, 38, 39, 49, 57, 64, 66, 70, 82, 87, 89, 90] == longest_increasing_subsequence(
    [18, 45, 53, 42, 73, 74, 65, 26, 31, 8, 55, 47, 5, 20, 93, 54, 62, 33, 44, 72, 43, 63, 19, 22, 71, 58, 80, 81,
     86, 15, 14, 38, 39, 68, 97, 11, 88, 28, 78, 35, 16, 69, 25, 84, 49, 79, 57, 64, 77, 40, 48, 98, 29, 76, 4, 99, 94,
     37, 24, 96, 92, 13, 1, 66, 27, 70, 3, 52, 30, 41, 56, 82, 87, 75, 23, 91, 17, 36, 89, 10, 85, 60, 46, 67, 32, 95,
     61, 21, 6, 83, 12, 2, 59, 0, 9, 51, 34, 50, 90, 7],
    get_from_pointer_pile_index))

num_rand_tests = 10
for test in range(num_rand_tests):
    rand_num_vals = random.randint(1, 10000)
    rand_nums = random.sample(range(rand_num_vals), rand_num_vals)
    assert(longest_increasing_subsequence(rand_nums, get_from_pointer_pile_index)
           == longest_increasing_subsequence(rand_nums, get_from_pointer_pile_index_binary_search))
