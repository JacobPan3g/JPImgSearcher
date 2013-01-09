import Image
import math

# The Segment of Image Process



# Function: calculate_checkRate
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

# Function: searcherForTaining
#	The process of the function searcher
#	Parameters:
#		src_address:String		the address of the source image
#		search_adress:String	the search address
#		weight:array			the weight array
#		curImgChar_12:array		the array of characteristic
#		num_imgs:int			how many images are in the search address
#		num_match:int			how many images you want to return
#	Return:
#		the image after processing		


# Function: searcher
# 	The main function to search the image
#	Parameters:
#		src_address:String		the address of the source image
#		search_adress:String	the search address
#		num_imgs:int			how many images are in the search address
#		num_match:int			how many images you want to return
#	Return:
#		the idx of the matching images
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
	print check_rate

	return resArr, res
	


if __name__ == '__main__':
	imgs = readAllImages( "images/" )
	print "read finish!"
	for i in xrange(1000):
		a = raw_input()
		resArr,res = searcher("images/", "images/", i, 1000, 100, imgs)
	

