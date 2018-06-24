import win32com.client as win32


def endIndex(WordDoc):
    DocAllRange = WordDoc.Range()
    return DocAllRange.End


def tableIndex(WordDoc):
    return WordDoc.Tables.Count


def insertTitle(WordDoc):
    WordDoc.Content.InsertAfter("原始记录\n")
    WordDoc.Content.InsertAfter("第   页  共   页\n")
    WordDoc.Content.InsertAfter("设备编号：\n")
    WordDoc.Content.InsertAfter("\n")
    eI = endIndex(WordDoc)
    WordDoc.Tables.Add(WordDoc.Range(eI - 1, eI), 1, 5)
    tI = tableIndex(WordDoc)
    WordDoc.Tables(tI).Rows(1).Cells(1).Range.Text = "序号"
    WordDoc.Tables(tI).Rows(1).Cells(1).Range.Text = "项目"
    WordDoc.Tables(tI).Rows(1).Cells(1).Range.Text = "技术要求"
    WordDoc.Tables(tI).Rows(1).Cells(1).Range.Text = "测试结果"
    WordDoc.Tables(tI).Rows(1).Cells(1).Range.Text = "备注"
    WordDoc.Tables(tI).Rows.Add()
    WordDoc.Tables(tI).Borders.Enable
    WordDoc.Tables(tI).Borders.InsideLineStyle = 1
    WordDoc.Tables(tI).Borders.OutsideLineStyle = 1
    WordDoc.Tables(tI).Borders.InsideLineWidth = 4
    WordDoc.Tables(tI).Borders.OutsideLineWidth = 12
    WordDoc.Tables(tI).Rows(1).Borders.OutsideLineWidth = 12


try:
    WordApp2 = win32.Dispatch('Word.Application')
    if WordApp2.Documents.Count > 0:
        for i in range(1, WordApp2.Documents.Count + 1):
            if WordApp2.Documents(i).Name == '原始记录.docx':
                print('打开文档：' + WordApp2.Documents(i).Name)
                WordDoc2 = WordApp2.Documents(i)
                break
            else:
                print('打开第{0}个文档：'.format(i) + WordApp2.Documents(i).Name)
        else:
            WordDoc2 = WordApp2.ActiveDocument
            print('打开文档：' + WordDoc2.Name)
    else:
        WordApp2 = win32.gencache.EnsureDispatch('Word.Application')
        WordApp2.Visible = 1
        WordDoc2 = WordApp2.Documents.Add()
        insertTitle(WordDoc2)
except Exception as e:
    print(repr(e))
finally:
    pass


print('')
print('WordApp2=' + repr(WordApp2))
print('WordDoc2=' + repr(WordDoc2))

WordDoc2.Content.InsertAfter("原始记录")
