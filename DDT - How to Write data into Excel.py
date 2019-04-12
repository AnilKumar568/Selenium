import openpyxl

# Writing Data into Excel file

path2 = r'C:\Users\Akumar4\Desktop\Test2_Write.xlsx'

workbook2 = openpyxl.load_workbook(path2)
sheet = workbook2.get_sheet_by_name('Sheet1')

for r in range(1, 6):  # 5 rows
    for c in range(1, 4):  # 3 columns
        sheet.cell(row=r, column=c).value = 'Welcome'

workbook2.save(path2)

