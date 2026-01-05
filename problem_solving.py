print(" ---------------------------------- Q1 ----------------------------------")
print("""
What is a variable in Python?
Write a simple example where:
    you store a customer name
    you store a total sales amount

Type your answer below (definition + code).
      """)

print("""Ans
        Varaiable is named reference to store data value in memory, 
      it can be accessed/ reused / updated during program execution.""")

cust_name = "Raama"
total_sales = 15000

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q2 ----------------------------------")
print("""
Write a Python program that:
    Takes customer name as input
    Takes daily sales amount as input
    Prints the customer name and sales
Hint: Remember that input() returns string by default.""")

cust_name = input('Enter Customer Name: ')
sales_amount = float(input('Enter sales Amount : '))
print(f'Customer Name: {cust_name} & sales Amount is : {sales_amount}')

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q3 ----------------------------------")
print("""
      Identify the data type of each variable without running code
      a = 10
    b = 10.5
    c = "100"
    d = True
    e = [1, 2, 3]
    f = (1, 2, 3)
    g = {1, 2, 3}
    h = {"id": 101, "name": "Raj"}
      """)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q4 ----------------------------------")
print("""
given the string, Write Python code to:
    Remove extra spaces
    Convert the name to title case
    Print the cleaned name""")

cust_name = '    chethanak          '
clean_name = cust_name.strip().title()
print(clean_name) # title converts only first letter to upper case


#-------------------------------------------------------------------------------
print(" ---------------------------------- Q5 ----------------------------------")
print("""
You receive sales data from a CSV file:
    sales_amount = "25000"
    Convert it into a numeric type
    Add 5000 bonus
Print the final amount
 """)
sales_amount = '25000'
bonus = 5000
final_amount = float(sales_amount) + bonus
print(f"final_amount : {final_amount}")

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q6 ----------------------------------")
print("""
Boolean Values & Comparison Operators (Easy → Medium)
    Check whether total_sales meets or exceeds the target
    Store the result in a variable
Print the result
       """)
total_sales = 42000
target = 40000
result = total_sales >= target
print(result)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q7 ----------------------------------")
print("""
Logical + Membership Operators (Medium):
Given this data:
        
Write code to check:
    Region is allowed AND
    Sales is greater than 20000
Store the result in a variable and print it.
""")
allowed_regions = ["APAC", "EMEA", "NA"]
region = "APAC"
sales = 30000

check = region in allowed_regions and sales > 20000

print(check)


#-------------------------------------------------------------------------------
print(" ---------------------------------- Q8 ----------------------------------")
print("""
if, elif, else (Easy → Medium):
Based on sales value:
    If sales ≥ 50000 → print "High Performer"
    If sales ≥ 30000 and < 50000 → print "Average Performer"
    Else → print "Low Performer"     
""")

sales = 20000
if sales >= 50000:
    print('High Performer')
elif sales >=30000:
    print('Average Performer')
else:
    print('Low Performer')

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q9 ----------------------------------")
print("""
You have daily sales data:
Write a for loop to:
    Print each sales value
    Also print total sales at the end"     
""")
daily_sales = [1000, 2000, 3000, 4000]
total_sales = 0
for d in daily_sales:
    print(d)
    total_sales += d
print(total_sales)


daily_sales = [1000, 2000, 3000, 4000]
total_sales = 0
for d in daily_sales:
    print(d)
total_sales = sum(daily_sales)
print(total_sales)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q10 ----------------------------------")
print("""
Given sales data:
    If sales is -1 → stop processing
    If sales is 0 → skip it
    Otherwise → print the sales value     
""")

sales_data = [12000, 0, 15000, -1, 20000]
for s in sales_data:
    if s == -1:
        break
    if s == 0:
        continue
    else:
        print(s)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q11 ----------------------------------")
print("""
You are validating sales data.:
    Write the code using for_else.
    Loop through sales
    If any negative value is found → print "Invalid data" and stop
    If loop completes without break → print "All data valid"    
""")
sales_data = [10000, -1, 20000]
for s in sales_data:
    if s < 0:
        print("Invalid Data")
        break
else:
    print("All data valid")

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q12 ----------------------------------")
print("""
You have sales data for multiple regions:
    Print each region
    Print each sales value under that region   
""")
region_sales = {
    "APAC": [10000, 20000],
    "EMEA": [15000, 25000]
}

for key, value in region_sales.items():
    for v in value:
        print(f'{key} : {v}')

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q13 ----------------------------------")
print("""
Simulate a retry mechanism:
    Start with attempt = 1
    Retry until attempt <= 3
    Print "Attempt X"
Increment attempt using while loop
""")

