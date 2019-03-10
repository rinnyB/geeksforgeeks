#code
casesNum = int(input())
for e in range(0, casesNum):
    (num, away) = tuple(map(int, input().strip().split(" ")))
    elems = [int(e) for e in input().strip().split(" ")]
    
    for i in range(away, num - away):
        edges = (i - away, i + away + 1)
        elems[edges[0]:edges[1]] = sorted(elems[edges[0]:edges[1]])
        
    print(" ".join([str(e) for e in elems]))