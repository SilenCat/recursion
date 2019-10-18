def dq(i, k):
    k *= i
    if i == 1:
        print(k)
        return None
    dq(i-1, k)

dq(int(input('> ')), 1)

