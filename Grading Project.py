# Create a simple school grading system script. The program should take a student's marks as input and 
# output their grade based on the following scale:

# 90 and above: A+
# 80 to 89: A
# 70 to 79: B+
# 60 to 69: B
# Below 60: Fail


# Define the student's marks (get input from the user)
marks = int(input("Enter your marks: "))


if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B+"
elif marks >= 60:
    grade = "B"
else:
    grade = "Fail"

# Print the result in the specified format
print(f"For marks {marks}, the grade is {grade}.")