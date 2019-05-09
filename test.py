from PIL import Image
arr = ['p1.jpg', 'p2.jpg']
toImage = Image.new('RGBA',(2550,3501))
box=(787,1100,1987,2080)

for i in range(2):
    fromImge = Image.open(arr[i])
    cropped = fromImge.crop(box)
    #cropped.save("./a{}.jpg".format(i))
    if(i==0):    
        loc = (785,275)
    else:
	    loc=(785,2025)
    toImage.paste(cropped,loc)
#
    
    #loc = ((int(i/2) * 200), (i % 2) * 200)
    #print(loc)
	#fromImge=fromImge[1303:2019, 863:1968]
    #toImage.paste(fromImge, loc)
	#print(fromImge.size())
#	cropped = fromImge.crop(box)
#	cropped.save("./a.jpg{}".format(i))
toImage.save('merged.png')
