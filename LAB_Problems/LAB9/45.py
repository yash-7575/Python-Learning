# Program to Concatenate Dictionaries to Create a New One
hard_skills_rating={"aptitude":8,"technical":9}
soft_skills_rating={"personality":10,"communication_skills":9.5}
overall_rating={**hard_skills_rating,**soft_skills_rating}
print(overall_rating)
