import numpy as np
import leargist
import csv
from PIL import Image   
  

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


def compute_map_features(ref_map):  #ref_map is a 1D list of images.

    ref_desc_list=[]
    
    for ref_image in ref_map:
        trainDescriptors = leargist.color_gist(ref_image)
        ref_desc_list.append(trainDescriptors)
    
    return ref_desc_list


def compute_query_desc(query):
    queryDescriptors = leargist.color_gist(query)

    return queryDescriptors


def perform_VPR(query_desc,ref_map_features): #ref_map_features is a 1D list of feature descriptors of reference images.
    
    confusion_vector=np.zeros(len(ref_map_features))
    itr=0
   
    for ref_desc in ref_map_features:
	    similarity_score = np.dot(query_desc, ref_desc) / (np.linalg.norm(query_desc) * np.linalg.norm(ref_desc))
	    confusion_vector[itr]=similarity_score
	    itr=itr+1

    max_score=np.amax(confusion_vector)
    max_index=np.argmax(confusion_vector)

    return max_score,max_index


ref_list = []
feature_descriptors = []

for ref in range(total_Ref_Images):
    try:
        img_1 = Image.open(ref_directory+get_ref_image_name(ref))
    
    except (IOError, ValueError) as e:
        img_1=None
        print('Exception! \n \n \n \n',ref)        
        
    if (img_1 is not None):
        
	    ref_list.append(img_1)


query_list = []
for query in range(total_Query_Images):

    try:    
        img_2 = Image.open(query_directory+get_query_image_name(query))

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

	with open('Results_Gist_1024_pixels.csv', 'a') as csvfile:
		my_writer = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
		row= str(i) + ',' + str(index) + ',' + str(score) 
		my_writer.writerow([row])
	csvfile.close() 


