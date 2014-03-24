import xbmc xbmcgui

class MyClass(xbmcgui.Window):
	print "hello world"
mydisplay = MyClass()
mydisplay.doModal()
del mydisplay 