'''
Problem: Build a "staircase" of a given height.
For example, height 5 would look like:
    #
   ##
  ###
 ####
#####
'''


def staircase(num_steps):
    stairs = ""
    for step_level in xrange(1, num_steps+1):
        spaces = build_spaces(step_level, num_steps)
        step = build_step(step_level)
        stairs += spaces + step + '\n'
    return stairs


def build_spaces(step_level, num_steps):
    return " " * (num_steps-step_level)


def build_step(step_level):
    return "#" * (step_level)


print staircase(5)
