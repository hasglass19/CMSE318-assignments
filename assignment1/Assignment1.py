# CMPE 318 Assignment 1 - Updated Version

class Student:
    def __init__(self, student_number, first_name, last_name, age, sex, major, nationality):
        self.__student_number = student_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__sex = sex
        self.__major = major
        self.__nationality = nationality

    # Getters
    def get_student_number(self):
        return self.__student_number

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def get_sex(self):
        return self.__sex

    def get_major(self):
        return self.__major

    def get_nationality(self):
        return self.__nationality

    # Setters
    def set_student_number(self, value):
        self.__student_number = value

    def set_first_name(self, value):
        self.__first_name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_age(self, value):
        self.__age = value

    def set_sex(self, value):
        self.__sex = value

    def set_major(self, value):
        self.__major = value

    def set_nationality(self, value):
        self.__nationality = value

    def __str__(self):
        return (f"ID: {self.__student_number}, "
                f"Name: {self.__first_name} {self.__last_name}, "
                f"Age: {self.__age}, Sex: {self.__sex}, "
                f"Major: {self.__major}, Nationality: {self.__nationality}")


# Max 100 students
MAX_STUDENTS = 100
students = [Student(71165946,"Daniel","Mutua",22,"M","Computer Engineering","Kenya"),
            Student(31908446,"Binwell","Kapila",21,"M","Artificial Intelligence Engineering","Zambia"),
            Student(88228872,"Nour","Azza",19,"F","Software Engineering","Syria"),
            Student(59094225,"Halima","Tanko",23,"F","Computer Intelligence Engineering","Nigeria"),
            Student(45719442,"Syergyei","Khakimov",25,"M","Software Engineering","Uzbekistan"),
            Student(87153631,"Kadir","Sert",25,"M","Artificial Engineering","Turkey"),
            Student(27349117,"Chol","Puk",23,"M","Software Engineering","South Sudan"),
            Student(36984691,"Meryem","Nacar",27,"F","Artificial Engineering","Cyprus"),
            Student(16773424,"Mamo","Ayalew",28,"M","Computer Engineering","Ethiopia"),
            Student(27471753,"Nadia","Babiker",21,"F","Software Engineering","Sudan")]


# Find student
def find_student(first_name, last_name):
    for s in students:
        if (s.get_first_name().lower() == first_name.lower() and
                s.get_last_name().lower() == last_name.lower()):
            return s
    return None


# Add student
def add_student():
    if len(students) >= MAX_STUDENTS:
        print("Array full.")
        return

    student_number = input("Enter student number: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    if find_student(first_name, last_name):
        print("Student already exists.")
        return

    try:
        age = int(input("Enter age: "))
        if age<0:
            raise ValueError
    except:
        print("Invalid age.")
        return

    sex = input("Enter sex: ")
    major = input("Enter major: ")
    nationality = input("Enter nationality: ")

    students.append(Student(student_number, first_name, last_name, age, sex, major, nationality))
    print("Student added.")


# Show one student
def show_student():
    first = input("First name: ")
    last = input("Last name: ")

    s = find_student(first, last)
    if s:
        print(s)
    else:
        print("Not found.")


# Show all
def show_all():
    if not students:
        print("No students.")
        return

    for s in students:
        print(s)


# Age range
def show_age_range():
    try:
        min_age = int(input("Min age: "))
        max_age = int(input("Max age: "))
        if min_age<0 or max_age<0:
            raise ValueError
    except:
        print("Invalid input.")
        return

    found = False
    for s in students:
        if min_age <= s.get_age() <= max_age:
            print(s)
            found = True

    if not found:
        print("No students in range.")


# Modify
def modify_student():
    first = input("First name: ")
    last = input("Last name: ")

    s = find_student(first, last)
    if not s:
        print("Not found.")
        return

    print("1.ID 2.First 3.Last 4.Age 5.Sex 6.Major 7.Nationality")
    choice = input("Choice: ")

    if choice == "1":
        s.set_student_number(input("New ID: "))
    elif choice == "2":
        s.set_first_name(input("New first name: "))
    elif choice == "3":
        s.set_last_name(input("New last name: "))
    elif choice == "4":
        try:
            age=int(input("New age: "))
            if age<0:
                raise ValueError
            s.set_age(age)
        except:
            print("Invalid.")
    elif choice == "5":
        s.set_sex(input("New sex: "))
    elif choice == "6":
        s.set_major(input("New major: "))
    elif choice == "7":
        s.set_nationality(input("New nationality: "))
    else:
        print("Invalid choice.")


# Delete
def delete_student():
    first = input("First name: ")
    last = input("Last name: ")

    s = find_student(first, last)
    if s:
        students.remove(s)
        print("Deleted.")
    else:
        print("Not found.")


# Write file
def write_file():
    filename = input("Filename: ")

    with open(filename, "w") as f:
        for s in students:
            f.write(f"{s.get_student_number()},{s.get_first_name()},{s.get_last_name()},"
                    f"{s.get_age()},{s.get_sex()},{s.get_major()},{s.get_nationality()}\n")

    print("Saved.")


# Read file
def read_file():
    filename = input("Filename: ")

    try:
        with open(filename, "r") as f:
            students.clear()
            for line in f:
                data = line.strip().split(",")
                if len(data) == 7:
                    students.append(Student(data[0], data[1], data[2],
                                            int(data[3]), data[4], data[5], data[6]))
        print("Loaded.")
    except:
        print("Error reading file.")


# Bonus search
def search_any():
    keyword = input("Enter keyword: ").lower()

    found = False
    for s in students:
        if (keyword in s.get_first_name().lower() or
            keyword in s.get_last_name().lower() or
            keyword in s.get_major().lower() or
            keyword in s.get_nationality().lower() or
            keyword==s.get_age().__str__() or
            keyword==s.get_student_number().__str__()):
            print(s)
            found = True

    if not found:
        print("No matches.")


def menu():
    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add a new student")
        print("2. Find a student by first name and last name")
        print("3. Show all students")
        print("4. Show all students within an age range")
        print("5. Modify a student record")
        print("6. Delete a student")
        print("7. Write student data to a file")
        print("8. Read student data from a file")
        print("9. Find students by any criterion (Bonus)")
        print("10. Quit")
        print("===============================================")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_student()
        elif choice == "3":
            show_all()
        elif choice == "4":
            show_age_range()
        elif choice == "5":
            modify_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            write_file()
        elif choice == "8":
            read_file()
        elif choice == "9":
            search_any()
        elif choice == "10":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")


menu()