import random
import math

# What is the average area of a random triangle in a unit square?

def gen_random_point_in_unit_square():
    x = random.random()
    y = random.random()
    return x, y

def dist_between_two_points(point_a, point_b):
    x_leg = point_b[0]-point_a[0]
    y_leg = point_b[1]-point_a[1]
    return math.hypot(x_leg, y_leg)

def area_of_triangle(point_a, point_b, point_c):
    ab = dist_between_two_points(point_a, point_b)
    bc = dist_between_two_points(point_b, point_c)
    ca = dist_between_two_points(point_c, point_a)
    
    perimeter = ab + bc + ca
    semi_perimeter = perimeter/2.
    
    area = (semi_perimeter
            *(semi_perimeter-ab)
            *(semi_perimeter-bc)
            *(semi_perimeter-ca)
            )**0.5
    
    return area

def est_avg_area_of_random_triangle_in_unit_square(num_trials=10**6):
    total_area = 0.
    for _ in xrange(num_trials):
        point_a = gen_random_point_in_unit_square()
        point_b = gen_random_point_in_unit_square()
        point_c = gen_random_point_in_unit_square()
        total_area += area_of_triangle(point_a, point_b, point_c)
    
    avg_area = total_area/num_trials

    return avg_area

estimated_avg_dist = est_avg_area_of_random_triangle_in_unit_square()
actual_avg_dist = 11/144.
difference_between_estimate_and_actual = abs(actual_avg_dist-estimated_avg_dist)

print "Estimate: \t {}".format(estimated_avg_dist)
print "Actual: \t {}".format(actual_avg_dist)
print "Difference: \t {}".format(difference_between_estimate_and_actual)
