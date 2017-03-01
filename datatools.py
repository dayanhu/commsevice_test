#coding:utf-8
import xlrd,xlwt,os
"""
创建数据工具类
"""
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        #get titles
        self.row = self.table.row_values(0)

        #get rows number
        self.rowNum = self.table.nrows

        #get columns number
        self.colNum = self.table.ncols

        #the current column
        self.curRowNo = 1

    # def write(self,mlist):
    #     num = len(mlist)
    #     for x in range(num):
    #         print('1')
    #         self.table.put_cell(1,x,1,list[x],0)


    def next(self):
        r = []
        while self.hasNext():

            s = []
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                if str(col[x])[-2:]=='.0':
                    col[x] = str(col[x])[0:-2]
                    #col[x] = float(col[x])
                s.append(col[x])
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :
            return False
        else:
            return True

class ExcelWrite(object):
    def __init__(self, excelPath, sheetName):
        self.file = xlwt.Workbook()
        self.table = self.file.add_sheet(sheetName)

        self.excelPath = excelPath


    def write(self,mlist):
        num = len(mlist)
        for x in range(num):
            mlist[x] = str(mlist[x])
            self.table.write(x,0,mlist[x])
        self.file.save(self.excelPath)
if __name__ == '__main__':

    a = ExcelWrite(r'c/4.xls','1')
    mlist = []
    for img in os.listdir(r'c/compareImg'):
        mlist.append(img)

    a.write(mlist)

#测试用例工具类


