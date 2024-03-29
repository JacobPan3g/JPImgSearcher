
"""The result view of searcher."""

import wx
import searcher as sr

class BlockWindow( wx.StaticBitmap ):
	def __init__( self, parent, id=-1, pos=wx.DefaultPosition, size=(192,192), imgName=""):
		bitmap = wx.Image( imgName, wx.BITMAP_TYPE_JPEG )
		w = bitmap.GetWidth()
		h = bitmap.GetHeight()
		bitmap = bitmap.Scale( 128, 128 )
#pos = ((192-w)/2,(192-h)/2)
		pos = (100,100)
		wx.StaticBitmap.__init__( self, parent, id, bitmap.ConvertToBitmap(), pos, size )
		self.SetMinSize( size )
		
class GridSizerFrame( wx.Frame ):
	def __init__( self, imgNameArr ):
		wx.Frame.__init__( self, None, -1, "Imager Searcher", size=(1366, 768) )
		self.scroll = wx.ScrolledWindow( self, -1 )
		self.scroll.SetScrollbars(1,1, 0, 0)
		sizer = wx.GridSizer( rows=0, cols=7, hgap=3, vgap=3 )
		
		for imgName in imgNameArr:
			name = "images/%d.jpg" % imgName	
			bw = BlockWindow( self.scroll, imgName=name )
			sizer.Add( bw, flag=wx.ALIGN_CENTER )
		
		self.scroll.SetSizer( sizer )
		self.scroll.Fit()

def startGUI( imgNameArr ):
	# Start the GUI view
	app = wx.PySimpleApp()
	GridSizerFrame( imgNameArr ).Show()
	app.MainLoop()
	
def main():
	while( True ):
		# input
		print "Please input the Image:"
		curName = raw_input()
		if int(curName) > 1000 or int(curName) < 0:
			break
		# search
		imgs = sr.getImgs()
		imgNameArr,resDetial,checkRate = sr.searcher( "images/"+curName+".jpg", 'images/', curName, 1000, 100, imgs )
		startGUI( imgNameArr )
		print "==========================================="
		print "The check rate of image "+curName+".jpg is:"
		print checkRate
		print "==========================================="
	print "Exit"

if __name__ == '__main__':
	main()
