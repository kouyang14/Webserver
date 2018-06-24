import win32com.client as win32
import cgitb
import cgi

cgitb.enable()
f = cgi.FieldStorage()
T = f.getvalue('OpenButton', '1')

print('''
<html>
<head><meta charset="gbk">
<title>InsertTitle</title></head>
<body>
<form action="Open.py">
打开文档：<br>
<input type="submit" name="OpenButton" value="打开文档"><br>

''')

try:
    if len(T) > 1:
        WordApp = win32.Dispatch('Word.Application')
        if WordApp.Documents.Count > 0:
            WordDoc = WordApp.ActiveDocument
            print("打开文档：" + WordDoc.Name)
        else:
            WordApp2 = win32.gencache.EnsureDispatch('Word.Application')
            WordApp2.Visible = 1
            WordDoc2 = WordApp2.Documents.Add()
            print("新建文档：" + WordDoc2.Name)
except Exception as e:
    print("发生异常：" + repr(e))
finally:
    pass


print('''
</form>
</body>
</html>	
	''')
