class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def find(self, left, right, num, target):
        if right - left <= 3 :
            for i in range(left,  right, 1):
                if num[i] == target:
                    return True
            return False
        else:
            mid = (left + right) / 2 
            l = num[left]
            m = num[mid]
            r = num[right-1]

            if target == l or target == m or target == r:
                return True

            if l < m and l < target and target < m :
                return self.find(left, mid, num, target)
            elif l > m and (l < target or target < m ):
                return self.find(left, mid, num, target)

            if m < r and m < target and target < r :
                return self.find(mid, right, num, target )
            elif m > r and (m < target or target < r ):
                return self.find(mid, right, num, target) 

            if l == m: 
                return self.find(left, mid, num, target) or self.find(mid, right, num, target)

            return False

    def search(self, A, target):
        return self.find(0, len(A), A, target)

if __name__ == "__main__":
    print Solution().search([1, 3],3)
    print Solution().search([], 9)
    print Solution().search([1,1], 9)
    print Solution().search([1,1,1], 1)
    print Solution().search([7, 8 ,9 , 9, 10, 3, 4, 5, 6 ], 9)
    print Solution().search([7, 8 ,9 , 9, 10, 3, 4, 5, 6 ], 22)
