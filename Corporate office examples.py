#Corporate Example
class Employee:
    empcount=0
    incamt=1.10
    def __init__(self):
        self.first=input("Enter first name :")
        self.last=input("Enter last name :")
        self.salary=int(input("Enter Salary :"))
        self.email=f"{self.first.lower()}.{self.last.lower()}@gmail.com"
        Employee.empcount+=1

    def increment(self):
        self.salary=self.salary*self.incamt

    def details(self):
        print (f"Full Name of Employee : {self.first.title()} {self.last.title()}")
        print (f"Salary of Employee : {self.salary}")
        print (f"Email ID of Employee : {self.email}")
        if(self.prolang!=None):
            print(f"Skills in Programming Language : {self.prolang}")
            
    def fullname(self):
        print(f"Full Name of Employee : {self.first.title()} {self.last.title()}")
    
class developer(Employee):
    incamt=1.30
    def __init__(self):
        super().__init__()
        self.prolang=input("Enter Programming Language :")

class manager(Employee): 
    def __init__(self): 
        super().__init__()
        print("Enter Employees under manager, or enter as 'None' for No employees")
        self.employees=[]
        if(self.employees is None):
            self.employees=[]

    def addemp(self,emp):
        if(emp not in self.employees):
            self.employees.append(emp)

    def removeemp(self,emp):
        if(emp in self.employees):
            self.employees.remove(emp)

    def printemp(self):
        for emp in self.employees:
            print(f"{emp.fullname()}")

