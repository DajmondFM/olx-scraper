# from openpyxl import Workbook
# import csv


# wb = Workbook()
# ws = wb.active
# with open('ogloszenia.csv', 'r') as f:
#     for row in csv.reader(f):
#         ws.append(row)
# wb.save('name.xlsx')

from openpyxl import Workbook
import csv


wb = Workbook()
ws = wb.active
with open('./csv/ogloszenia.csv', 'r', encoding='utf-8') as f:
    for row in csv.reader(f):
        ws.append(row)
wb.save('ogloszenia.xlsx')