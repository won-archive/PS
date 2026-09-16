def solution(skill, skill_trees):
    ans = 0
    for skill_tree in skill_trees:
        temp = list(skill)
        
        flag = True
        for st in skill_tree:
            if st in temp:
                if temp[0] == st:
                    temp.pop(0)
                else:
                    flag = False
                    break
        
        if flag:
            ans += 1
        
    return ans