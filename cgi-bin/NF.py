#!C:\Program Files\Python36\python.exe
# -*- coding: UTF-8 -*-

print('Content-type:text/html')
print()

import math
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
Tref = form.getvalue('Tref', '290')
NF = form.getvalue('NF', '1.05')
NT = form.getvalue('NT', '80')
Cala = form.getvalue('button1', '1')
Calb = form.getvalue('button2', '2')

try:
    Tref2 = float(Tref)
except Exception as e:
    Tref2 = 290.0

try:
    NF2 = float(NF)
except Exception as e:
    NF2 = 1.05

try:
    NT2 = float(NT)
except Exception as e:
    NT2 = 80

NT3 = Tref2 * (10 ** (NF2 / 10) - 1)
NT3 = int(NT3)
NF3 = 10 * math.log10(NT2 / Tref2 + 1)
NF3 = round(NF3, 2)

CalResult1 = ''
CalResult2 = ''

if len(Cala) > 1:
    CalResult1 = str(NT3) + "K"
if len(Calb) > 1:
    CalResult2 = str(NF3) + "dB"

print('''<html>
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>噪声系数计算</title></head>

<body background="../img/timg.jpg">
	
	<img src="../img/bn_product.jpg" width="400" alt="">
<br>
<a href="../Index.html">返回首页</a>
<br>
	<form id="NfCal" action="NF.py">
<div align="left">
	<table width="410">
	<tbody>
		<tr>
		<td width="170" align="right">环境温度：</td>
		<td width="70"><input type="text" value={0} id="Tref" name="Tref" size=4></td>
		<td width="20">K</td>
		
		<td width="50" ></td>
		<td width="100" ></td>
		</tr>
		
		<tr>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
		
		<td></td>
		<td></td>
		</tr>
				
		<tr>
		<td align="right">噪声系数：</td>
		<td><input type="text" value="{1}" id="NF" name="NF" size=4></td>
		<td>dB</td>
		
		<td><input type="submit"  name="button1" id="button1" value="计算"></td>
		<td>{3}</td>
		</tr>
		
		<tr>
		<td>&nbsp;</td>
		<td>&nbsp;&nbsp;
			
			</td>
		<td>&nbsp;</td>
		<td></td>
		
		<td></td>
		</tr>
			
		<tr>
		<td align="right">噪声温度：</td>
		<td><input type="text" value="{2}" id="NT" name="NT" size=4></td>
		<td>K</td>
		
		<td><input type="submit"  name="button2" id="button2" value="计算"></td>
		<td>{4}</td>
		</tr>
		</tbody>
		</table></div></form>
<div align="center"><iframe src="../Footer.html" frameborder="0"  scrolling="no"></iframe></div>
</body></html>
'''.format(Tref2, NF2, NT2, CalResult1, CalResult2))
