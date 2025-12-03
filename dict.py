# my_info = {"name": "mr beans", "age": 500, "gender": "Male", "dept": "HR"}
# print(my_info["age"])
# my_info["name"] = "Omole"
# print(my_info)
# del my_info["gender"]
# print(my_info)
# print(12 in my_info.values())
# print("dept" in my_info)
# print(list(my_info))

day = input("Enter any day of the week: ").capitalize()
weekend = ["Saturday", "Sunday"]
weekday = ["Monday", "Tuesday", "Wednessday", "Thursday", "Friday"]
if day in weekend:
    print("Weekend")
else:
    print("Weekday")


