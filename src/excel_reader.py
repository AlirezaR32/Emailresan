import openpyxl as xl

# baz kardan file excel
# va entekhan safhe faal
wb = xl.load_workbook('data/Devops.xlsx')
ws = wb.active

# for x in ws['c']: print(x.value) 

# ertefa jadval
h = len(ws["a"])

# sakht dictinary khali va ezafeh kardan etelat
user_email = {}
for i in range(2,h+1):
    name = ws[f"a{i}"].value
    email = ws[f"b{i}"].value

    user_email[name] = email




