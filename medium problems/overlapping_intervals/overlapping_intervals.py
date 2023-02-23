# O(nlog(n)) time | O(n) space - n is the number of intervals in the input array

def sort_key(interval):
    return interval[0]

def mergeOverlappingIntervals(intervals):

    if len(intervals) == 1:
        return intervals[0]

    intervals.sort(key = sort_key)
    new_intervals = []
    idx = 0
    while idx < len(intervals):
        if idx == len(intervals) - 1 or intervals[idx][1] < intervals[idx+1][0]:
            new_intervals.append(intervals[idx])
            idx += 1
            continue
        
        merged_interval = intervals[idx]
        while idx < len(intervals) - 1 and max(merged_interval[1], intervals[idx][1]) >= intervals[idx+1][0]:
            idx += 1
        merged_interval[1] = max(merged_interval[1], intervals[idx][1])
        new_intervals.append(merged_interval)
        idx += 1
    
    return new_intervals
