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
	
	def GetVal(self):
		return self.value
	
	def GetNext(self):
		return self.next
	
	def SetNext(self, new):
		self.next = new
	
	def GetPrev(self):
		return self.prev
		
	def SetPrev(self, parent):
		self.prev = parent

class LinkedList(object):
	def __init__(self, head = None, tail = None):
		self.head = head
		self.tail = tail
	
	def AddNode(self, data):
		#create a node at the tail end of the existing list and set its previous to the current tail.
		new = Link(data, self.tail)
		#set the current tails next node to the new node.
		self.tail.SetNext(new)
		#set the Lists tail to the new node.
		self.tail = new
		
	def DelNode(self, node):
		#Get the surrounding nodes.
		left = node.GetPrev()
		right = node.GetNext()
		
		#set the left node to point to the right and vice versa.
		left.SetNext(right)
		right.SetPrev(left)
		
	def Insert(self, node, left, right):
		#Set the nodes new 'prev' and 'next' values
		node.SetNext(right)
		node.SetPrev(left)
		#Set the neighbors to point to node.
		left.SetNext(node)
		right.SetPrev(node)



































