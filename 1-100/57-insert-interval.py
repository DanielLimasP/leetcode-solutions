def insert_interval(intervals, new_interval):
    if not intervals:
        intervals = [new_interval]
    start = new_interval[0]
    end = new_interval[1]
    left = right = []
    for interval in intervals:
        if interval[1] < start:
            left.append(interval)
        elif interval[0] > end:
            right.append(interval)
        else:
            start = min(start, interval[0])
            end = max(end, interval[1])
        new_intervals = left + [[start, end]] 
        new_intervals.sort()

    return new_intervals

    
if __name__ == "__main__":
    print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

    
        

        
    