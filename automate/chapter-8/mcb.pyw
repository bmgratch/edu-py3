#! python3
# mcb.pyw -saves and loads pieces of text to the clipboard
# usage:    py.exe mcb.pyw save <keyword> - saves clipboard to keyword
#           py.exe mcb.pyw <keyword> - loads keyword to clipboard
#           py.exe mcb.pyw  list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO save clipboard content
# TODO List keywords and load content


mcbShelf.close()
