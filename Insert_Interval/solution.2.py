# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def check_intersected(self, inter, newInterval):
        return inter.start <= newInterval.end and newInterval.start <= inter.end   
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        ret = [] 
        isInserted = False
        isMerging = False

        for i, inter in enumerate(intervals):        
            if isInserted:
                ret.append(inter)
            else:
                if i == 0 and newInterval.end < inter.start:
                    ret.append(newInterval)
                    isInserted = True

                if i > 0 and intervals[i-1].end < newInterval.start and newInterval.end < inter.start:
                    ret.append(newInterval)
                    isInserted = True                    

                if not isMerging and self.check_intersected(inter, newInterval):
                    # print i, inter.start, inter.end
                    isMerging = True
                    merged_inter = Interval(min(inter.start, newInterval.start), max(inter.end, newInterval.end))
                    # print merged_inter.start, merged_inter.end


                if isMerging:
                    merged_inter.end = max(merged_inter.end, inter.end)

                    if i < len(intervals)-1:
                        next_inter = intervals[i+1]
                    else:
                        next_inter = None

                    if next_inter is None or merged_inter.end < next_inter.start:
                        ret.append(merged_inter)
                        isInserted = True
                        isMerging = False
                else:
                    ret.append(inter)

        if not isInserted:
            ret.append(newInterval)
            isInserted = True 

        return ret 

if __name__ == "__main__":
    # inter_list = [Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)]
    # newInterval = Interval(4,9)
    inter_list = [Interval(1,5), Interval(6,8)]
    newInterval = Interval(5,6)
    for e in Solution().insert(inter_list, newInterval):
        print e.start, e.end
