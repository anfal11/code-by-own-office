# New list of offers with description for Banglalink
offers = [
"১.১৯ টাকা/ মিনিট (১০ সেকেন্ড প্লাস) ৩ দিন",
"১ পয়সা / সেকেন্ড ৩ দিন",
"১ পয়সা/ সেকেন্ড ৫ দিন",
"১.১৯ টাকা/ মিনিট (১০ সেকেন্ড প্লাস) ৩০ দিন",
"১ পয়সা/ সেকেন্ড ৩০দিন",
"১ পয়সা/ সেকেন্ড ৬০দিন",
"১ পয়সা/ সেকেন্ড ৯০ দিন",
"১ পয়সা/ সেকেন্ড ৩৬৫ দিন",
"১.১৯ টাকা/ মিনিট (১০ সেকেন্ড প্লাস) ২ দিন",
"১.১৯ টাকা/ মিনিট (১০ সেকেন্ড প্লাস) ৭ দিন",
"৯৯ পয়সা/মিনিট ৩০ দিন",
"৯৯ পয়সা/মিনিট ৩০ দিন"
]

# Corresponding amounts for each offer in English
amounts = [
34,
44,
64,
124,
144,
204,
304,
904,
26,
56,
106,
114
]

# SQL query template for Banglalink
query_template = "INSERT INTO [dbo].[topupdeals] ([operator], [dealtype], [amount], [description], [is_cash_back], [cash_back]) VALUES ('robi', '4', '{amount}', N'{description}', 'false', '0');"

# Generate the queries
queries = []
for amount, description in zip(amounts, offers):
    query = query_template.format(amount=amount, description=description)
    queries.append(query)

# Write the queries to a file
with open('callrate.sql', 'w', encoding='utf-8') as file:
    for query in queries:
        file.write(query + '\n')

# Print a success message
print("SQL queries generated and saved to 'internet.sql'")
