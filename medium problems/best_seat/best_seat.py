# O(n) time | O(1) space - where n is the number of seats

def bestSeat(seats):
    best_seat = -1
    start_idx = 0
    max_space = 0
    
    while start_idx < len(seats):
        if seats[start_idx] == 0:
            num_spaces = 0
            end_idx = start_idx
            while end_idx < len(seats) and seats[end_idx] == 0:
                end_idx += 1
                num_spaces += 1
            if num_spaces > max_space:
                max_space = num_spaces
                best_seat = (start_idx + end_idx - 1) // 2
            start_idx = end_idx
        else:
            start_idx += 1
    return best_seat
    