# School Supply Order Tracking – Logic Challenge

## Objective
# Students will apply their understanding of lists, nested lists, slicing, sorting, list grouping, and logical decision-making to solve a real-world data organization problem without using code.

# ---

# ## Scenario
# You are helping the main office organize student supply requests for the week. Each request includes:

# - Student name  
# - Item requested  
# - Quantity requested  

names = ["Allyson", "Alayna", "Aby", "Sophia"]
items = ["cookies", "apples", "folders", "paint brushes"]
quantity = [2, 4, 1, 6]

# All requests must be stored together in one organized system.

lists = [names, items, quantity]

# ---

# ## Student Tasks (No Coding – Logic Only)

# ### 1. Create Student Requests
# Create a collection that stores information for **3 different student requests**.  
# Each student request must include:
# - Student name  
# - Item requested  
# - Quantity requested  

# ---

# ### 2. Identify Key Information
# From your collection:
# - Identify the **first student’s name**
print(lists[0][0])
# - Identify the **last student’s requested item only**
print(lists[1][3])
# ---

# ### 3. Quantity Extraction
# Create a **separate list that contains only the quantities requested** by the students.
quantity_dos = [2, 4, 1, 6]

# ---

# ### 4. Order Size Analysis
# Analyze the quantities:
# - If **any quantity is greater than 5**, label the order:
#   “Large order detected!”
# - Otherwise label the order:
#   “Orders within normal limits.”

if quantity >=6:
    print("Large order detected")
else:
    print("Order within range")

# ---

# ### 5. Quantity Organization
# Re-organize the quantity list from **smallest to largest** and display the final result.
quantity.sort()
print(quantity)

# ---

# ## Challenge Extension: Classroom Storage Grid

# You are also given a grid showing classroom supply counts:

# Classroom 1: 8, 12, 5  
# Classroom 2: 7, 3, 9  
# Classroom 3: 10, 6, 4  

# Answer the following:

# 1. What is the **middle number** in the second classroom’s list?
# 2. Create a new list that extracts **only the last number** from each classroom.
# 3. Explain **why this information must be stored as a nested structure instead of a single list.**

# ---

# ## What This Assignment Tests
# - Understanding how grouped data is stored
# - Nested structure reasoning
# - Data extraction using position
# - Organizational logic
# - Real-world decision-making with quantities

# ---

# ## Submission Requirements
# - All answers must be written in words and/or tables.
# - No programming code may be used.
# - Show clear reasoning for each response.

# ---

# ## Academic Integrity
# This is an individual logic and reasoning task. All work must be your own.

# ---

# Instructor: Marvin Evins  
# Course:  AP Computer Science Principles  
