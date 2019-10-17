import xlrd

from page_object_patern.utils.search_dataA import SearchData


class ExcelReader:

    @staticmethod   #nie wymaga tworzenia obiektu danej klasy zeby ja wywołac (self)
    def get_data():
        wb = xlrd.open_workbook("../utils/Dane.xlsx")
        sheet = wb.sheet_by_index(0)
        data = []
        for i in range(1, sheet.nrows):
            search_data = SearchData(sheet.cell(i,0).value, sheet.cell(i,1).value)
            data.append(search_data)
        return data
