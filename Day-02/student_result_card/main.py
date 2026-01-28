student_name = input("Enter name of student: ")
sub1_marks = input("Enter the marks of Subject 1: ")
sub2_marks = input("Enter the marks of Subject 2: ")
sub3_marks = input("Enter the marks of Subject 3: ")

sub1_marks = int(sub1_marks)
sub2_marks = int(sub2_marks)
sub3_marks = int(sub3_marks)

total_marks = sub1_marks+sub2_marks+sub3_marks

print(f"Name: {student_name}")
print(f"Total Marks: {total_marks}")
