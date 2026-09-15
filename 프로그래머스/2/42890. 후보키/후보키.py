import itertools

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    ans = []
    for r in range(1, col + 1):
        for comb in itertools.combinations(range(col), r):
            new_comb = list(comb)
            
            seen = set()
            for rel in relation:
                temp = ' '.join(rel[c] for c in new_comb)
                if temp in seen:
                    break
                else:
                    seen.add(temp)
            if len(seen) == row:
                if any(set(a) <= set(new_comb) for a in ans):
                    continue
                ans.append(new_comb)
    
    return len(ans)