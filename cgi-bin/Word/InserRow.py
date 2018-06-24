import win32com.client as win32
import cgi
import cgitb

cgitb.enable()


def tableIndex(WordDoc):
    return WordDoc.Tables.Count


def insertRow(WordDoc):
    tI = tableIndex(WordDoc)
    x = WordDoc.Tables(tI).Rows.Count
    print(str(x))
    sn = 1
    try:
        print(WordDoc.Tables(tI).Rows(x).Cells(1).Range.Text)
        sn = int(WordDoc.Tables(tI).Rows(x).Cells(1).Range.Text) + 1
    except Exception as e:
    	print(WordDoc.Tables(tI).Rows(x).Cells(3).Range.Text)
        sn = 999

    WordDoc.Tables(tI).Rows.Add()
    WordDoc.Tables(tI).Rows(x + 1).Cells(1).Range.Text = str(sn)
    WordDoc.Tables(tI).Rows(x + 1).Cells(2).Range.Text = ""
    WordDoc.Tables(tI).Rows(x + 1).Cells(3).Range.Text = "≥66dB"
    WordDoc.Tables(tI).Rows(x + 1).Cells(4).Range.Text = "68.4dB"
    WordDoc.Tables(tI).Rows(x + 1).Cells(5).Range.Text = "WordDoc.Tables(tI).Rows(x).Cells(1).Range.Text"
    WordDoc.Tables(tI).Borders.Enable
    WordDoc.Tables(tI).Borders.InsideLineStyle = 1
    WordDoc.Tables(tI).Borders.OutsideLineStyle = 1
    WordDoc.Tables(tI).Borders.InsideLineWidth = 4
    WordDoc.Tables(tI).Borders.OutsideLineWidth = 12
    WordDoc.Tables(tI).Rows(1).Borders.OutsideLineWidth = 12


print('''
<html>
<head><meta charset="gbk">
<title>InsertTitle</title></head>
<body>
<form action="InsertRow.py">
在最后一个表格增加新行：<br>
<input type="submit" name="InsertRowButton" value="插入新行"><br>

''')
try:
    f = cgi.FieldStorage()
    T = f.getvalue('InsertRowButton', '0')
    if len(T) > 1:
        WordApp = win32.Dispatch('Word.Application')
        if WordApp.Documents.Count > 0:
            WordDoc = WordApp.ActiveDocument
            insertRow(WordDoc)
            print("完成！")
        else:
            print("Word未打开！")

except Exception as e:
    print("发生异常：<br>" + repr(e))

print('''
</form>
</body>
</html>	
	''')