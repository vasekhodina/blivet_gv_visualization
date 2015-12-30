class Node(object):
	def __init__(self,name,disk_type,size=0):
		self.__name=name
		self.__disk_type=disk_type	
		self.__size=size
	def setName(name):
		self.__name=name
	def setSize(size):
		self.__size=size
	def setType(disk_type):
		self.__disk_type=disk_type
	def getName(self):
		return self.__name
	def getType(self):
		return self.__disk_type
	def getSize(self):
		return self.__size
