matrix = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# Split the matrix into rows
rows = matrix.split('\n')

# Determine the number of columns based on the length of the first row
num_columns = len(rows[0])

# Create an empty list to store the columns
columns = [''] * num_columns

# Iterate through each row and extract the characters for each column
for row in rows:
    for i in range(num_columns):
        if i < len(row):
            columns[i] += row[i]

# Decrypt the matrix and extract the hidden message
secret_message = ''
for column in columns:
    for char in column:
        if char.isalpha():
            secret_message += char
        else:
            secret_message += ' '

# Print the decrypted message
print(secret_message)
matrix = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

# Split the matrix into rows
rows = matrix.split('\n')

# Determine the number of columns based on the length of the first row
num_columns = len(rows[0])

# Create an empty list to store the columns
columns = [''] * num_columns

# Iterate through each row and extract the characters for each column
for row in rows:
    for i in range(num_columns):
        if i < len(row):
            columns[i] += row[i]

# Decrypt the matrix and extract the hidden message
secret_message = ''
for column in columns:
    for char in column:
        if char.isalpha():
            secret_message += char

# Print the decrypted message
print(secret_message)
