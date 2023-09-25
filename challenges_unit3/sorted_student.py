class student:
  def __init__(self,name,roll_number,cgpa):
     self.name=name
     self.roll_number=roll.number
     self.cgpa=cgpa
  def sort_students(student_list):
     sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=true)
     return sorted_students
students=[student("Hari","A123",7.8),student("Srikanth","A124",9.8),student("Sowmiya","A125",8.9),student("Mahidhar","A126",9.2)]
sorted_students=sortred_students(students)
for student in sorted_students:
    print("Name:{},Rollnumber:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))
