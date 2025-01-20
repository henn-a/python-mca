# Function to add total marks and grade to the student dictionary
def add_total_marks_and_grade(student, total_marks):
    student["total_marks"] = total_marks
    
    # Determine grade based on total marks
    if total_marks >= 90:
        student["grade"] = "A"
    elif total_marks >= 82:
        student["grade"] = "B"
    elif total_marks >= 75:
        student["grade"] = "C"
    elif total_marks >= 60:
        student["grade"] = "D"
    elif total_marks >= 50:
        student["grade"] = "P"
    else:
        student["grade"] = "F"

# Main function to get input from the user and process the details
def main():
    # Taking input for student details
    name = input("Enter the student's name: ")
    roll_number = input("Enter the student's roll number: ")
    register_number = input("Enter the student's register number: ")
    department = input("Enter the student's department: ")
    semester = int(input("Enter the student's semester: "))
    
    # Creating the student dictionary with the input values
    student = {
        "name": name,
        "roll_number": roll_number,
        "register_number": register_number,
        "department": department,
        "semester": semester
    }
    
    # Taking input for total marks and adding grade
    total_marks = int(input("Enter the total marks: "))
    add_total_marks_and_grade(student, total_marks)

    # Deleting roll number from the student dictionary
    del student["roll_number"]

    # Print the updated student details
    print("\nUpdated Student Details:")
    for key, value in student.items():
        print(f"{key}: {value}")

# Call the main function to run the program
main()
