# Program to Update the First Set with Items That Don’t Exist in the Second Set
skills1={"aptitude","technical","CGPA"}
skills2={"aptitude","technical","personality"}

#updating the skills which are not in skills1
skills1.difference_update(skills2)
print(skills1)