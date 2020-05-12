#wxPython GUI
#Hello World! pt 2
import wx

class HelloFrame(wx.Frame):
    # A frame that says Hello World

    def __init__(self, *args, **kw):
        # Ensure parent's init is called
        super(HelloFrame, self).__init__(*args, **kw)

        # Create a panel in the frame
        pnl = wx.Panel(self)

        # put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="Hello World")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # Createa sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # Create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

    def makeMenuBar(self):
        # A menu bar is composed of menus, which are composed of menu items.
        # This method builds a set of menus and binds handlers to be called.

        # make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # the "\t..." syntax defines an accelerator key that also triggers the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                                    "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using stock ID, we don't need to specify the menu's label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defiens that
        # The next letter is the mnemonic for the menu item.  On the platforms
        # That support it, those letters are underlined and can be triggered by
        # the keyboard
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the meny bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means whent he menu item is activated
        # then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        self.Close(True)


    def OnHello(self, event):
        wx.MessageBox("Hello again, from wx.Python")


    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello World Sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)

if __name__ == '__main__':
    # When this module is run (not imported)
    # Create the app, the frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Hello World 2')
    frm.Show()
    app.MainLoop()
