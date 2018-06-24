import win32com.client as win32
import cgi
import cgitb

cgitb.enable()


def endRange(WordDoc):
    DocAllRange = WordDoc.Range()
    return WordDoc.Range(DocAllRange.End - 1, DocAllRange.End)


def tableIndex(WordDoc):
    return WordDoc.Tables.Count


def insertNewPage(WordDoc):
    eR = endRange(WordDoc)
    eR.InsertBreak(7)


print('''
<html>
<head><meta charset="gbk">
<title>InsertTitle</title></head>
<body>
<form action="InsertNewPage.py">
在文档末尾插入分页符：<br>
<input type="submit" name="InsertNewPageButton" value="插入分页符"><br>

''')
try:
    f = cgi.FieldStorage()
    T = f.getvalue('InsertNewPageButton', '0')
    if len(T) > 1:
        WordApp = win32.Dispatch('Word.Application')
        if WordApp.Documents.Count > 0:
            WordDoc = WordApp.ActiveDocument
            insertNewPage(WordDoc)
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
