# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = [] #���� a �]���ܤp���B�u�u���}�Clist
        while head != None:
            a.append(head.val)
            head = head.next
        print(a) # ���L�X�}�C
        N = len(a)
        for i in range(N): # a���h�ּƦr, i�N�Ӱj��]
            if a[i] != a[N-1-i]: return False # �Y�����ۦP
        return True #���üg
