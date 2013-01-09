
"""Some Tool for Jacob Pan."""

# =========================================================================

# Funcion: getAsIntArrFromTxt
#	get the follow form in txt as a array
#	1 2 3
#	4 5 6
#	retun a array: [ [1, 2, 3], [4, 5, 6] ]
#
def getAsIntArr2DFromTxt( filename ):
	fobj = open( filename )
	arr_2D = list()
	for line in fobj:
		line = line[0:line.find(' \n')]
		arr_2D.append( map( int, line.split(' ') ) )
	fobj.close()
	return arr_2D

def saveAsIntArr2DToTxt( filename, arr_2D ):
	fobj = open( filename, 'w' )
	for arr_1D in arr_2D:
		fobj.writelines( [ "%d "%x for x in arr_1D ] )
		fobj.writelines( "\n" )
	fobj.close()

# 1 2 3 | 1 2 3 | 3 2 1
def saveAsIntArr3DToTxt( filename, arr_3D ):
	fobj = open( filename, 'w' )
	for arr_2D in arr_3D:
		for arr_1D in arr_2D:
			fobj.writelines( [ "%d "%x for x in arr_1D ] )
			fobj.writelines( '|' )
		fobj.writelines( '\n' )
	fobj.close()

def getAsIntArr3DFromTxt( filename ):
	fobj = open( filename )
	arr_3D = list()
	for line in fobj:
		arr_2D = list()
		line = line[0:line.find(' |\n')]
		iner_lines = line.split( ' |' )
		for iner_line in iner_lines:
			arr_2D.append( map( int, iner_line.split(' ') ) )
		arr_3D.append( arr_2D )
	fobj.close()
	return arr_3D

# write a [1,2,3]

if __name__ == '__main__':
	saveAsIntArr3DToTxt( 'tool.txt', (((9,9,9),(100,120,300)),((1,2),(0,0))) )
	print getAsIntArr3DFromTxt( "tool.txt" )




