import cgitb
import win32com.client as win32
cgitb.enable()
gg=win32.gencache.EnsureDispatch('Runtime.InteropServices.Marshal.GetActiveObject("Word.Application")')
myw=gg("Word.Application")
myw.Visible=1
d=myw.Documents.Add()