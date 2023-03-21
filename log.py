#log.py file
import time
# Define timestamp
def timestamp(func):
    # Define a nested function to print ctime
    def printDate():
        print(time.ctime())
        # Call func()
        func()
    # Return nested function        
    return printDate





#test.py file
# import timestamp from log file
from log import timestamp
# Use decorator on function hi()
@timestamp
def hi():
    print("hi")

# Define main function
def main():    
    # Call hi function
    hi()

# Call main function
main()

