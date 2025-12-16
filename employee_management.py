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
            emp_id=input("enter the empolyee id: ")
            name=input( "\n enter the empolyee name:  ")
            age=input( "\n enter the empolyee age:  ")
            salary=input( "\n enter the empolyee salary: ")
            department=input( "\n enter the empolyee department: ")
            add_empolyee(emp_id,name,age,salary,department)

        elif choice == '2':
            view_employee()

        elif choice == '3':
            pass

        elif choice == '4':
            pass

        elif choice == '5':
            pass

        elif choice == '6':
            pass

        elif choice == '7':
            pass

if __name__ == "__main__":
    menu()