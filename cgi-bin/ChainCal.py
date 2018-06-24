import math
import cgi
import cgitb
import io

cgitb.enable()

try:
    form = cgi.FieldStorage()
    CAL = form.getvalue('CAL', '1')
    swidth = form.getvalue('swidth', '2000')
    ebn0 = form.getvalue('ebn0', '1')

    Fre = form.getvalue('Fre', '1')
    Fre = form.getvalue('Fre', '1')
    Fre = form.getvalue('Fre', '1')
    Fre = form.getvalue('Fre', '1')
    Fre = form.getvalue('Fre', '1')
    Fre = form.getvalue('Fre', '1')
    Fre = form.getvalue('Fre', '1')
    Fre = form.getvalue('Fre', '1')
    Fre = form.getvalue('Fre', '1')

fff = io.open('ChainCal.html')
HtmlStr = fff.read()
print(HtmlStr)
