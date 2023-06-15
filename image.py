import cv2
import matplotlib.pyplot as plt
import copy
from segmentation import segmentation1 
from segmentation import BinarImageConvertion
from segmentation import group
import sys


sys.setrecursionlimit(10**6)


print("starting")




path = r'color.jpg'
img = cv2.imread(path, 0)
thresholdimage=BinarImageConvertion(img)
plt.imshow(thresholdimage)


segment=segmentation1(thresholdimage)
plt.imshow(segment)

print("conversion done")
plt.imsave('xyz.jpg', segment)







# edgeTouchingRemoved=clear_border(thresholdimage)        
# labelimage=measure.label(edgeTouchingRemoved)
# colorlabel=label2rgb(labelimage)
# plt.imshow(colorlabel)



# def Thining(image):
#     thinimage = np.zeros((len(image),len(image[0])), dtype=np.int32)
#     for row in range(0,len(image)):
#         for col in range(0,len(image)):
#             pick=True
#             if not(0<=row<len(image) and 0<=col<len(image[0]) and image[row][col]==255):
#                 pick=False
#             elif not(0<=row+1<len(image) and 0<=col<len(image[0]) and image[row+1][col]==255):
#                 pick=False
#             elif not(0<=row+1<len(image) and 0<=col-1<len(image[0]) and image[row+1][col-1]==255):
#                 pick=False
#             elif not(0<=row+1<len(image) and 0<=col+1<len(image[0]) and image[row+1][col+1]==255):
#                 pick=False
#             elif not(0<=row+2<len(image) and 0<=col<len(image[0]) and image[row+2][col]==255):
#                 pick=False
            
            
#             if pick:
#                 thinimage[row+1][col]=255
#     return thinimage


# thin=copy.copy(thresholdimage)

# for i in range(0,10):
#     thin=Thining(thin)
# #plt.imsave('blackhorse.jpg',thresholdimage)
# plt.imsave('thinhorse.jpg',thin)


# #cv2.imwrite('color.jpg',img)
# #cv2.imwrite('gray.jpg',grayimage)
# #cv2.imwrite('black.jpg',thresholdimg)


