# Import required modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Assign credentials ann path of style sheet
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Google Sheets API Tutorial").sheet1

# display data
data = sheet.get_all_records()
row4 = sheet.row_values(4)
col2 = sheet.col_values(2)
cell = sheet.cell(5, 2).value

print("Column 2 Data : ")
pprint(col2)
print("\nRow 4 Data : ")
pprint(row4)
print("\nCell (5,2) Data : ")
pprint(cell)
print("\nAll Records : ")
pprint(data)

# Inserting data
insertRow = [6, "SOUMON ", "Purple"]
sheet.insert_row(insertRow, 4)
print("\nAll Records after inserting new row : ")
pprint(data)

# Deleting data
sheet.delete_row(7)
print("\nAll Records after deleting row 7 : ")
pprint(data)

# Update a cell
sheet.update_cell(5, 2, "Nitin Das")
print("\nAll Records after updating cell (5,2) : ")
pprint(data)

# Display no. of rows, columns
# and no. of rows having content
numRows = sheet.row_count
numCol = sheet.col_count
print("Number of Rows : ", numRows)
print("Number of Columns : ", numCol)
print("Number of Rows having content : ", len(data))
Insert = [7, "SOUMOUN ", "KAKA"]
sheet.update_cell(6, 2, "Trial")
pprint(data)

