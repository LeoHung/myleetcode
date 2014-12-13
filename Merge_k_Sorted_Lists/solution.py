# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MinHeap:
    def __init__(self, unsorted):
        self._array = self.sort(unsorted)

    def len(self):
        return len(self._array)

    def sort(self, unsorted):
        self._array = unsorted

        for i in range(len(self._array)-1, 0, -1):
            parent = (i-1) / 2
            if self._array[parent][0] > self._array[i][0]:
                self._array[parent], self._array[i] = self._array[i], self._array[parent]
                self.correct(i)

                # print "sort", self._array

        return self._array

    def correct(self, parent_i):

        a_l = len(self._array)

        parent = self._array[parent_i]

        left_child_i = 2 * parent_i +1
        right_child_i = 2 * parent_i + 2

        if left_child_i < a_l and right_child_i < a_l:
            left_child = self._array[left_child_i]
            right_child = self._array[right_child_i]

            if left_child[0] <= right_child[0] and left_child[0] < parent[0]:
                self._array[parent_i], self._array[left_child_i] = self._array[left_child_i], self._array[parent_i]
                self.correct(left_child_i)
            elif right_child[0] < left_child[0] and right_child[0] < parent[0]:
                self._array[parent_i], self._array[right_child_i] = self._array[right_child_i], self._array[parent_i]
                self.correct(right_child_i)

        elif left_child_i < a_l and right_child_i >= a_l:
            left_child = self._array[left_child_i]

            if left_child[0] < parent[0]:
                self._array[parent_i], self._array[left_child_i] = self._array[left_child_i], self._array[parent_i]

    def coorect_bottom_up(self, child_i):
        if child_i == 0 or child_i >= len(self._array):
            return

        parent_i = (child_i -1) / 2

        child = self._array[child_i]
        parent = self._array[parent_i]

        if parent[0] > child[0]:
            self._array[parent_i], self._array[child_i] = self._array[child_i], self._array[parent_i]
            self.coorect_bottom_up(parent_i)


    def pop(self):
        pair = self._array[0]
        last_pair = self._array.pop()

        if len(self._array) > 0:
            self._array[0] = last_pair
            self.correct(0)

        # print "pop", self._array

        return pair

    def push(self, pair):
        self._array.append(pair)
        self.coorect_bottom_up(len(self._array) - 1)

        # print "push", self._array


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        unsorted  = []
        for i, l in enumerate(lists):
            if l is not None:
                unsorted.append((l.val, i))
                lists[i] = l.next

        minHeap = MinHeap(unsorted)

        ret_head = ListNode(-1)
        ret_tail = ret_head

        while minHeap.len() > 0:
            min_pair = minHeap.pop()
            ret_tail.next = ListNode(min_pair[0])
            ret_tail = ret_tail.next

            if lists[min_pair[1]] is not None:
                new_val = lists[min_pair[1]].val
                minHeap.push((new_val, min_pair[1]))
                lists[min_pair[1]] = lists[min_pair[1]].next

        ret_head = ret_head.next

        return ret_head




def printList(node):
    while node is not None:
        print node.val,
        node = node.next

def genList( array ):
    head = ListNode(-1)
    tail = head
    for e in array:
        tail.next = ListNode(e)
        tail = tail.next
    return head.next


if __name__ == "__main__":
    listoflistp = [
                    genList([-8,2,4]),
                    genList([-9,-9,-9,-9,-8,-5,-3,-2,1]),
                    genList([-9,-7,-5,-3,-3,-1,0,3,4]),
                    genList([-9,-7,-6,-4,-2,-1,3,4]),
                    genList([-10,-3,0]),
                    genList([-9,0,4]),
                    genList([-8,-8])
                ]

    listoflistp = [
                    genList([-3,2,2]),
                    genList([-9]),
                    genList([-10,-5,-4,-2,-1,1,3,4]),
                    genList([-10,-9,-8,3,4]),
                    genList([-5,-3,3,4]),
                    genList([-9,-8,-5,-4,-2,-1,3])
                ]


    printList( Solution().mergeKLists(listoflistp) )
