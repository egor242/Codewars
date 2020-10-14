from collections import OrderedDict


class Array:
    def __init__(self, arr):
        self.arr = arr

    def num_elements(self):
        return len(self.arr)

    def num_values(self):
        return len(set(self.arr))

    def start_end(self):
        return [self.arr[0], self.arr[-1]]

    def range_(self):
        return [min(self.arr), max(self.arr)]

    def largest_increas_subseq(self):
        best_subseq = []
        current_subseq = [self.arr[0]]
        for i in range(1, len(self.arr)):
            if self.arr[i] > self.arr[i-1]:
                current_subseq.append(self.arr[i])
            else:
                if len(current_subseq) > len(best_subseq):
                    best_subseq = current_subseq
                current_subseq = [self.arr[i]]
        if len(current_subseq) > len(best_subseq):
            best_subseq = current_subseq
        if len(best_subseq) > 2:
            return best_subseq
        return "No increasing subsequence"

    def largest_decreas_subseq(self):
        best_subseq = []
        current_subseq = [self.arr[0]]
        for i in range(1, len(self.arr)):
            if self.arr[i] < self.arr[i-1]:
                current_subseq.append(self.arr[i])
            else:
                if len(current_subseq) > len(best_subseq):
                    best_subseq = current_subseq
                current_subseq = [self.arr[i]]
        if len(current_subseq) > len(best_subseq):
            best_subseq = current_subseq
        if len(best_subseq) > 2:
            return best_subseq
        return "No decreasing subsequence"

    def __str__(self):
        d = OrderedDict([('1.number of elements', self.num_elements()),
                        ('2.number of different values', self.num_values()),
                        ('3.first and last terms', self.start_end()),
                        ('4.range of values', self.range_()),
                        ('5.increas subseq', self.largest_increas_subseq()),
                        ('6.decreas subseq', self.largest_decreas_subseq())])
        return str(d)

