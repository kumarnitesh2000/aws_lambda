import pybase64
image=open("deer.gif","rb")
image_read=image.read()
print(image_read)
#now want to encode the image
image_64_encode=pybase64.b64encode(image_read)
print(image_64_encode)
print(type(image_64_encode))
#now decoding the image .
image_64_decode=pybase64.b64decode(image_64_encode)
print(image_64_decode)
image_result=open("deer_decode.gif","wb")
image_result.write(image_64_decode)
