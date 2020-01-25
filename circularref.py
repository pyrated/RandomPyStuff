#To demonstrate the concept of circular references and the working of garbage collector

import ctypes
import gc

#Reference Counter
def ref_count(address):
	return ctypes.c_long.get_address(address).value

#Checks if object is present in garbage collection list
def object_by_id(object_id):
	for obj in gc.get_objects():
		if id(obj) == object_id:
			return "Object Exists"
		return "Not Found"

#First Class
class A:
	def __init__(self):
		self.b = B(self)
		print('A: self: {0}, b: {1}'.format(hex(id(self))), hex(id(self.b)))

#Second Class
class B:
	def __init__(self, a):
		self.a = a
		print('B: self: {0}, a: {1}'.format(hex(id(self))), hex(id(self.a)))

gc.disable() #Disables automatic garbage collection

my_var = A()

#Storing memory addresses of the two instances 'a' and 'b'
a_id = id(my_var)
b_id = id(my_var.b)

my_var = None #my_var is no longer pointing to the memory location of 'a'

#Before garbage collection
object_by_id(a_id)
object_by_id(b_id)

gc.collect() #garbage collection manually turned on

#After garbage collection
object_by_id(a_id)
object_by_id(b_id)
