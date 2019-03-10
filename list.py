# Creation of a linked list.

'''
Practice with traditional list
list = []
entry = 0
print("Enter a value:")
val=input()
while val != '':
	list.append(val)
	print("Enter a value:")
	val = input()
	
print(list)
'''

#definition of a link.
#Each link should know the link before it and the link after.
#{
#	value = string
#	next = object
#	prev = object
#}
class Link(object):
	def __init__(self, value=None, prev=None, next=None):
		self.value = value
		self.next = next
		self.prev = prev
	
	def get_Val(self):
		return self.value
	
	def get_next(self):
		return self.next
	
	def set_next(self, new):
		self.next = new
	
	def set_prev(self, parent):
		self.prev = parent

class LinkedList(object):
	def __init__(self, head = None, tail = None):
		self.head = head
		self.tail == tail
	
	def AddNode(self, data):
		#create a node at the tail end of the existing list.
		new = Link(data, self.tail, None)
		#set its previous to the current tail
		new.prev = self.tail
		#set the old tails next node to the new node.
		self.tail.next = new
		#set the Lists tail to the new node
		self.tail = new



































