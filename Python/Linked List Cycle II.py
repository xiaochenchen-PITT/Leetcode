# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def detectCycle(self, head):
		if not head:
			return 

		fast = head
		slow = head
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if fast == slow:
				while head != slow:
					head = head.next
					slow= slow.next
				return head
		return