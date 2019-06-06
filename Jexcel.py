import xlwt

class Jexcel:
    
    def __init__(self, encoding = 'utf-8'):
        self.row = 0
        self.excel = xlwt.Workbook(encoding)
        self.sheet = self.excel.add_sheet('xlwt_sheet1',cell_overwrite_ok=True)

    def new_line(self, line = 1):
        self.row = self.row + line

    def write_line(self, *tupleArg):
        i = 0
        for s in tupleArg:
            self.sheet.write(self.row, i, str(s))
            i = i + 1
        self.new_line()
    
    def save(self, filename_or_stream):
        self.excel.save(filename_or_stream)

    
