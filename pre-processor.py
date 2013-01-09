
"""Pre-processing for searching."""

import math
import Image
import JPTool

# Function: openImg
# 	Open the image in the same schema (RGB and 256x256)
#	Parameters:
#		imgName:String	the name of the image
#	Return:
#		the Image Object
def openImg( imgName ):
	return Image.open(imgName).resize((256,256)).convert('RGB')

# Function: split
#	Split the Image
#	Parameters:
#		img:Image	the image
#		size:truple	the size of image
#	Return:
#		the array of the splited images
def split( img, size=(32,32)):
	w, h = img.size
	sw, sh = size 
	return [img.crop((i, j, i+sw, j+sh)).copy() \
				for i in xrange(0, w, sw) \
				for j in xrange(0, h, sh)]

# Function: rgb2hsi
#	Transfore the rgb to hsi
#	Parameters:
#		rgbImg:Image	the image of rgb
#	Return:
#		the imgage of hsi
def rgb2hsi( rgbImg ):
	#rgbImg = openImg("CBIRdataset/images/900.jpg")
	rgbMat = list(rgbImg.getdata())
	hsiMat = list()
	for i in rgbMat:
		R = i[0]/255.0
		G = i[1]/255.0
		B = i[2]/255.0
		
		h = (180/math.pi) * math.acos(0.5*((R-G)+(R-B))/(math.sqrt((R-G)*(R-G)+(R-B)*(G-B))+0.000001))
		if B > G:
			h = 360 - h
		s = 1 - 3/(R+G+B+0.000001)*min((R,G,B))
		i = sum((R,G,B))/3.0
		hsiMat.append((h,s,i))
		# Here here
	return hsiMat

# Function: statitict
#	statitict and quantization the hsi histogram
#	Parameter:
#		imgArr;Array		the rgb histogram array of a splited image
#		nums:int			the number of blocks
def statitict( imgArr, nums ):
	H = [0, 0, 0, 0, 0, 0, 0, 0]
	S = [0, 0 ,0]
	I = [0, 0, 0]	
	# statitic HSI
	for i in nums:
		hsiMat = rgb2hsi( imgArr[i] )
		for point in hsiMat:
			# statitict the H
			if point[0] >= 21 and point[0] <= 40:
				H[1] += 1
			elif point[0] >= 41 and point[0] <= 75:
				H[2] += 1
			elif point[0] >= 76 and point[0] <= 155:
				H[3] += 1
			elif point[0] >= 156 and point[0] <= 190:
				H[4] += 1
			elif point[0] >= 191 and point[0] <= 270:
				H[5] += 1
			elif point[0] >= 271 and point[0] <= 295:
				H[6] += 1
			elif point[0] >= 296 and point[0] <= 315:
				H[7] += 1
			else:
				H[0] += 1	
			# statitict the S
			if point[1] >= 0 and point[1] < 0.2:
				S[0] += 1
			elif point[1] >= 0.2 and point[1] < 0.7:
				S[1] += 1
			else:
				S[2] += 1
			# statitict the I
			if point[2] >= 0 and point[2] < 0.2:
				I[0] += 1
			elif point[2] >= 0.2 and point[2] < 0.7:
				I[1] += 1
			else:
				I[2] += 1
	# calculate the arr72
	# motify here
	arr72 = [9*h+3*s+i for i in I for s in S for h in H]
	
	#arr72 = H
	#arr72.append(S[0])
	#arr72.append(S[1])
	#arr72.append(S[2])
	#arr72.append(I[0])
	#arr72.append(I[1])
	#arr72.append(I[2])
	return arr72

# Function: getCharacteristics
# 	Get the characteristics of 12 partions
#	Parameters:
#		imgArr:Image	the arr of 16x16 images splited from a image
#	Return:
#		the characteristics of 12 partions
def getCharacteristics( img ):
	# the partion array
	partion = ( \
		[0],\
		[7],\
		[56],\
		[63],\
		(8,16,24,32,40,48),\
		(1,2,3,4,5,6),\
		(15,23,31,39,47,55),\
		(57,58,59,60,61,62),\
		(9,10,11,17,18,19,25,26,27,28,35,36),\
		(12,13,14,20,21,22,29,30,27,28,35,36),\
		(33,34,41,42,43,49,50,51,27,28,35,36),\
		(37,38,44,45,46,52,53,54,27,28,35,36) )
	# sqlit the image	
	imgArr = split( img )
	# get the characteristics
	imgChar_12 = list()
	for i in xrange(12):
		arr_72 = statitict( imgArr, partion[i] )
		imgChar_12.append( arr_72 )
	return imgChar_12	

# Funcion: readAllImages
#	read all the image and get their chacteristic and save it
#	Parmameter:
#		search_adress:String	the address of images
#		num_imgs:int			the number of images
#	Return:
#		the arr of the image
def readAllImages( search_adress, num_imgs=1000 ):
	imgs = list()
	for i in xrange(num_imgs):
		imgName = search_adress+'%d.jpg' % (i)
		item = dict()
		img = openImg(imgName)
		item['imgObj'] = img
		item['idx'] = i
		item['charact'] = getCharacteristics( img )
		imgs.append(item)
	return imgs;

def saveChacteristic( imgs ):
#print [img['charact'] for img in imgs]
	JPTool.saveAsIntArr3DToTxt( 'chacteristic.txt', [img['charact'] for img in imgs] )


if __name__ == '__main__':
	imgs = readAllImages( 'images/', 1000 )
	saveChacteristic( imgs )
#print JPTool.getAsIntArr3DFromTxt( 'chacteristic.txt' )
	
	
