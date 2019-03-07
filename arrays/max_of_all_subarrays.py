# black magic f......
casesNum = int(input())
data = []
for e in range(0, casesNum):
    (num, window) = tuple(map(int, input().strip().split(" ")))
    elems = [int(e) for e in input().strip().split(" ")]
    # slow and mem ineffective
    # windows = [elems[i: i + window] for i in range(0, num - window + 1)]
    # maxs = [max(elems[i: i + window]) for i in range(0, num - window + 1)]

    
    # instead of finding a max over all windows,
    # find a max in a first window,
    # then, roll
    # if the new element is bigger than max, it is new max
    # (else) if not: check if older max falls out of new window 
    # then we have to find max over new window
    # (else) if it didn't fall out (new elem still smaller than max)
    # we maintain old max, as max for new window

    maxs = []
    max1 = max(elems[:window])
    maxs.append (max1)

    for i in range(window, num):
        if elems[i] > max1:
            max1 = elems[i]
            maxs.append(max1)
        elif elems[i - window] == max1:
            max1 = max(elems[i - window + 1: i + 1])
            maxs.append(max1)
        else:
            maxs.append(max1)
    res = " ".join([str(e) for e in maxs])
    print(res)
    
    
    