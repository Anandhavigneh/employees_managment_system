empolyees={}

#Add empolyee

def add_empolyee(emp_id, name, age, salary, department):
    empolyees[emp_id] = {
        'name': name,
        'age': age,
        'salary': salary,
        'department': department
    }
    print(f"\nEmployee {name} added successfully!")


#view employee

def view_employee():
    if empolyees:
        for emp_id, emp_details in empolyees.items():
            print(emp_id, emp_details)
    else:
        print("No employees added yet!")

#update employee

def update_employee(emp_id,name=None,age=None,salary=None,department=None):
    try:
        if emp_id in empolyees:
            if name:
                empolyees[emp_id]['name'] = name
            if age:
                empolyees[emp_id]['age'] = age
            if salary:
                empolyees[emp_id]['salary'] = salary
            if department:  
                empolyees[emp_id]['department'] = department
            print(f"\nEmployee {emp_id} updated successfully!")

        else:
            print(f"error with id{emp_id} not found")
        
    except KeyError as e:
        print(F'error updating employee details: {e}')  

#delete employee
def remove_employee(emp_id):
    try:
        emp=empolyees.pop(emp_id)
        print(f"\nEmployee {emp['name']} removed successfully!")
        
    except KeyError :
        print(f"error with id{emp_id} not found")

# save to file
def save_to_file(filename):
    try:
        with open(filename,'w') as file:

            for emp_id,deails in empolyees.items():
                
                line=f"{emp_id}:-> {deails['name']},{deails['age']},{deails['salary']},{deails['department']}\n"
                file.write(line)
        print(f"\nEmployee data saved to {filename} successfully!")

    except Exception as e:
        print(f"error saving to file: {e}")






# main menu function

def menu():

    while True:
        

        print(f"\n welcome to the employee management system")

        print(f"\n 1. Add empolyee")
        print(f"\n 2. view empolyee")
        print(f"\n 3. update empolyee")
        print(f"\n 4. Delete empolyee")
        print(f"\n 5. save to file")
        print(f"\n 6. load from file")
        print(f"\n 7. Exit")


        choice=input("enter you choice: ")

        if choice =="1":
            emp_id=input("\n enter the empolyee id: ")
            name=input( "\n enter the empolyee name:  ")
            age=input( "\n enter the empolyee age:  ")
            salary=input( "\n enter the empolyee salary: ")
            department=input( "\n enter the empolyee department: ")
            add_empolyee(emp_id,name,age,salary,department)

        elif choice == '2':
            view_employee()

        elif choice == '3':
            emp_id=input("\n enter the new empolyee id: ")
            name=input( "\n enter the new empolyee name:  ") or None
            age=input( "\n enter the  new empolyee age:  ")  or None
            salary=input( "\n enter the new empolyee salary: ")  or None
            department=input( "\n enter the new empolyee department: ")  or None

            
            update_employee(emp_id,name,age,salary,department)

        elif choice == '4':
            emp_id=input("\n enter the empolyee id to delete: ")

            remove_employee(emp_id)

        elif choice == '5':
            filename= input('\nenter filename to save :')
            save_to_file(filename)

        elif choice == '6':
            pass

        elif choice == '7':
            pass

if __name__ == "__main__":
    menu()