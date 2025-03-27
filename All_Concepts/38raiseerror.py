try:
    a = int(input("Enter a number between 5 to 9: "))
    if a < 5 or a > 9:
        raise ValueError("Number should be between 5 to 9")
except ValueError as e:
    print("Something went wrong:", e)


# try:
#     print(10 / 0)
# except Exception as e:  # 'e' stores the error message
#     print("Something went wrong:", e)
