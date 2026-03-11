# Student Grade Calculator
# Week 2 Python Project

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A", "Excellent work! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better! 💪"
    elif marks >= 60:
        return "D", "You passed! Try to improve next time 📚"
    else:
        return "F", "Don't give up! Practice more and try again 💡"


# Main program
print("📊 Student Grade Calculator\n")

name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("❌ Invalid input! Marks must be between 0 and 100.")
        else:
            break

    except ValueError:
        print("❌ Please enter a valid number!")

# Get grade using function
grade, message = calculate_grade(marks)

# Display result
print("\n📊 RESULT FOR", name.upper())
print("---------------------------")
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)