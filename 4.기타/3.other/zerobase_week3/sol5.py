def solution(reward, health, optional):
    return recursive(1, 0, reward, health, optional)

def recursive(attack, current, reward, health, optional):
    if current == len(reward):
        return 0
    
    time = (health[current] + attack - 1) // attack
    path_a = time + recursive(
        attack + reward[current],
        current + 1,
        reward, health, optional
    )
    
    if optional[current] == 0:
        return path_a
    else:
        path_b = recursive(
            attack,
            current + 1,
            reward, health, optional
        )
        return min(path_a, path_b)
