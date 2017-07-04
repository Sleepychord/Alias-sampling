# Alias Sampling
## Introduction
这是一个O(1)时间，O(n)空间按给定权重产生随机数的算法。

This is an algorithm to generating random numbers in O(1) time complexity and O(n) space complexity, where the random numbers are generated corresponding to given weights.
## Example
```
from alias_sampling import Alias

if __name__ == '__main__':
    w = [1, 2, 3, 5, 26, 9] # weights
    random = Alias(w)
    cnt = [0] * len(w)
    for i in range(100000):
        cnt[random.random()] += 1 # random
    print 'weights = ', w
    print 'frequency = ', [cnt[i] * 1. / cnt[0] for i in range(len(cnt))]
```

results:

```
weights =  [1, 2, 3, 5, 26, 9]
frequency =  [1.0, 2.023288309268747, 3.0675360968793663, 5.046576618537494, 26.302748020493713, 9.136469492314857]

```