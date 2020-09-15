# 导包
import openpyxl

# 读取Excel文件到内存中并生成wb对象
wb = openpyxl.load_workbook('File/123.xlsx')

# 获取Excel所有sheet名称
sheetNames = wb.sheetnames
print(sheetNames)

# 根据sheet名称获取sheet对象
sheet = wb['SheetJS']
print(sheet.title)

# 获取当前正在显示的sheet
sheet = wb.active
print(sheet.title)

# 用单元格下标获取a2单元格的值
a2 = sheet['A2']
print(a2.value)
# column列；row行
print(a2.column,a2.row)

# 用cell函数行与列获取单元格d2单元格的值
d2 = sheet.cell(row=2,column=4)
print(d2.value)

# 获取最大行
max_row = sheet.max_row
print(max_row)
# 获取最大列
max_column = sheet.max_column
print(max_column)

# 


