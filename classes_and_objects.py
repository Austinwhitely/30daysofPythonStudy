import statistics as s
import numpy as np
from collections import Counter

ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]


class Statistics:
    def __init__(self, data):
        self.data = data

    def get_count(self):
        return len(self.data)

    def get_sum(self):
        return np.sum(self.data)

    def get_min(self):
        return np.min(self.data)

    def get_max(self):
        return np.max(self.data)

    def get_range(self):
        return max(self.data) - min(self.data)

    def get_mean(self):
        return s.mean(self.data)

    def get_median(self):
        return s.median(self.data)

    def get_mode(self):
        return s.mode(self.data)

    def get_std(self):
        return s.stdev(self.data)

    def get_var(self):
        return s.variance(self.data)

    def get_freq_dist(self):
        counts = Counter(self.data)
        total = len(self.data)

        sorted_items = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

        return [((counts / total) * 100, age) for age, counts in sorted_items]


data_set = Statistics(ages)
print("Count:", data_set.get_count())
print("Sum: ", data_set.get_sum())
print("Max: ", data_set.get_max())
print("Range: ", data_set.get_range())
print("Mean: ", data_set.get_mean())
print("Median: ", data_set.get_median())
print("Mode: ", data_set.get_mode())
print("Standard Deviation: ", data_set.get_std())
print("Variance: ", data_set.get_var())
print("Frequency Distribution: ", data_set.get_freq_dist())
