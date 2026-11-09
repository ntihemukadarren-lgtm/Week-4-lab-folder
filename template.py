"""
RECORD CHECK  -  my version
===========================

Name  :Ntihemuka Migambi Darren
Lane  :  AI 
Date  :14/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def check_record(label,value, limit):
    """
    Calculates difference between value and limit and percentage of the value to the limit with status
    """
    percentage = (value/limit)*100
    if percentage >= 100:
        status = "over limit"
    elif percentage >= 90:
        status = "Warning"
    else:
        status = "OK"
    return label,status

def print_report(label, value, limit, difference, percent, status):
    """
    Prints label, value, limit, difference, percent, status
    """
    print(f"value = {value}")
    print(f"limit = {limit}")
    print(f"Difference = {difference:+.2f}")
    print(f"Percentage = {percent:.2f}%")
    print(f"status = {status}")
    return label, value, limit, difference, percent, status


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.
   
def load_records(path):
    records = []
    with open(path) as f:
        for line in f:
            label,value,limit = line.strip().split(",")
            records.append({"label" : label,"value" : float(value),"limit" : float(limit)})
    return records
records = load_records("C:/Users/PC/OneDrive/Python MDX/Phython code practice/Practice.txt")
for record in records:
    label, value, limit = record["label"], record["value"], record["limit"],
    record = check_record(label,value,limit)
    print(record)

# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
