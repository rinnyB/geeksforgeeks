cases = int(input())
for i in range(cases):
    l_lim, r_lim = tuple(map(int, input().strip().split(" ")))
    ls = [int(e) for e in input().strip().split(" ")]
    rs = [int(e) for e in input().strip().split(" ")]
    
    l_idx = 0
    r_idx = 0
    
    res = []
    
    while l_idx < l_lim and r_idx < r_lim:
        if ls[l_idx] < rs[r_idx]:
            res.append(ls[l_idx])
            l_idx += 1
        else:
            res.append(rs[r_idx])        
            r_idx += 1
            
    if l_idx < l_lim:
        res.extend(ls[l_idx:])
    if r_idx < r_lim:
        res.extend(rs[r_idx:])
    
    print(" ".join([str(e) for e in res]))
        
    