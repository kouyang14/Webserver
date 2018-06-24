#!C:\Program Files\Python36\python.exe

print('Content-type:text/html')
print()

import math
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
Fre = form.getvalue('Fre', '1')
d = form.getvalue('d', '0.3')
yita = form.getvalue('yita', '50')
button = form.getvalue('button', '1')

try:
    Fre = float(Fre)
except Exception as e:
    Fre = 1

try:
    d = float(d)
except Exception as e:
    d = 0.3

try:
    yita = float(yita)
except Exception as e:
    yita = 50

Gain = ''
WaveWidth = ''
if len(button) > 1:
    gain = 10 * math.log10((Fre / 0.3) ** 2 * d ** 2 * 3.14159265 ** 2 * yita /100)
    gain = round(gain, 2)
    Gain = str(gain) + 'dBi'
    wavewidth = 70 * 0.3 / (Fre * d)
    wavewidth = round(wavewidth, 2)
    WaveWidth = str(wavewidth) + '°'


print('''



<html>
    <head>
    
    <meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>antenna cal</title>
        
    </head>

<body background="../img/timg.jpg">
	<div align="center">
    <img src="../img/bn_product.jpg" width=400>
    <table width=400>
    <tr>
        <td><a href="../Index.html">返回首页</a></td>
        <td></td>
        <td></td>
    </tr>
    
    <tr>
        <td></td>
        <td></td>
        <td></td>
        
    </tr>
    </table></div>
	<form action="">
    <table width="400" border="1" cellspacing="0" cellpadding="0" align="center">
  <tbody>
    <tr>
      <td align="right"><label for="textfield">工作频率:</label></td><td>
      <input type="text" name="Fre" id="Fre" value="{0}" size=6>GHz</td>
    </tr>
    <tr>
      <td align="right"><label for="textfield2">天线口径:</label></td><td>
      <input type="text" name="d" id="d" value="{1}" size=6>m</td>
    </tr>
    <tr>
      <td align="right"><label for="textfield3">天线效率:</label></td><td>
      <input type="text" name="yita" id="yita" value="{2}" size=6>%</td>
    </tr>
    <tr>
      <td align="right"><input type="submit" name="button" id="button" value="计算" size=6></td><td></td>
    </tr>
    <tr>
      <td align="right">天线增益：</td><td>{3}</td>
    </tr>
    <tr>
      <td align="right">3dB波束宽度：</td><td>{4}</td>
    </tr>
  </tbody>
</table>
	</form>

    <div align="center"><iframe src="../Footer.html" frameborder="0"  scrolling="no"></iframe></div>
    </body></html>
    '''.format(Fre, d, yita, Gain, WaveWidth))