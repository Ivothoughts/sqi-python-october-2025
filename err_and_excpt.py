
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age < 0:
#             print("age can not be negative")
#             continue
#     except ValueError as exc:
#         print(f"Age can not be a: {exc}")
#         continue
#     else:
#         print(2025 - age)
        

while True:
    try:
        age = int(input("Enter your age: "))
    except ValueError as exc:
        print(f"Age can not be a text: {exc}")
    else:
        if age < 0:
            print("Age can not be negative")
            continue
        print(2025 - age)
        break