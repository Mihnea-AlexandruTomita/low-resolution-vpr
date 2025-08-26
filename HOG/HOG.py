import cv2
import numpy as np
import csv


total_Query_Images = 100  # Number of images in the query folder
total_Ref_Images = 100    # Number of images in the reference folder
ref_index_offset = 0
query_index_offset = 0

# NOTE: Update the query and reference image paths below to point to your own dataset
query_directory = '/home/mihnea/resized_datasets/1024_pixels/Campus_Loop/query/'
ref_directory = '/home/mihnea/resized_datasets/1024_pixels/Campus_Loop/map/'


def get_query_image_name(query):
    query_name = str(query + query_index_offset)

    return query_name + '.jpg'

def get_ref_image_name(ref):
    ref_name = str(ref + ref_index_offset)

    return ref_name + '.jpg'

#Create feature descriptors from the reference images
def compute_map_features(ref_map):
    
    winSize = (512,512)
    blockSize = (32,32)
    blockStride = (16,16)
    cellSize = (16,16)
    nbins = 9
    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)
    ref_desc_list=[]
    
    for ref_image in ref_map:
        
        if ref_image is not None:    
            hog_desc=hog.compute(cv2.resize(ref_image, winSize))
            
        ref_desc_list.append(hog_desc)

        
    return ref_desc_list

#Create feature descriptors from the query images
def compute_query_desc(query):
        
    winSize = (512,512)
    blockSize = (32,32)
    blockStride = (16,16)
    cellSize = (16,16)
    nbins = 9
    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)
    query_desc=hog.compute(cv2.resize(query, winSize))
    
    return query_desc

# Compares a query descriptor against all reference descriptors
# Returns the highest similarity score along with the index of the closest match
def perform_VPR(query_desc,ref_map_features):

    confusion_vector=np.zeros(len(ref_map_features))
    itr=0
    for ref_desc in ref_map_features:
        score=np.dot(query_desc.T,ref_desc)/(np.linalg.norm(query_desc)*np.linalg.norm(ref_desc))
        confusion_vector[itr]=score
        itr=itr+1
        
    return np.amax(confusion_vector), np.argmax(confusion_vector)


ref_list = []
feature_descriptors = []
for ref in range(total_Ref_Images):
    
    try:
        img_1 = cv2.imread(ref_directory+get_ref_image_name(ref), 0)
    
    except (IOError, ValueError) as e:
        img_1=None
        print('Exception! \n \n \n \n',ref)        
        
    if (img_1 is not None):
        
	    ref_list.append(img_1)


query_list = []
for query in range(total_Query_Images):
    
    try:    
        img_2 = cv2.imread(query_directory+get_query_image_name(query), 0)

    except (IOError, ValueError) as e:
        img_2=None        
        print('Exception! \n \n \n \n')    
       
    if (img_2 is not None):
	    query_list.append(img_2)


feature_descriptors = compute_map_features(ref_list)

query_descriptor = []
for i in range(len(query_list)):
	query_descriptor.append(compute_query_desc(query_list[i]))


for i in range(len(query_list)):

	score, index = perform_VPR(query_descriptor[i],feature_descriptors)

	with open('Results_HOG_1024_pixels.csv', 'a') as csvfile:
		my_writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		row= str(i) + ',' + str(index) + ',' + str(score) 
		my_writer.writerow([row])
	csvfile.close() 



	  
