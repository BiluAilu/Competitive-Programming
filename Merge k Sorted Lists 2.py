import heapq
# class ListNode:
#     def __init__(self,val ,next):
#         self.val=val
#         self.next=None
class Solution(object):
    def mergeKLists(self,lists):
        heap=[]
        result_node=temp_node=ListNode(None)
        for listnode in lists:
            while listnode:
                heapq.heappush(heap,listnode.val)
                listnode=listnode.next 
        while heap:
            temp_node.next=ListNode(heapq.heappop(heap))
            temp_node=temp_node.next 
        return result_node.next