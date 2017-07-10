import xlwt
from xlrd import open_workbook
from xlutils.copy import copy


def Results(Row,TestCaseID,Status):
    if Row==1:
        Colum=0
        wb = xlwt.Workbook()
        ws =wb.add_sheet("ContentApprovalResults")
        ws.write(0,0,'TestCaseID')
        ws.write(0,1,'Status')
        ws.write(Row,Colum,TestCaseID)
        Colum+=1
        ws.write(Row,Colum,Status)
        wb.save("C:/Users/ckumar/Desktop/Test1_Suit/Results/ContentApprovalResults.csv")
        print "done"
        
    if Row!=1:
        Colum=0
        rb = open_workbook("C:/Users/ckumar/Desktop/Test1_Suit/Results/ContentApprovalResults.csv")
        wb = copy(rb)
        s = wb.get_sheet(0)
        s.write(Row,Colum,TestCaseID)
        Colum+=1
        s.write(Row,Colum,Status)
        wb.save('C:/Users/ckumar/Desktop/Test1_Suit/Results/ContentApprovalResults.csv')






