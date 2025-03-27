# Program to Sort (Ascending and Descending) a Dictionary by Value
rating={"aptitude":8,"technical":9,"a":9,"personality":10,"communication_skills":9.5}

as_rating=dict(sorted(rating.items(), key=lambda item:item[1]))
print(as_rating)
dec_rating=dict(sorted(rating.items(), key=lambda item:item[1], reverse=True))
print(dec_rating)


# if we want to sort by keys it will alphabetically if theres str
as_rating=dict(sorted(rating.items(), key=lambda item:item[0]))
print(as_rating)
dec_rating=dict(sorted(rating.items(), key=lambda item:item[0], reverse=True))
print(dec_rating)


# print()
# for i in rating.keys():
#     if rating[i]==9:
#         print(i)
# l1=list(rating.values())
# l1.sort(reverse=True)
# print(l1)
# dic={}
# for i in l1:
#     for j in rating:
#         if rating[j]==i:
#             dic[j]=rating[j]
#             print(j,":",i)

# print(dic)