import openpyxl as xl

def read_excel(excel_path = "data/test.xlsx"):
    # baz kardan file excel
    # va entekhan safhe faal
    wb = xl.load_workbook(excel_path)
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
    return user_email


if __name__ == "__main__":
    for a,b in read_excel().items():
        print(f'{a}:{b}')


