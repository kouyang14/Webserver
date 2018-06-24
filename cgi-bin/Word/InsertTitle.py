import win32com.client as win32
import cgi
import cgitb


cgitb.enable()


def endRange(WordDoc):
    DocAllRange = WordDoc.Range()
    return WordDoc.Range(DocAllRange.End - 1, DocAllRange.End)


def tableIndex(WordDoc):
    return WordDoc.Tables.Count


def insertTitle(WordDoc):
    eR = endRange(WordDoc)
    eR.InsertAfter("原始记录\n")

    eR = endRange(WordDoc)
    eR.InsertAfter("第   页  共   页\n")

    eR = endRange(WordDoc)
    eR.InsertAfter("设备编号：\n")

    eR = endRange(WordDoc)
    WordDoc.Tables.Add(eR, 1, 5)

    tI = tableIndex(WordDoc)
    WordDoc.Tables(tI).Rows(1).Cells(1).Range.Text = "序号"
    WordDoc.Tables(tI).Rows(1).Cells(2).Range.Text = "项目"
    WordDoc.Tables(tI).Rows(1).Cells(3).Range.Text = "技术要求"
    WordDoc.Tables(tI).Rows(1).Cells(4).Range.Text = "测试结果"
    WordDoc.Tables(tI).Rows(1).Cells(5).Range.Text = "备注"
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
<form action="InsertTitle.py">
在页首插入顶部内容：<br>
<input type="submit" name="InsertTitleButton" value="插入顶部内容"><br>

''')
try:
    f = cgi.FieldStorage()
    T = f.getvalue('InsertTitleButton', '0')
    if len(T) > 1:
        WordApp = win32.Dispatch('Word.Application')
        if WordApp.Documents.Count > 0:
            WordDoc = WordApp.ActiveDocument
            insertTitle(WordDoc)
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
