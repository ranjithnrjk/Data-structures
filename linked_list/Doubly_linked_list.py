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

		return count


	def insert_values(self, data):
		self.head = None
		for i in data:
			self.insert_at_end(i)


	def insert_at(self, index, data):
		if index < 0 or index > self.get_length():
			raise Exception("Invalid index")
			return

		if index == 0:
			self.insert_at_beginning(data)
			return

		itr = self.head
		count = 0
		while itr:
			if count == index-1:
				node = Node(data, itr.next, itr)
				itr.next.prev = node
				itr.next = node
				break
			itr = itr.next
			count += 1




if __name__ == '__main__':
	ll = DoublyLinkedList()
	# ll.insert_values([*range(0,100,10)])
	ll.insert_at(0, 500)
	ll.Print()
	print(ll.get_length())