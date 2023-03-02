import pyodbc 

# Replace the connection details with your own
server = 'testserver.domainname.com'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Connect to the SQL database
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Execute a sample query
cursor.execute('SELECT * FROM your_table_name')

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)
    
# Close the cursor and connection
cursor.close()
connection.close()
