import xlsxwriter

def wexcel(exname,sheetname,tabname,all_data):
    with xlsxwriter.Workbook(exname) as workbook:
        worksheet = workbook.add_worksheet(sheetname)
        worksheet.set_column(0, 1, 30)
        worksheet.set_column(1, 2, 30)
        worksheet.set_column(2, 3, 30)
        worksheet.set_column(3, 4, 30)
        worksheet.set_column(4, 5, 30)
        worksheet.set_column(5, 6, 25)
        worksheet.set_column(6, 7, 30)
        worksheet.set_column(7, 8, 30)
        worksheet.set_column(8, 9, 30)
        worksheet.set_column(9, 10, 15)
        worksheet.set_column(10, 11, 30)
        worksheet.set_column(11, 12, 30)
        worksheet.set_column(12, 13, 30)
        worksheet.autofilter('A1:M13')
        ItemStyle = workbook.add_format({
            'align': 'center',
            'top': 1,
            'left': 1,
            'right': 1,
            'bottom': 1,
            "text_wrap":1
        })

        worksheet.write_row("A1",tabname,ItemStyle)
        num = 1
        for i in all_data:
            num += 1
            row_num = "A"+str(num)
            worksheet.write_row(row_num,i,ItemStyle)