abc=True
while(abc):
    
        print("WELCOME TO EMPLOYEE MANAGEMENT APPLICATION")
        print("""
                1. Employee Operations
                2. Developer operations
                3. Manager Operations
                """)
        x=int(input("Enter your choice :"))
    
        if(x==1):
            print("""
                    1. To add an Employee 
                    2. For employee's increment
                    3. To Check their details
                 """)
            z=int(input("Enter your choice :"))
            if(z==1):
                emp1=Employee()
                c=1
                while(c<=3):
                    i=input("""
                           To add another Employee press '+'
                           or '0' To go back
                           NOTE : You can add upto 3 Employees""")
                    if(i=="+" and c==1):
                        emp2=Employee()
                        c+=1
                    elif(i=="+" and c==2):
                        emp3=Employee()
                        c+=1
                        print("Employee list is full, you can not add more employees")
                        break
                    elif(i=="0"):
                        break
                    else:
                        print("Invalid choice")

            elif(z==2):
                p=int(input("""To increment salary of employee 1, press '1'
                               To increment salary of employee 2, press '2'
                               To increment salary of employee 3, press '3'
                                Enter employee number : """))
                if(p==1):
                    emp1.increment()
                    print(f"Proposed incremented salary : {emp1.salary}")
                elif(p==2):
                    emp2.increment()
                    print(f"Proposed incremented salary : {emp2.salary}")
                elif(p==3):
                    emp3.increment()
                    print(f"Proposed incremented salary : {emp3.salary}")
                else:
                    print("Employee not found")
                
            elif(z==3):
                p=int(input("""
                               For Details of employee 1, press '1'
                               For Details of employee 2, press '2'
                               For Details of employee 3, press '3'
                               Enter employee number : """))
                if(p==1):
                    emp1.details()
                elif(p==2):
                    emp2.details()
                elif(p==3):
                    emp3.details()
                else:
                    print("Employee not found")
            elif(z==0):
                break
            else:
                ("Invalid Choice")
        
        elif(x==2):
            print("""
                    1. To add a developer 
                    2. For Developer's increment
                    3. To Check their Full Name
                  """)
            z=int(input("Enter your choice :"))
            if(z==1):
                dev1=developer()
                u=1
                while(u<=3):
                    i=input("""
                               To add another developer press '+'
                               or '0' to go back
                               NOTE : You can add upto 3 Develoeprs""")
                    if(i=="+" and u==1):
                        dev2=developer()
                        u+=1
                    elif(i=="+" and u==2):
                        dev3=developer()
                        u+=1
                        print("Developer list is full, you can not add more developer")
                        break
                    elif(i=="0"):
                        break
                    else:
                        print("Invalid Choice")
                                             
            elif(z==2):
                p=int(input("""To increment salary of developer 1, press '1'
                               To increment salary of developer 2, press '2'
                               To increment salary of developer 3, press '3'
                                Enter developer number : """))
                if(p==1):
                    dev1.increment()
                    print(f"Proposed incremented salary : {dev1.salary}")
                elif(p==2):
                    dev2.increment()
                    print(f"Proposed incremented salary : {dev2.salary}")
                elif(p==3):
                    dev3.increment()
                    print(f"Proposed incremented salary : {dev3.salary}")
                else:
                    print("Employee not found")

            elif(z==3):
                p=int(input("""For Details of developer 1, press '1'
                               For Details of developer 2, press '2'
                               For Details of developer 3, press '3'
                               Enter developer number : """))
                if(p==1):
                    dev1.details()
                elif(p==2):
                    dev2.details()
                elif(p==3):
                    dev3.details()
                else:
                    print("Developer not found")
                    
        elif(x==3):
            print("""
                    1. To add Manager
                    2. To add/remove employees
                    3. To enlist the employees
                  """)
            z=int(input("Enter your choice :"))
        
            if(z==1):
                q=int(input("""
                               To create manager for employees, press '1'
                               To create manager for Developers, press '2':"""))            
                if(q==1):
                    print("Enter first name, last name, salary of manager & list of employees under manager")
                    if(c==1):
                        print("""
                             list of employees :
                             1. emp1""")
                        mgr1=manager()
                        while(True):
                            b=int(input("""To add employees under manager,
                                       1. emp1
                                       0. Exit
                                       Enter the number :"""))
                            if(b==1):
                                emp=emp1
                            elif(b==0):
                                break
                            else:
                                print("No such employee listed")
                            mgr1.employees.append(emp)
                    elif(c==2):
                        print("""
                             list of employees :
                             1. emp1
                             2. emp2
                             """)
                        mgr1=manager()
                        while(True):
                            b=int(input("""To add employees under manager,
                                       1. emp1
                                       2. emp2
                                       0. Exit
                                       Enter the number :"""))
                            if(b==1):
                                emp=emp1
                            elif(b==2):
                                emp=emp2
                            elif(b==0):
                                break
                            else:
                                print("No such employee listed")
                            mgr1.employees.append(emp)
                    elif(c==3):
                        print("""
                             list of employees :
                             1. emp1
                             2. emp2
                             3. emp3
                             """)
                        mgr1=manager()
                        while(True):
                            b=int(input("""To add employees under manager,
                                   1. emp1
                                   2. emp2
                                   3. emp3
                                   0. Exit
                                   Enter the number :"""))
                            if(b==1):
                                emp=emp1
                            elif(b==2):
                                emp=emp2
                            elif(b==3):
                                emp=emp3
                            elif(b==0):
                                break
                            else:
                                print("No such employee listed")
                            mgr1.employees.append(emp)
                            continue
                elif(q==2):
                    print("Enter first name, last name, salary of manager & list of employees under manager")
                    if(u==1):
                        print("""
                             list of employees :
                             1. dev1""")
                        mgr2=manager()
                        while(True):
                            b=int(input("""To add list of Developers under manager,
                                       1. dev1
                                       0. exit
                                       Enter the number :"""))
                            if(b==1):
                                emp=dev1
                            elif(b==0):
                                break
                            else:
                                print("No such employee listed")
                            mgr2.employees.append(emp) 

                            
                    elif(u==2):
                        print("""
                             list of employees :
                             1. dev1
                             2. dev2
                             """)
                        mgr2=manager()
                        while(True):
                            b=int(input("""To add list of Developers under manager,
                                       1. dev1
                                       2. dev2
                                       0. exit
                                       Enter the number :"""))
                            if(b==1):
                                emp=dev1
                            elif(b==2):
                                emp=dev2
                            elif(b==0):
                                break
                            else:
                                print("No such employee listed")
                            mgr2.employees.append(emp) 

                    elif(u==3):
                        print("""
                             list of employees :
                             1. dev1
                             2. dev2
                             3. dev3
                             """)
                        mgr2=manager()
                        while(True):
                            b=int(input("""To add list of Developers under manager,
                                       1. dev1
                                       2. dev2
                                       3. dev3
                                       0. exit
                                       Enter the number :"""))
                            if(b==1):
                                emp=dev1
                            elif(b==2):
                                emp=dev2
                            elif(b==3):
                                emp=dev3
                            elif(b==0):
                                break                            
                            else:
                                print("No such employee listed")
                            mgr2.employees.append(emp) 
                                        
            elif(z==2):
                m=int(input("""
                               To add employees press '1'
                               To add Developer press '2'
                               To remove employees press '3'
                               To remove developer press '4':"""))
                if(m==1):
                      a=input("Enter number of employee to add :")
                      if(a=="1"):
                          mgr1.addemp(emp1)
                      elif(a=="2"):
                          mgr1.addemp(emp2)
                      elif(a=="3"):
                          mgr1.addemp(emp3)
                
                elif(m==2):
                      a=input("Enter number of developer to add :")
                      if(a=="1"):
                          mgr2.addemp(dev1)
                      elif(a=="2"):
                          mgr2.addemp(dev2)
                      elif(a=="3"):
                          mgr2.addemp(dev3)

                elif(m==3):
                      a=input("Enter number of employee to remove :")
                      if(a=="1"):
                          mgr1.removeemp(emp1)
                      elif(a=="2"):
                          mgr1.removeemp(emp2)
                      elif(a=="3"):
                          mgr1.removeemp(emp3)
                          
                elif(m==4):
                      a=input("Enter number of developer to remove :")
                      if(a=="1"):
                          mgr2.removeemp(dev1)
                      elif(a=="2"):
                          mgr2.removeemp(dev2)
                      elif(a=="3"):
                          mgr2.removeemp(dev3)
                else:
                    print("Bad request, please choose valid option")

            elif(z==3):
                a=input("""
                           1. Manager of Employees
                           2. Manager of developers""")
                if(a=="1"):
                    mgr1.printemp()
                elif(a=="2"):
                    mgr2.printemp()       
