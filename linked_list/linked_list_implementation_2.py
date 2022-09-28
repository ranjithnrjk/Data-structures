class Node:
	"""It creates a node with a values and address to next element"""
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def Print(self):
		if self.head is None:
			print("LinekdList is empty")
			return

		itr = self.head
		llstr = ''
		while itr:
			llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
			itr = itr.next

		print(llstr)


	def insert_at_beginnig(self, data):
		if self.head is None:
			node = Node(data, None)
			self.head = node
			return

		node = Node(data, self.head)
		self.head = node

	def insert_at_end(self, data):
		if self.head is None:
			node = Node(data,None)
			self.head = node
			return

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(data, None)

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


	def insert_at(self, data, index):
		if index < 0 or index > self.get_length():
			raise Exception ("Invalid index")

		if index == 0:
			self.insert_at_beginnig(data)
			return

		itr = self.head
		count = 0
		while itr:
			if count == index - 1:
				node = Node(data, itr.next)
				itr.next = node
				break
			itr = itr.next
			count += 1


	def remove_at(self, index):
		if index < 0 or index > self.get_length():
			raise Exception ("Invalid index")

		if index == 0:
			self.head = self.head.next
			return

		itr = self.head
		count = 0
		while itr:
			if count == index -1:
				itr.next = itr.next.next
				break

			itr = itr.next
			count += 1


	def insert_after_value(self, data_after, data_to_insert):
		if self.head is None:
			raise Exception ("LinekdList is empty")

		itr = self.head
		while itr:
			if itr.data == data_after:
				node = Node(data_to_insert, itr.next)
				itr.next = node
				break
			itr = itr.next


	
	def remove_by_value(self, data):
		if self.head is None:
			raise Exception ("LinekdList is empty")

		if self.head.data == data:
			self.head = self.head.next
			return

		itr = self.head
		if_data_exists = False
		while itr.next:
			if itr.next.data == data:
				itr.next = itr.next.next
				if_data_exists = True
				break
			itr = itr.next
		if not if_data_exists:
			print(f"{data} is/are not present in LinkedList.")


if __name__ == "__main__":
	# ll = LinkedList()
	# ll.insert_values([1,2,3,4])
	# ll.Print()
	# ll.insert_after_value(4,5)
	# ll.Print()
	# ll.insert_after_value(1,1.5)
	# ll.Print()
	# ll.remove_by_value(1.5)
	# ll.Print()
	ll = LinkedList()
	ll.insert_values(["banana","mango","grapes","orange"])
	ll.insert_at(500, 2)
	ll.Print()
	# ll.insert_after_value("mango","apple") # insert apple after mango
	# ll.remove_by_value("orange") # remove orange from linked list
	# ll.Print()
	# ll.Print()
	# ll.remove_by_value("figs")
	# ll.Print()
	# ll.remove_by_value("banana")
	# ll.remove_by_value("mango")
	# ll.remove_by_value("apple")
	# ll.remove_by_value("grapes")
	# ll.Print()
