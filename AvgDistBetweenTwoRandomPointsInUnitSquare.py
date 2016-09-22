import random
import math

# What is the average distance between two random points in a unit square?

def gen_random_point_in_unit_square():
    x = random.random()
    y = random.random()
    return x, y

def dist_between_two_points(point_a, point_b):
    x_leg = point_b[0]-point_a[0]
    y_leg = point_b[1]-point_a[1]
    return math.hypot(x_leg, y_leg)

def est_avg_dist_of_two_random_points_in_unit_square(num_trials=10**6):
    total_distance = 0.
    for _ in xrange(num_trials):
        point_a = gen_random_point_in_unit_square()
        point_b = gen_random_point_in_unit_square()
        total_distance += dist_between_two_points(point_a, point_b)
    
    avg_distance = total_distance/num_trials

    return avg_distance

estimated_avg_dist = est_avg_dist_of_two_random_points_in_unit_square()
actual_avg_dist = (2+2**.5+5*math.log(2**.5+1))/15
difference_between_estimate_and_actual = abs(actual_avg_dist-estimated_avg_dist)

print "Estimate: \t {}".format(estimated_avg_dist)
print "Actual: \t {}".format(actual_avg_dist)
print "Difference: \t {}".format(difference_between_estimate_and_actual)
