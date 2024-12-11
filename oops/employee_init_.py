class employee:
    company_name="abcd"
    location="calicut"
    
    def __init__(self,id,name,salary):
        self.emp_id=id
        self.emp_name=name
        self.emp_salary=salary
    def details(self):
        print(self.emp_id,self.emp_name,self.emp_salary)
                                                          
emp1=employee(102,"sura",2000)       
emp2=employee(102,"jyothi",2001)

emp1.details()
emp2.details()
      
        
        
