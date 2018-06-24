import math
import cgi
import cgitb

cgitb.enable()

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


print('''
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>通信链路计算</title>
	
</head>
<body background="../img/timg.jpg">
	<img src="../img/bn_product.jpg" width="400">
''')

print('<h1>[{0}]</h1><br>'.format(CAL))

print('''
	<form action="">
	<table width="400">
	<tr>
		<td>载波带宽：</td>
		<td><input type="text" value="2000" name="swidth">kHz</td>
		</tr>
	
	<tr>
		<td>门限信噪比：</td>
		<td><input type="text" value="5" name="ebn0">dB</td>
		</tr>
	<tr><td>门限载噪比：</td>
		<td><input type="submit" name="CAL" value="CAL C/N">{0}</td>
		</tr>
		<tr><td>&nbsp;</td><td>&nbsp;</td></tr>
		<tr>
		  <td><b>发站指标：</b></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>发射频率：</td>
		  <td><input type="text" value="31.0" name="txFre">GHz</td>
	  </tr>
		<tr>
		  <td>天线口径：</td>
		  <td><input type="text" value="1.2" name="txAD">m</td>
	  </tr>
		<tr>
		  <td>天线效率：</td>
		  <td><input type="text" value="50" name="txAY">%</td>
	  </tr>
		<tr>
		  <td>馈线损耗：</td>
		  <td><input type="text" value="0.0" name="txAL1">dB</td>
	  </tr>
		<tr>
		  <td>指向损耗：</td>
		  <td><input type="text" value="0.5" name="txAL2">dB</td>
	  </tr>
		<tr>
		  <td>功放功率：</td>
		  <td><input type="text" value="16" name="txPower">dBW</td>
	  </tr>
		<tr>
		  <td>天线驻波：</td>
		  <td><input type="text" value="2" txVSWR>:1</td>
	  </tr>
		<tr>
		  <td><input type="submit" name="CAL" value="CAL TX"></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>天线增益：</td>
		  <td>{1}</td>
	  </tr>
		<tr>
		  <td>失配损耗：</td>
		  <td>{2}</td>
	  </tr>
		<tr>
		  <td>EIRP：</td>
		  <td>{3}</td>
	  </tr>
		<tr>
		  <td>&nbsp;</td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td><strong>发链路损耗：</strong></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>发站经度：</td>
		  <td><input type="text" value="2" name="txJD"></td>
	  </tr>
		<tr>
		  <td>发站纬度：</td>
		  <td><input type="text" value="2" name="txWD"></td>
	  </tr>
		<tr>
		  <td>卫星经度：</td>
		  <td><input type="text" value="2" name="sJD1"></td>
	  </tr>
		<tr>
		  <td><input type="submit" name="CAL" value="CAL TX LOSS"></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>传输距离：</td>
		  <td>{4}</td>
	  </tr>
		<tr>
		  <td>传输损耗：</td>
		  <td>{5}</td>
	  </tr>
		<tr>
		  <td>信号通量：</td>
		  <td>{6}(可达到的值)</td>
	  </tr>
		<tr>
		  <td>&nbsp;</td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td><strong>星上指标：</strong></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>饱和通量：</td>
		  <td><input type="text" value="-115" name="sSFD">W/m^2</td>
	  </tr>
		<tr>
		  <td>EIRP：</td>
		  <td><input type="text" value="36" name="sEIRP">dBW</td>
	  </tr>
		<tr>
		  <td>G/T：</td>
		  <td><input type="text" value="2" name="sGT">dB/K</td>
	  </tr>
		<tr>
		  <td>输入补偿：</td>
		  <td><input type="text" value="6" name="inputBackOff">dB</td>
	  </tr>
		<tr>
		  <td>输出补偿：</td>
		  <td><input type="text" value="3" name="outputBackOff">dB</td>
	  </tr>
		<tr>
		  <td>转发器带宽：</td>
		  <td><input type="text" value="36" name="transponderWidth">MHz</td>
	  </tr>
		<tr>
		  <td><input type="submit" name="CAL" value="CAL TRANSPONDER"></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>载波回退：</td>
		  <td>{7}</td>
	  </tr>
		<tr>
		  <td>转发器增益：</td>
		  <td>{8}</td>
	  </tr>
		<tr>
		  <td>可达C/N：</td>
		  <td>{9}</td>
	  </tr>
		<tr>
		  <td>实际C/N：</td>
		  <td>{10}以星上饱和通量计算</td>
	  </tr>
		<tr>
		  <td>下行信号功率：</td>
		  <td>{11}最大为卫星EIRP</td>
	  </tr>
		<tr>
		  <td>星上增益：</td>
		  <td>{12}</td>
	  </tr>
		<tr>
		  <td>&nbsp;</td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td><strong>收链路损耗：</strong></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>收站经度：</td>
		  <td><input type="text" value="2" name="rxJD"></td>
	  </tr>
		<tr>
		  <td>收站纬度：</td>
		  <td><input type="text" value="2" name="rxWD"></td>
	  </tr>
		<tr>
		  <td>卫星经度：</td>
		  <td><input type="text" value="2" name="sJD2"></td>
	  </tr>
		<tr>
		  <td>下行频率：</td>
		  <td><input type="text" value="21.2" name="rxFre">GHz</td>
	  </tr>
		<tr>
		  <td><input type="submit" name="CAL" value="CAL RX LOSS"></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>传输距离：</td>
		  <td>{13}</td>
	  </tr>
		<tr>
		  <td>传输损耗：</td>
		  <td>{14}</td>
	  </tr>
		<tr>
		  <td>&nbsp;</td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td><strong>收站指标：</strong></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>天线口径：</td>
		  <td><input type="text" value="1.2" name="rxAD">m</td>
	  </tr>
		<tr>
		  <td>天线效率：</td>
		  <td><input type="text" value="50" name="rxAY">%</td>
	  </tr>
		<tr>
		  <td>馈线损耗：</td>
		  <td><input type="text" value="0.5" name="rxAL1">dB</td>
	  </tr>
		<tr>
		  <td>指向损耗：</td>
		  <td><input type="text" value="0.5" name="rxAL2">dB</td>
	  </tr>
		<tr>
		  <td>天线驻波：</td>
		  <td><input type="text" value="2" name="rxVSWR">:1</td>
	  </tr>
		<tr>
		  <td>天线噪温：</td>
		  <td><input type="text" value="100" name="rxANT">K</td>
	  </tr>
		<tr>
		  <td>低噪噪温：</td>
		  <td><input type="text" value="120" name="LNAT">K</td>
	  </tr>
		<tr>
		  <td><input type="submit" name="CAL" value="CAL RX"></td>
		  <td>&nbsp;</td>
	  </tr>
		<tr>
		  <td>天线增益：</td>
		  <td>{15}</td>
	  </tr>
		<tr>
		  <td>噪声温度：</td>
		  <td>{16}</td>
	  </tr>
		<tr>
		  <td>G/T：</td>
		  <td>{17}</td>
	  </tr>
		<tr>
		  <td>失配损耗：</td>
		  <td>{18}</td>
	  </tr>
		<tr>
		  <td>下行C/N：</td>
		  <td>{19}</td>
	  </tr>
		<tr>
		  <td>&nbsp;</td>
		  <td>&nbsp;</td>
	  </tr>
	</table></form>	
	<div align="center"><iframe src="../Footer.html" frameborder="0"  scrolling="no"></iframe></div>
	</body>
</html>
''')
