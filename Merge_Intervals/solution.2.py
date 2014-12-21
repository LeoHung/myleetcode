class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, key= lambda x: x.start )
        i = 0 
        ret = []
        for e in intervals:
            if len(ret) == 0:
                ret.append(e)
            else:
                last_e = ret[-1]
                if last_e.start <= e.start and e.end <= last_e.end :
                    continue
                elif e.start <= last_e.end and last_e.end < e.end :
                    last_e.end = e.end
                elif last_e.end < e.start: 
                    ret.append(e)
        return ret 