log_file = open("um-server-01.txt") # Opens the .txt file and assigns it to the variable log_file


def sales_reports(log_file): # Creates a function called sales_reports and takes in the parameter log_file
    for line in log_file: # Loops through log_file line by line
        line = line.rstrip() # Removes any white space at the end of each line (on the right)
        day = line[0:3] # Takes the date information at the start of the line from index 0 and stopping at index 3 [0, 1, 2] and assigns it to the 'day' variable as a list
        if day == "Mon": # An if statement checking to see if the string "Tue" is included in 'day' / then changed to Mon for Monday following assessment instructions
            print(line) # If line 8 condition is true, print that line


sales_reports(log_file) # Calls the function sales_reports taking in the argument log_file

def melon_orders(log_file):
    for line in log_file:
        line = line.rstrip()
        line = line.split(" ")
        num_orders = int(line[2])
        if num_orders > 10:
            print(line)

melon_orders(log_file)
