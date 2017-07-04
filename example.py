from alias_sampling import Alias

if __name__ == '__main__':
    w = [1, 2, 3, 5, 26, 9]
    random = Alias(w)
    cnt = [0] * len(w)
    for i in range(100000):
        cnt[random.random()] += 1
    print 'weights = ', w
    print 'frequency = ', [cnt[i] * 1. / cnt[0] for i in range(len(cnt))]