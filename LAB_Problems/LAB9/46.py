# Program to Check Whether a Given Key Already Exists in a Dictionary
rating={"aptitude":8,"technical":9,"personality":10,"communication_skills":9.5}
skill=input(str("Enter a skill: "))
if skill in rating.keys():
    print("Your key is present and it's value is:", rating[skill])
else:
    print("Your key is not present enter another one")
