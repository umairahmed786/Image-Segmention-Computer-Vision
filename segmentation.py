
def group( row,col,alpha,image,groupedImage):
    groupedImage[row][col]=alpha
    
    if 0<=row-1<len(groupedImage):
        if image[row-1][col]==True and groupedImage[row-1][col]==0:
            group(row-1,col,alpha,image,groupedImage)
    if 0<=row+1<len(groupedImage):
        if image[row+1][col]==True and groupedImage[row+1][col]==0:
            group(row+1,col,alpha,image,groupedImage)
    if 0<=col-1<len(groupedImage[0]):
        if image[row][col-1]==True and groupedImage[row][col-1]==0:
            group(row,col-1,alpha,image,groupedImage)
    if 0<=col+1<len(groupedImage[0]):
        if image[row][col+1]==True and groupedImage[row][col+1]==0:
            group(row,col+1,alpha,image,groupedImage)        
    if 0<=row-1<len(groupedImage) and 0<=col+1<len(groupedImage[0]):
        if image[row-1][col+1]==True and groupedImage[row-1][col+1]==0:
            group(row-1,col+1,alpha,image,groupedImage)    
    if 0<=row+1<len(groupedImage) and 0<=col-1<len(groupedImage[0]):
        if image[row+1][col-1]==True and groupedImage[row+1][col-1]==0:
            group(row+1,col-1,alpha,image,groupedImage) 
    return 0
            
def segmentation1(image):
    import numpy as np
    groupedImage = np.zeros((len(image),len(image[0])), dtype=np.int32)       
    count=0
    for row in range(0,len(groupedImage)):
        for col in range(0,len(groupedImage[0])):
            if image[row][col]==True and groupedImage[row][col]==0:            
                count=count+1
                
                group(row,col,count,image,groupedImage)
    segmentedColorImage=np.zeros((len(image),len(image[0]),3), dtype=np.float64)

    for groupnum in range(0,groupedImage.max()+1):
        color=tuple(np.random.randint(256, size=3))
        for row in range(0,len(groupedImage)):
            for col in range(0,len(groupedImage[0])):
                if(groupedImage[row][col]==groupnum):
                    segmentedColorImage[row][col][0]=color[0]
                    segmentedColorImage[row][col][1]=color[1]
                    segmentedColorImage[row][col][2]=color[2]           
    segmentedColorImage=segmentedColorImage/255
    return segmentedColorImage



def BinarImageConvertion(image):
    from skimage.filters import threshold_otsu
    #grayimage=image[:,:,0]*0.1140+image[:,:,1]*0.5870+image[:,:,2]*0.2989 
    grayimage=image
    threshold=threshold_otsu(grayimage)
    thresholdimg=grayimage<threshold+35
    return thresholdimg

            
    