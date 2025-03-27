#Program 53. Program to Remove Items from Set1 That Are Not Common to Both Set1 and Set2

skills1={"aptitude","technical","CGPA"}
skills2={"aptitude","technical","personality"}

# Retain only common elements in test_players
skills1.intersection_update(skills2)
print(skills1)