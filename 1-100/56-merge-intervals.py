def merge_intervals(intervals):
    res = [intervals[0]]
    intervals.sort()
    for interval in intervals[1:]:
        if interval[0] <= res[-1][1]:
            res[-1][1] = max(interval[1], res[-1][1]) 
        else:
            res.append(interval)
    return res

if __name__ == "__main__":
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))