class employee:
    def __init__(self, name, age, department, is_manager):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
        
employee1 = employee("islam", 56, "marketing", True )      
employee2 = employee("kaoutar", 60, "facebook", False)
print(employee1.name)

