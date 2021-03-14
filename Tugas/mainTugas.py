import wx
import tampilanTugas

class subClass(tampilanTugas.MyFrame_Rachma):
    def __init__(self, parent) :
        tampilanTugas.MyFrame_Rachma.__init__(self, parent)

app =wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()
