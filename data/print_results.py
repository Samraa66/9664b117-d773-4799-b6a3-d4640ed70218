#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Print a summary of the results (and misclassifications if requested)
#

def print_results(results_dic,
                  results_stats_dic,
                  model,
                  print_incorrect_dogs=False,
                  print_incorrect_breed=False):
    """
    Prints summary of results and optionally misclassified dogs and breeds.
    
    Parameters:
      results_dic - Dictionary with filename as key and value list:
                    [pet_label, classifier_label, match(1/0),
                     pet_is_dog(1/0), cls_is_dog(1/0)]
      results_stats_dic - Dictionary with statistics (counts & percentages)
      model - CNN model architecture name (string)
      print_incorrect_dogs - True prints misclassified dogs (default False)
      print_incorrect_breed - True prints misclassified breeds (default False)
    """

    # Header
    print(f"\n*** Results Summary for CNN Model Architecture: {model.upper()} ***")

    # Counts
    print(f"Number of Images:          {results_stats_dic['n_images']}")
    print(f"Number of Dog Images:      {results_stats_dic['n_dogs_img']}")
    print(f"Number of 'Not-a' Dogs:    {results_stats_dic['n_notdogs_img']}")

    # Percentages
    for k in results_stats_dic:
        if k.startswith('pct_'):
            print(f"{k:20}: {results_stats_dic[k]:5.1f}%")

    # Misclassified dogs 
    if print_incorrect_dogs:
        if (results_stats_dic['n_correct_dogs'] +
            results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images']:
            print("\nMisclassified Dogs:")
            for fname, vals in results_dic.items():
                if sum(vals[3:5]) == 1:  # one says dog, other says not-dog
                    print(f"  Pet: {vals[0]:20}  |  Classifier: {vals[1]}")

    # Misclassified breeds 
    if print_incorrect_breed:
        if results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
            print("\nMisclassified Breeds:")
            for fname, vals in results_dic.items():
                if sum(vals[3:5]) == 2 and vals[2] == 0:  # both dogs, wrong breed
                    print(f"  Pet: {vals[0]:20}  |  Classifier: {vals[1]}")
