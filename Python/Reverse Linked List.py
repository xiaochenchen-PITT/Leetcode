# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reverseList(self, head):
		# # extra space, easy
		# if not head:
		# 	return

		# node = head
		# nodeList = []
		# while node:
		# 	nodeList.append(node)
		# 	node = node.next

		# head = nodeList[-1]
		# node = head
		# for i in range(len(nodeList) - 2, -1, -1):
		# 	node.next = nodeList[i]
		# 	node = node.next
		# node.next = None
		# return head


		# in place, constant space
		if not head:
			return 
		
		beforeNode = None
		while head:
			afterNode = head.next
			head.next = beforeNode
			beforeNode = head
			head = afterNode
		return beforeNode

	def reverseList_recursive(self, head):
		if not head:
			return 

		return self.reverseList_recursive_helper(None, head)

	def reverseList_recursive_helper(self, beforeNode, head):
		if not head:
			return 
		if head and not head.next:
			head.next = beforeNode
			return head

		afterNode = head.next
		head.next = beforeNode
		beforeNode = head
		head = afterNode
		return self.reverseList_recursive_helper(beforeNode, head)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

head = Solution().reverseList_recursive(head)
while head:
	print head.val,
	head = head.next
