import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    username='root',
    password='983920Abdul#',
    database='zpizza'
)

my_cursor = conn.cursor()

# Execute a SELECT query to fetch the table data
my_cursor.execute("SELECT * FROM pizza")  # Replace 'your_table_name' with your actual table name

# Fetch all the rows from the result set
rows = my_cursor.fetchall()

# Close the cursor and connection
my_cursor.close()
conn.close()

# Generate the HTML table rows dynamically using the fetched data
table_rows = ""
for row in rows:
    table_rows += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"

# Replace the placeholder table rows in the HTML code with the generated table rows
html_code = """
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    /* CSS styles omitted for brevity */
  </style>
</head>
<body>
  <!-- Existing HTML code -->
  <div class="section">
    <h2 class="section-heading">Swiggy</h2>
    <!-- Existing HTML code -->
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Restaurant</th>
            <th>Rating</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          <!-- Dynamically generated table rows -->
          {table_rows}
        </tbody>
      </table>
    </div>
  </div>
  <!-- Existing HTML code -->
</body>
</html>
""".format(table_rows=table_rows)

# Save the modified HTML code to a file
file_path = r"C:\Users\Abdul\output.html"  # Update the file path to the desired directory
with open(file_path, "w") as file:
    file.write(html_code)

print("HTML file generated successfully.")
