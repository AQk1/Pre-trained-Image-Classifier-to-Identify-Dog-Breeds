#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Abdullah Alkathiri
# DATE CREATED:        January 1, 2024                          
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##

# Import necessary Python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (e.g., filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    # List all items in the directory with pet images
    files = listdir(image_dir)
    
    # Create an empty dictionary
    results_dic = dict()
    
    # Iterate through each filename to save the pet name individually
    for filename in files:
        if not filename.startswith("."):
            pet_label = ' '.join(word.lower() for word in filename.split('_') if word.isalpha())
            
            # Strip leading and trailing whitespace from the pet label
            pet_label = pet_label.strip()
            
            # Add each pet label as a value to the results_dic with the filename as the key
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print('\nWARNING: key =', filename, 'already exists in results_dic with value =', results_dic[filename])
          
    return results_dic
