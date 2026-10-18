def solution(bandage, health, attacks):
    q = attacks[:]
    
    t = 0   # 시간
    s = 0   # 연속 성공
    cur_health = health
    
    while q:
        if cur_health <= 0:
            return -1 
            
        if t == q[0][0]:    # 공격
            at, d = q.pop(0)
            cur_health -= d
            s = 0
        else:
            # 초당 회복
            diff = health - cur_health
            if diff > 0:
                cur_health += bandage[1] if diff >= bandage[1] else diff
                
            # 추가 회복
            diff = health - cur_health
            if s == bandage[0] and diff > 0:
                cur_health += bandage[2] if diff >= bandage[2] else diff
                s = 0
            
        # print(t,cur_health, s)
        t += 1
        s += 1
    
    return cur_health if cur_health > 0 else -1 