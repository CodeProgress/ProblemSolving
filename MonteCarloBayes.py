import random

# Monte Carlo Bayes

test_sensitivity = .99  # percent chance of true positive
test_specificity = .99  # percent chance of true negative

actual_occurrence_rate = .01

num_trials = 1000000

true_positives = 0
false_positives = 0
true_negatives = 0
false_negatives = 0

for _ in xrange(num_trials):
    is_actual_occurrence = random.random() < actual_occurrence_rate
    if is_actual_occurrence:
        is_true_positive = random.random() < test_sensitivity
        if is_true_positive:
            true_positives += 1
        else:
            false_negatives += 1
    else:
        if random.random() < test_specificity:
            true_negatives += 1
        else:
            false_positives += 1

print "True Positives: \t {}".format(true_positives)
print "False Positives: \t {}".format(false_positives)
print "False Negatives: \t {}".format(false_negatives)
print "True Negatives: \t {}".format(true_negatives)

#expected_num_occurrences = num_trials*actual_occurrence_rate

chance_of_actual_occurrence = float(true_positives)/(true_positives+false_positives)*100

print "If a random person tests positive, the chance of actual occurrence is \
    {}%".format(chance_of_actual_occurrence)
