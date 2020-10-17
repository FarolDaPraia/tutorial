from openpyxl import load_workbook


class Data:
    def __init__(self, order_data, region, rep, item, units, unit_cost, total):
        self.orderData = order_data
        self.region = region
        self.rep = rep
        self.item = item
        self.units = units
        self.unitsCost = unit_cost
        self.total = total

    def __repr__(self):
        return f'{self.__dict__}'


class Sample:
    def __init__(self, file_name, sheet_name='Sheet1'):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.datas = []
        self.read_xls()

    def __repr__(self):
        return f'File name:{self.file_name}, with a list of {len(self.datas)} datas'

    def read_xls(self):
        ws = load_workbook(self.file_name)[self.sheet_name]
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
            column_value = []
            for cell in row:
                column_value.append(cell.value)
            self.datas.append(
                (
                    Data(
                        column_value[0],
                        column_value[1],
                        column_value[2],
                        column_value[3],
                        column_value[4],
                        column_value[5],
                        column_value[6],
                    )
                )
            )


teste = Sample('SampleData.xlsx', 'SalesOrders')
