from os import system as sys
sys("cls")

# try block
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(f"{x}/{y} = {x/y}")

# specific exceptions
except ValueError:
    print("Could not convert to a number.")

except ZeroDivisionError:
    print("Can't divide by zero")

# any other error
except:
    print("Something went very wrong.")

# executed when there is no exception
else:
    print("there are no errors encountered")

# always get executed
# useful for clean-up code that should be run no matter what else happened
# e.g close a file
finally:
    del x, y

# raise own error
raise ValueError("error raised")
