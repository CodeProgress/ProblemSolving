# Find the longest common substring
# using dynamic programming

# ex: longest_common_substring("abcdef", "jbcdaf") = "bcd"

def longest_common_substring(str_a, str_b):
    solution = [[0 for b in range(len(str_b)+1)]
                for a in range(len(str_a)+1)]
    max_sub_str_len = 0
    indices_of_max = (0,0)
    for a_i in range(1, len(str_a)+1):
        for b_i in range(1, len(str_b)+1):
            if str_a[a_i-1] == str_b[b_i-1]:
                sub_str_len = 1 + solution[a_i-1][b_i-1]
                solution[a_i][b_i] = sub_str_len
                if sub_str_len > max_sub_str_len:
                    max_sub_str_len = sub_str_len
                    indices_of_max = (a_i, b_i)
    print "length of substring = {}, indices of max substring = {}".format(max_sub_str_len, indices_of_max)
    for row in solution:
        print row
    sub_str = ""
    a, b = indices_of_max
    while solution[a][b] != 0:
        sub_str += str_a[a-1] # -1 to account for off by 1 between solution and str indices
        a -= 1
        b -= 1
    return sub_str[::-1]

str_a = "abcdaf"
str_b = "bcdf"
str_c = "xyz"
str_d = "abcdaf"
str_e = "abcdefghijklmnopqrs"
str_f = "abcde_fghijklmnopqr"

print longest_common_substring(str_e, str_f)

# print longest_common_substring(str_e, str_f)

# length of substring = 13, indices of max substring = (18, 19)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# fghijklmnopqr