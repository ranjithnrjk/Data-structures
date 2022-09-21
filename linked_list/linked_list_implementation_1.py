class Node:
	"""It creates a node with a values and address to next element"""
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinekdList:
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



if __name__ == "__main__":
	ll = LinekdList()
	ll.insert_at_beginnig(77)
	ll.insert_at_end(56)
	ll.insert_at_end(77)
	ll.insert_at_beginnig(56)
	ll.Print()
	print(ll.get_length())
	ll.insert_values(["A",'B','C','D','E','F','G','H','I','J','k','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	print(ll.get_length())
	ll.Print()
	ll.insert_values(["banana","mango","grapes","orange"])
	print(ll.get_length())
	ll.Print()
	ll.Print()
	ll.Print()
	ll.insert_at("blueberry",1)
	ll.remove_at(2)
	ll.Print()    
	ll.insert_values([45,7,12,567,99])
	ll.insert_at_end(67)
	ll.Print()