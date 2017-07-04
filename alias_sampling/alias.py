import copy
import random
class Alias:
    """
        Alias Sampling is a sampling method.
        it give an random value corresponding to the `weights` in O(1)
        building Alias table need O(n) time
    """
    def __init__(self, weights, eps = 1e-6):
        assert isinstance(weights, list)
        assert len(weights) > 0
        mean = sum(weights) * 1. / len(weights)
        v = copy.copy(weights)
        self.mean = mean
        self.n = len(weights)
        self.table = [0] * self.n
        self.v = v
        QLess = []
        QMore = []
        l1, l2 = 0, 0
        for i in range(self.n):
            if weights[i] < mean - eps:
                QLess.append(i)
            elif weights[i] > mean + eps:
                QMore.append(i)
            else:
                self.table[i] = i
        while l1 < len(QLess) and l2 < len(QMore):
            self.table[QLess[l1]] = QMore[l2]
            v[QMore[l2]] -= mean - v[QLess[l1]]
            if v[QMore[l2]] < mean - eps:
                QLess.append(QMore[l2])
                l2 += 1
            elif v[QMore[l2]] > mean + eps:
                pass
            else:
                self.table[QMore[l2]] = QMore[l2]
                l2 += 1
            l1 += 1
        assert l1 == len(QLess) and l2 == len(QMore)

    def random(self):
        """
        :return: random integer between 0 and len(weights) - 1
        """
        x = random.randint(0, self.n - 1)
        return x if random.random()  * self.mean < self.v[x] else self.table[x]