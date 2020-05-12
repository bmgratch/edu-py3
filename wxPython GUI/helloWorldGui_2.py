#wxPython GUI
#Hello World!
import wx
#Add an application object
app = wx.App()
# Then add a frame
frm = wx.Frame(None, title="Hello World")

#Display it
frm.Show()

#Start event loop
app.MainLoop()
