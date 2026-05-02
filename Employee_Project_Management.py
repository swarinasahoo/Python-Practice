6# Employee payroll management system 

# employee class is used to calculate the hra, da, bonus, deduction, net 
class Employee:
    # constructor 
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id 
        self.name = name
        self.dept = dept 
        self.salary = salary
        
    # First method  - Calculate salary of an employee
    def calculate_salary(self): 
        hra = 0.2 * self.salary 
        da = 0.1 * self.salary 
        bonus = 0.05 * self.salary 
        deduction = 0.08 * self.salary 
        net = self.salary + hra + da + bonus - deduction 
        return hra, da, bonus, deduction, net 
    
    # Second method - display the employee details
    def display(self): 
        print(f'EMPLOYEE ID : {self.emp_id}')
        print(f'NAME : {self.name}')
        print(f'DEPARTMENT : {self.dept}')
        print(f'SALARY : {self.salary}')
    
    # Third method - display the salary slip
    def salary_slip(self): 
        hra, da, bonus, deduction, net = self.calculate_salary()
        print('*'*50)
        print("SALARY SLIP")
        print('*'*50)
        
        print(f'EMPLOYEE ID : {self.emp_id}')
        print(f'NAME : {self.name}')
        print(f'DEPARTMENT : {self.dept}')
        print(f'BASIC SALARY : {self.salary}')
        print(f'HRA : {hra}')
        print(f'DA : {da}')      
        print(f'BONUS : {bonus}')  
        print(f'DEDUCTION : {deduction}')
        print(f'NET SALARY : {net}')
        
class PayrollSystem:
    # BUG 1 FIX: was __int__ (typo), corrected to __init__
    def __init__(self):
        self.employee_list = [] 
        self.load_file() 
    
    # find employee function 
    def find_employee(self, emp_id): 
        for emp in self.employee_list:
            if emp.emp_id == emp_id:
                return emp 
        return None 
    
    # 1. Add employee 
    def add_employee(self):
        emp_id = input('ENTER EMP ID : ')
        
        if self.find_employee(emp_id): 
            print("Employee already exists !")
            return
        
        name = input("ENTER EMPLOYEE NAME : ")
        dept = input("ENTER DEPARTMENT : ")
        
        try: 
            salary = float(input('ENTER SALARY : '))
        except:
            print('INVALID SALARY INPUT !!!')
            return
        # OBJECT 
        emp = Employee(emp_id, name, dept, salary)
        self.employee_list.append(emp)
        print('EMPLOYEE ADDED SUCESSFULLY !!!')
    
    # 2. method to view the employee
    def view_employees(self):
        if not self.employee_list:
            print('NO RECORDS FOUND')
            return 
        
        print('*'*50)
        print('EMPLOYEE RECORDS')
        print('*'*50)
        
        for emp in self.employee_list:
            emp.display()
            
    # 3. method to search the employee
    def search_employee(self): 
        emp_id = input('ENTER EMPLOYEE ID : ')
        emp = self.find_employee(emp_id)
        
        if emp:
            emp.display() 
        else: 
            print('EMPLOYEE NOT FOUND')
            
    # 4. update employee details 
    def update_employee(self): 
        emp_id = input('ENTER EMPLOYEE ID : ')
        emp = self.find_employee(emp_id)
        
        if not emp:
            print('EMPLOYEE NOT FOUND !!!')
            return 
        
        emp.name = input('ENTER NAME : ')
        emp.dept = input("ENTER DEPARTMENT : ")
        
        try:
            emp.salary = float(input('ENTER NEW SALARY : '))
        except:
            print('INVALID SALARY INPUT !!!')
            
        print('\n SALARY UPDATED SUCESSFULLY !!!')
        
    # 5. delete the employee details 
    def delete_employee(self):
        emp_id = input('ENTER EMPLOYEE ID : ')
        emp = self.find_employee(emp_id)
        
        if emp:
            self.employee_list.remove(emp)
            print('\n EMPLOYEE DELETED SUCESSFULLY !!!')
        else:
            print('\n EMPLOYEE NOT FOUND !!!')
            
    # 6. generate the salary slip 
    def generate_salary_slip(self): 
        emp_id = input('\n ENTER EMPLOYEE ID : ')
        emp = self.find_employee(emp_id)
        
        if emp:
            emp.salary_slip() 
        else:
            print('\n EMPLOYEE NOT FOUND !!!')
            
    # 7. save file
    # BUG 2 FIX: was 'employee.txt', corrected to 'employees.txt' to match load_file
    def save_file(self):
        try:
            with open('employees.txt', 'w') as file:
                for emp in self.employee_list:
                    file.write(f'{emp.emp_id},{emp.name},{emp.dept},{emp.salary}\n')
        except Exception as e:
            print('ERROR SAVING FILE : ', e)
    
    # 8. load file     
    # BUG 3 FIX: strip each field individually to remove stray whitespace
    def load_file(self):
        try:
            with open('employees.txt', 'r') as file: 
                for line in file:
                    parts = line.strip().split(',')
                    emp_id, name, dept, salary = [p.strip() for p in parts]
                    self.employee_list.append(
                        Employee(emp_id, name, dept, float(salary))
                    )
        except FileNotFoundError:
            pass  # No existing file yet, start fresh
        except Exception as e:
            print('ERROR LOADING FILE : ', e)    
            
    # give menu to user    
    def menu(self): 
        while True: 
            print('*'*50)
            print('PAY-ROLL SYSTEM')
            print('*'*50) 
            
            print('1. ADD EMPLOYEE')
            print('2. VIEW EMPLOYEE')
            print('3. SEARCH EMPLOYEE')
            print('4. UPDATE EMPLOYEE')
            print('5. DELETE EMPLOYEE')
            print('6. GENERATE SALARY SLIP')
            print('7. SAVE EMPLOYEE DATA')
            print('8. EXIT APPLICATION')
            
            choice = input('\n ENTER CHOICE :')
            
            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.view_employees() 
            elif choice == '3':
                self.search_employee() 
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.delete_employee() 
            elif choice == '6':
                self.generate_salary_slip() 
            elif choice == '7':
                self.save_file() 
            elif choice == '8':
                self.save_file() 
                print('\n DATA SAVED. EXITING !!!')
                break
            else:
                print('\n PLEASE CHOOSE NUMBER BETWEEN 1 TO 8 !!!')            
                
# Call the functions 
if __name__ == '__main__':
    # object
    system = PayrollSystem() 
    system.menu()
