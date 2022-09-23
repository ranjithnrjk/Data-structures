class Node:
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next
		self.prev = prev

class DoublyLinkedList:
	def __init__(self):
		self.head = None


	def insert_at_beginning(self,data):
		if self.head is None:
			node = Node(data, None, None)
			self.head = node
			return

		node = Node(data, self.head, None)
		self.head.prev = node
		self.head = node

		

	def insert_at_end(self, data):
		if self.head is None:
			node = Node(data, None, None)
			self.head = node
			return

		itr = self.head
		while itr.next:
			itr = itr.next
		node = Node(data, None, itr.data)
		itr.next = node


	def Print(self, F_or_B = "forward"):
		if self.head is None:
			raise Exception("LinkedList is empty")

		itr = self.head 
		llstr_b = []
		llstr = ''
		while itr:
			llstr += str(itr.data) + " --> " if itr.next else str(itr.data)
			llstr_b.append(str(itr.data))
			itr = itr.next

		if F_or_B == 'forward':
			print(llstr)
		elif F_or_B == "backward":
			llstr_b.reverse()
			for i in llstr_b:
				print(i, ' --> ', end='')
			print("None")


	def get_length(self):
		count = 0
		itr = self.head
		while itr:
			itr = itr.next
			count += 1

		print(count)


if __name__ == '__main__':
	ll = DoublyLinkedList()
	ll.insert_at_end(4)
	ll.insert_at_end(3)
	ll.insert_at_end(2)
	ll.Print()
	ll.get_length()