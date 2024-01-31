# Example solution
#
# class Employee():
#   new_id = 1
#   def __init__(self, name=None):
#     self.id = Employee.new_id
#     Employee.new_id += 1
#     self._name = name
# 
#   def get_name(self):
#     return self._name
# 
#   def set_name(self, new_name):
#     self._name = new_name
# 
#   def del_name(self):
#     del self._name
# 
# e1 = Employee("Maisy")
# e2 = Employee()
# print(e1.get_name())
# 
# e2.set_name("Fluffy")
# print(e2.get_name())
# 
# e2.del_name()
# print(e2.get_name())


class Employee:

    new_id = 1

    def __init__(self, name=None):
        self.id = Employee.new_id
        Employee.new_id += 1
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def del_name(self):
        del self._name


e1 = Employee("Maisy")
e2 = Employee()

e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())

e2.set_name("Fluffy")
print(e2.get_name())

e2.del_name()
print(e2.get_name())
