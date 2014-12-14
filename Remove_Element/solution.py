class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        while True:
            try:
                A.remove(elem)
            except:
                return len(A)
        return len(A)
