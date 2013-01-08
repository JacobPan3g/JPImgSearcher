
"""The result view of searcher."""

import wx

class BlockWindow( wx.StaticBitmap ):
	def __init__( self, parent, id=-1, pos=wx.DefaultPosition, size=(192,192), imgName=""):
		bitmap = wx.Image( imgName, wx.BITMAP_TYPE_JPEG )
		w = bitmap.GetWidth()
		h = bitmap.GetHeight()
		bitmap = bitmap.Scale( w/2, h/2 )
#pos = ((192-w)/2,(192-h)/2)
		pos = (100,100)
		wx.StaticBitmap.__init__( self, parent, id, bitmap.ConvertToBitmap(), pos, size )
		self.SetMinSize( size )
		
class GridSizerFrame( wx.Frame ):
	def __init__( self ):
		wx.Frame.__init__( self, None, -1, "Imager Searcher", size=(1366, 768) )
		self.scroll = wx.ScrolledWindow( self, -1 )
		self.scroll.SetScrollbars(1,1, 0, 0)
		sizer = wx.GridSizer( rows=0, cols=7, hgap=3, vgap=3 )
		
		for i in xrange(100):
			name = "images/%d.jpg" % i	
			bw = BlockWindow( self.scroll, imgName=name )
			sizer.Add( bw, flag=wx.ALIGN_CENTER )
		
		self.scroll.SetSizer( sizer )
		self.scroll.Fit()

app = wx.PySimpleApp()
GridSizerFrame().Show()
app.MainLoop()
	
