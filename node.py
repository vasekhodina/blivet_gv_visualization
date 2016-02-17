class Node(object):
	def __init__(self,name,disk_type,status="",uuid="",path="",size=""):
		self.__name=name
		self.__disk_type=disk_type	
		self.__attributes = {}
		self.__label = ""
		if status != "":
			self.__attributes['status'] = status
		if uuid != "":
			self.__attributes['uuid'] = uuid
		if path != "":
			self.__attributes['path'] = path
		if size != "":
			self.__attributes['size'] = size
	def setName(name):
		self.__name=name
	def setType(disk_type):
		self.__disk_type=disk_type
	def getName(self):
		return self.__name
	def getType(self):
		return self.__disk_type
	def getLabel(self):
		return self.__label
	def prepare(self):
		print self.__name
		self.__label = "Name: " + self.__name + "\n" + "Type: " + self.__disk_type + "\n"	
		print self.__label
		for k,v in self.__attributes.iteritems():
			self.__label = self.__label + str(k) + ": " + str(v) + "\n"
