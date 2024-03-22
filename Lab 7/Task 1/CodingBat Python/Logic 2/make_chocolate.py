def make_chocolate(small, big, goal):
    big_bars_needed = min(big, goal // 5)
    remaining_weight = goal - (big_bars_needed * 5)
    
    if remaining_weight <= small:
        return remaining_weight
    else:
        return -1
