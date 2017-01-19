"""
Output all possibilities to put "+" or "-" or nothing between the numbers
1, 2, 3, 4, 5, 6, 7, 8 and 9 (in this order) such that the result is 100
Example: 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100.
"""

import Queue


def bfs(start, goal, successor_function):
    count = 0
    visited = set()
    q = Queue.Queue()
    q.put(start)
    while not q.empty():
        cur_path = q.get()
        if eval(cur_path) == goal and cur_path[-1] == "9":
            if count <100:
                print cur_path
        for add_on in successor_function(cur_path):
            next_val = cur_path + add_on
            if next_val not in visited:
                q.put(next_val)
                visited.add(next_val)
    return "Done!"

def next_expression(val):
    if val[-2:] == "10":
        return ()
    next_val = str(int(val[-1]) + 1)
    minus = "-" + next_val
    plus = "+" + next_val
    num = next_val
    return [minus, plus, num]


print bfs("1", 100, next_expression)
