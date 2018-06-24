import io

HtmlFile = io.open(r"ChainCal.html")
HtmlStr = HtmlFile.read()
HtmlFile.close
print(HtmlStr)
