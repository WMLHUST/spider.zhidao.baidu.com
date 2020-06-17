import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.append([1, 2, 3])
ws['A1'] = 42
wb.save("sample.xlsx")