attempt = 1
while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q14 ----------------------------------")
print("""
Access the second element
Update the last element to 5000
Print the updated list
""")
sales = [1000, 2000, 3000, 4000]
second_element = sales[1] # Accessed 2nd element
sales[-1] = 5000 # Updated the last element to 5000
print(sales)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q15 ----------------------------------")
print("""
You have a list of SKUs:
    Perform the following:
    Add "A104" at the end
    Remove "A102"
    Update "A103" to "A105"
    Print the final list
""")

skus = ["A101", "A102", "A103"]
skus.append('A104')
skus.remove('A102')
skus[-2] = 'A105'
print(skus)


skus = ["A101", "A102", "A103"]
skus.append('A104')
skus.remove('A102')
skus[skus.index('A103')] = 'A105'  # index number may not be known if data is huge, so use index
print(skus)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q16 ----------------------------------")
print("""
Do the following:
    Sort sales_2023
    Create a copy of sales_2023
    Combine both lists into one
    Print the final list
""")

sales_2023 = [3000, 1000, 2000]
sales_2024 = [4000, 5000]
sales_2023.sort()
sales_2023_copy = sales_2023.copy()
sales_2023_2024 = sales_2023 + sales_2024
print(sales_2023_2024)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q17 ----------------------------------")
print("""
Use zip() to print product with price
Use enumerate() to print index with product name
""")

products = ["Pen", "Notebook", "Marker"]
prices = [10, 50, 30]

for pro, pri in zip(products, prices):
    print(f"{pro} : {pri}")

for pro in enumerate(products):
    print(pro)

for index, pro in enumerate(products):
    print(index, pro)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q18 ----------------------------------")
print("""
Use map() + lambda to add 10% tax
Use filter() to keep sales greater than 2500
Print the results
""")

sales = [1000, 2000, 3000, 4000]
taxed_sales = list(map(lambda x: x + (x * 0.1), sales))
print(taxed_sales)
result = list(filter(lambda x: x > 2500, taxed_sales))
print(result)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q19 ----------------------------------")
print("""
Using list comprehension only, do the following:
Add 10% tax
Keep only values greater than 2500
""")
sales = [1000, 2000, 3000, 5000]
result = [sale + (sale * 0.1)
for sale in sales 
if sale > 2500]
print(result)

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q20 ----------------------------------")
print("""
You receive this record from a database:
    Unpack values into variables
    Print them in readable format
""")

record = ("APAC", "India", 45000)
name, country, price = record
print(f"Name : {name}")
print(f" Country : {country}")
print(" Price : {price}")

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q21 ----------------------------------")
print("""
You have duplicate SKUs coming from two sources:
    Remove duplicates
    Find common SKUs
    Print both results
""")

source1 = ["A101", "A102", "A103"]
source2 = ["A102", "A104", "A103"]

source1 = set(["A101", "A102", "A103"])
source2 = set(["A102", "A104", "A103"])
common_skus = source1.intersection(source2)
print(f"common_skus : {common_skus}")
result_set = source1.union(source2)
print(f"Result after removing duplicates: {result_set}")

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q22 ----------------------------------")
print("""
You have sales data in dictionary form:
    Access sales for "EMEA"
    Update "NA" sales to 48000
    Add new region "LATAM" with sales 30000
    Print the final dictionary
""")

sales_data = {
    "APAC": 50000,
    "EMEA": 40000,
    "NA": 45000
}

print(sales_data.get('EMEA', 'unknown'))
sales_data['NA'] = 48000
sales_data["LATAM"] = 30000
print(sales_data)
for key, value in sales_data.items():
    print(key[1])


#-------------------------------------------------------------------------------
print(" ---------------------------------- Q23 ----------------------------------")

print("""
Explain the difference between:
    is
    in
Give one simple example for each.
      """)


print("""
is (Identity Operator):
    Checks whether both variables point to the same object in memory.
in (Membership Operator):
    Checks whether a value exists inside a collection.

      """)
a = [1,2,3]
b = [1,2,3]
print(a is b)

b = [1, 2, 3]

print(2 in b)      # True
print(5 not in b)  # True

#-------------------------------------------------------------------------------
print(" ---------------------------------- Q24 ----------------------------------")

print("""
You receive raw sales records:
    Ignore records with negative sales
    Calculate total sales per region
    Store result in a dictionary
      """)

records = [
    ("APAC", 10000),
    ("EMEA", 20000),
    ("APAC", 15000),
    ("NA", 30000),
    ("EMEA", -1)
]


result = {}
for region, sales in records:
    if sales < 0:
        continue
    if region in result:
        result[region] += sales
    else:
        result[region] = sales
print(result)


