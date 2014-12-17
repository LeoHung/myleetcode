class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num = sorted(num)
        num_len = len(num)

        closest = num[0] + num[1] + num[2]
        minV = abs(target - closest)

        for i in range(num_len -2):
            start = i + 1
            end = num_len - 1

            while start < end:
                tmp = num[start] + num[end] + num[i]
                if tmp > target:
                    if tmp - target < minV:
                        minV = tmp - target
                        closest = tmp
                    end -= 1 
                elif tmp == target:
                    return target
                else:
                    if target - tmp < minV:
                        minV = target - tmp
                        closest = tmp
                    start += 1 

        return closest

if __name__ == "__main__":
    print Solution().threeSumClosest([0, 0, 0], 1)

