from alias import Alias
import random
if __name__ == '__main__':
    w = [random.randint(0, 10) for i in range(100)]
    w[0] = 1
    random = Alias(w)
    cnt = [0] * len(w)
    for i in range(1000000):
        cnt[random.random()] += 1
    print [cnt[i] * 1. / cnt[0] - w[i] for i in range(len(cnt))]