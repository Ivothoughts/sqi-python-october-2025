#1.  Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.
# Handle Multiple Exceptions:



class WhyNegativeError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise WhyNegativeError("Number must be positive")
    else:
        print(f"{number} is positive")

try:
    # check_positive(-100)
    # check_positive("hpdnoa")
    check_positive(0.1)
    check_positive(2)
    check_positive(200)
    check_positive(8.5)
except WhyNegativeError as e:
    print(f"Negative number not allowed: {e}")
except ValueError as exc:
    print(f"Only accepts integers: {exc}")
except TypeError as exc:
    print(f"only integers are allowed: {exc}")



#2.  Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.

def safe_divide(a: int, b: int):
    try:
        result = int(a) / int(b)
        print(f"Result: {result}")
        return result

    except ValueError as exc:
        print(f"only numbers can be divided: {exc}")
    except ZeroDivisionError as exc:
        print(f"cannot divide by: {exc}")
    except TypeError as exc:
        print(f"invalid data type [interger / float only]: {exc}")



safe_divide(100, 0)
safe_divide(100, 2)
safe_divide(0, 0.1)
safe_divide(20.8, 4)
safe_divide(100, "how")
safe_divide("fish", "me")