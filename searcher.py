
""".The Segment of Image Process"""


import Image
import math
import JPTool

# Function getWeightArr
#	Get the Weights from the file
#	Parameters:
#		label:String	the label name
#	Return:
#		the array of weight
def getWeightArr( label ):
	arr = (0.025, 0.045, 0.18)
	return arr

# Funciton: calculate
#	The main calculator
#	Parameters:
#		curImgChar_12:Array		the cur image chacteristic
#		imgChar_12:Array		the matching image chacteristic
#		weight:Array				the weight Array
#	Return:
#		the same rate
def calculate( curImgChar_12, imgChar_12, weight ):
	# calculating the likehoods
	likehoods = list()
	N = len( imgChar_12 )
	for i in xrange(N):
		x = curImgChar_12[i]
		y = imgChar_12[i]
		xAver = sum( x ) / (N*1.0)
		yAver = sum( y ) / (N*1.0)
		r = sum((xi-xAver)*(yi-yAver) for xi, yi in zip(x,y)) / math.sqrt(sum((xi-xAver)*(xi-xAver) for xi in x)*sum((yi-yAver)*(yi-yAver) for yi in y))
		likehoods.append( r )
	# calculating the total same rate
	rate = weight[0] * sum(likehoods[i] for i in xrange(4)) + weight[1] * sum(likehoods[i+4] for i in xrange(4)) + weight[2] * sum(likehoods[i+8] for i in xrange(4))
	#print rate
	return rate

# Function: calculate_checkRate
#	caculate the checkRate
#	Parameters:
#		resArr:Array		the Array of result idx
#		curIdx:int			the cur image idx
#	Return:
#		the checkRate
def calculate_checkRate( resArr, curIdx ):
	res = 0
	curIdx = int(curIdx)
	rights = 0
	for i in xrange(len(resArr)):
		idx = int(resArr[i])
		R = 0
		if idx/100 == curIdx/100:
			rights = rights + 1
			R = 1
		res = res + (rights*1.0) / (i+1)
	return res / len(resArr)

# Function: searcher
# 	The main function to search the image
#	Parameters:
#		src_address:String		the address of the source image
#		search_adress:String	the search address
#		label:String			the name of cur image
#		num_imgs:int			how many images are in the search address
#		num_match:int			how many images you want to return
#		imgs:Array(Dict)		the data of all images
#	Return:
#		the idx and the Array(Dict) of the matching images
def searcher( src_address, search_adress, label, num_imgs, num_match, imgs ):
	# read all image
	weight = getWeightArr(label)	
	# get the characteristics of cur image
	curItem = imgs[int(label)]
	# calculate the rate
	for item in imgs:
		rate = calculate(curItem['charact'], item['charact'], weight)
		item['rate'] = rate
	res = sorted(imgs, key=lambda x: x['rate'], reverse=True )	
	
	# show the cur Image
	#curItem['imgObj'].show()
	
	#print "Result:"
	#for i in range(num_match):
	#	res[i]['imgObj'].show()

	resArr = list()
	for i in xrange(num_match):
		resArr.append(res[i]['idx'])
	
	# Calculate the check_rate
	check_rate = calculate_checkRate( resArr, label )
	#print check_rate

	return resArr, res, check_rate

# Funcion: getImgs
#	get the image chacteristic from txt
#	Parameter:
#		search_adress:String		the search address
#		num_imgsLint				the number of image would get
#	Return:
#		the image Array(Dict)
def getImgs( search_adress="images/", num_imgs=1000 ):
	tmp = JPTool.getAsIntArr3DFromTxt( 'chacteristic.txt' )
	imgs = list()
	for i in xrange(num_imgs):
		imgName = search_adress+'%d.jpg' % (i)
		item = dict()
		img = Image.open(imgName).resize((256,256)).convert('RGB')
		item['imgObj'] = img
		item['idx'] = i
		item['charact'] =  tmp[i]
		imgs.append(item)
	return imgs;

def writeRateToTxt( checkRates  ):
	fobj = open( 'result.txt', 'w' )
	fobj.writelines( ["%lf\n"%x for x in checkRates] )
	fobj.close()

if __name__ == '__main__':
	imgs = getImgs()
	checkRates = list()
	for i in xrange(1000):
		#print "One finish!:"
		#a = raw_input()
		resArr,res, check_rate = searcher("images/", "images/", i, 1000, 100, imgs)
		checkRates.append( check_rate )
	#print checkRates
	writeRateToTxt( checkRates )

