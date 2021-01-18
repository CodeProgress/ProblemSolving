import random


def longest_increasing_subsequence(a_list, function_find_index_leftmost_valid_pile_to_insert_value):
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
        index_of_new_value = create_index_for_new_val(piles, function_find_index_leftmost_valid_pile_to_insert_value, val)
        insert_value_at_index(piles, val, index_of_new_value)

        index_of_value_to_point_to = get_index_of_value_to_point_to(index_of_new_value, piles)
        pointers[index_of_new_value] = index_of_value_to_point_to

    backwards_path_values = values_following_back_pointers_from_top_card_of_final_pile(piles, pointers)
    vals_of_longest_increasing_subsequence = backwards_path_values[::-1]  # reverse since the path was backwards
    return vals_of_longest_increasing_subsequence


def values_following_back_pointers_from_top_card_of_final_pile(piles, pointers):
    index_of_top_value_final_pile = (len(piles) - 1, len(piles[-1]) - 1)
    val_of_top_value_final_pile = piles[-1][-1]
    values_along_back_path = [val_of_top_value_final_pile]
    index_of_next_pile = pointers[index_of_top_value_final_pile]
    while index_of_next_pile != (-1, -1):
        pile_index, val_index = index_of_next_pile
        values_along_back_path.append(piles[pile_index][val_index])
        index_of_next_pile = pointers[index_of_next_pile]
    return values_along_back_path


def create_index_for_new_val(piles, function_find_index_leftmost_valid_pile_to_insert_value, val):
    # 2d index as tuple: (pile index, value index)
    top_value_of_final_pile = piles[-1][-1]
    if val > top_value_of_final_pile:
        index_for_new_val = (len(piles), 0)

    # else put value in leftmost eligible pile (find via binary search?)
    else:
        index_of_pile = function_find_index_leftmost_valid_pile_to_insert_value(piles, val)
        index_for_new_val = (index_of_pile, len(piles[index_of_pile]))
    return index_for_new_val


def insert_value_at_index(piles, val, index_of_new_value):
    index_of_final_existing_pile = len(piles)-1
    pile_index = index_of_new_value[0]
    if pile_index > index_of_final_existing_pile:
        new_pile = [val]
        piles.append(new_pile)
    else:
        piles[pile_index].append(val)


def get_index_of_value_to_point_to(index_of_new_value, piles):
    pile_index = index_of_new_value[0]  # todo make named tuples for all indices
    index_of_pile_left_of_from_value = pile_index - 1
    if index_of_pile_left_of_from_value < 0:
        to_pointer_index = (-1, -1)
    else:
        index_of_value_within_to_pile = len(piles[index_of_pile_left_of_from_value]) - 1
        to_pointer_index = (index_of_pile_left_of_from_value, index_of_value_within_to_pile)
    return to_pointer_index


def get_index_leftmost_pile(piles, val):
    # starts at left most pile, iterates until valid pile found
    for pile_index in range(len(piles)):
        if val <= piles[pile_index][-1]:
            return pile_index
    return -1


def get_index_leftmost_pile_binary_search(piles, val):
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


# Assertion tests:

# Deterministic
assert([0, 2, 6, 9, 11, 15] == longest_increasing_subsequence(
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
    get_index_leftmost_pile))
assert ([18, 26, 31, 33, 38, 39, 49, 57, 64, 66, 70, 82, 87, 89, 90] == longest_increasing_subsequence(
    [18, 45, 53, 42, 73, 74, 65, 26, 31, 8, 55, 47, 5, 20, 93, 54, 62, 33, 44, 72, 43, 63, 19, 22, 71, 58, 80, 81,
     86, 15, 14, 38, 39, 68, 97, 11, 88, 28, 78, 35, 16, 69, 25, 84, 49, 79, 57, 64, 77, 40, 48, 98, 29, 76, 4, 99, 94,
     37, 24, 96, 92, 13, 1, 66, 27, 70, 3, 52, 30, 41, 56, 82, 87, 75, 23, 91, 17, 36, 89, 10, 85, 60, 46, 67, 32, 95,
     61, 21, 6, 83, 12, 2, 59, 0, 9, 51, 34, 50, 90, 7],
    get_index_leftmost_pile))

# Randomized, mostly to test function_find_index_leftmost_valid_pile_to_insert_value
num_rand_tests = 10
for test in range(num_rand_tests):
    rand_num_vals = random.randint(1, 10000)
    rand_nums = random.sample(range(rand_num_vals), rand_num_vals)
    assert(longest_increasing_subsequence(rand_nums, get_index_leftmost_pile)
           == longest_increasing_subsequence(rand_nums, get_index_leftmost_pile_binary_search))
