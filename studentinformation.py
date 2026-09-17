def student_information():
    print("=== Student Information ===")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course name: ")
    college = input("Enter college name: ")

    print("\n----- STUDENT DETAILS -----")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("College:", college)
    print("---------------------------")


student_information()
