# import pandas as pd

# # Load the Excel file
# file_path = 'C:/Users/Ratul/Downloads/BQR_Name_Bangla1.xlsx'
# df = pd.read_excel(file_path)

# # Check the first few rows to understand the structure
# print(df.head())

# # Assuming the columns are 'MSISDN' and 'CommonBusinessName'
# # Create the SQL UPDATE statements
# update_statements = []

# for _, row in df.iterrows():
#     msisdn = row['MSISDN']
#     business_name = row['CommonBusinessName'].replace("'", "''")  # Escape single quotes
#     update_statement = f"""
#     UPDATE [dbo].[SW_TBL_PROFILE_MERCHANT]
#     SET [CommonBusinessName] = '{business_name}'
#     WHERE [MSISDN] = '{msisdn}';
#     """
#     update_statements.append(update_statement.strip())

# # Combine all statements into one string with line breaks
# sql_script = "\n".join(update_statements)

# # Print or save the SQL script to a file
# print(sql_script)

# # Save the script to a file with utf-8 encoding
# with open('bqr-bqr.sql', 'w', encoding='utf-8') as file:
#     file.write(sql_script)






# import pandas as pd

# # Load the Excel file
# file_path = 'C:/Users/Ratul/Downloads/BQR_Name_Bangla_.xlsx'
# df = pd.read_excel(file_path)

# # Print column names to check for any discrepancies
# print(df.columns)

# # Assuming the columns have extra spaces or different names, you can clean or directly use the correct names
# df.columns = df.columns.str.strip()  # Remove any leading or trailing spaces

# # Check the first few rows again
# print(df.head())

# # Use the correct column names
# update_statements = []

# for _, row in df.iterrows():
#     Merchant_Number = row['Merchant_Number']  # Use the actual column name from df.columns
#     English_Business_Name = row['English_Business_Name'].replace("'", "''")  # Use actual column name
#     update_statement = f"""
#     UPDATE [dbo].[SW_TBL_PROFILE_MERCHANT]
#     SET [CommonBusinessName] = '{English_Business_Name}'
#     WHERE [MSISDN] = '{Merchant_Number}';
#     """
#     update_statements.append(update_statement.strip())

# # Combine all statements into one string with line breaks
# sql_script = "\n".join(update_statements)

# # Print or save the SQL script to a file
# print(sql_script)

# # Save the script to a file with utf-8 encoding
# with open('bqr-xd.sql', 'w', encoding='utf-8') as file:
#     file.write(sql_script)


import pandas as pd

# Load the Excel file
file_path = 'C:/Users/Ratul/Downloads/BQR_Name_Bangla_.xlsx'
df = pd.read_excel(file_path)

# Clean column names by removing leading/trailing spaces
df.columns = df.columns.str.strip()

# Print column names to verify they are correct
print("Columns in the Excel file:", df.columns)

# Display the first few rows to verify the data structure
print(df.head())

# Create a list to store the SQL update statements
update_statements = []

# Iterate over each row in the DataFrame and build the SQL statement
for _, row in df.iterrows():
    merchant_number = str(row['Merchant_Number']).strip()  # Ensure it's treated as a string
    english_name = str(row['EnglishBusinessName']).replace("'", "''")  # Handle single quotes in names

    # Generate the SQL update statement
    update_statement = f"""
    UPDATE [dbo].[SW_TBL_PROFILE_MERCHANT]
    SET [CommonBusinessName] = '{english_name}'
    WHERE [MSISDN] = '{merchant_number}';
    """
    update_statements.append(update_statement.strip())

# Combine all update statements into a single SQL script
sql_script = "\n".join(update_statements)

# Display the generated SQL script (optional)
print(sql_script)

# Save the SQL script to a file with UTF-8 encoding
output_file = 'bqr-xd.sql'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(sql_script)

print(f"SQL script saved to {output_file}")
