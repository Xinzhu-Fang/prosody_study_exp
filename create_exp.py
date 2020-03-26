# dput(sort(unique()))
# Three navtive speaekers were asked to classifiy sex for these namees into Female (F), Male (M), and Ambiguous (A). For each name, if at least two people both chose F of M and the third one chose A, the name is put in the majority sex category, otherwise the name is discarded.

# In order to have the filler questions be the same indepdent of the correction condition, the "wrong" list, or the question list, is the same acroos exps; the "correct" list was initilized to be different from the "wrong" on each trial and then adjusted to the same as "wrong" on control trials, in which the "wrong" is actaully correct.
# This way of creating wrong instead of correct first -- how items were created -- can bd problematic because I don't have full sex combinations for each action and the sexes for question verbs may not match those of picture verbs. The solution is to choose verbs from the same sex category. 


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import create_stimuli



exps_names = ['exp0', 'exp1', 'exp2', 'exp3', 'exp4', 'exp5', 'exp6', 'exp7', 'exp8', 'exp9', 'exp10', 
              'exp11', 'exp12']
num_exp = len(exps_names)
bCreate_stimuli = 1

#locations = ['Agent', 'Verb', 'Patient']
#num_locations = len(locations)
my_seed = [1, 1, 1, 5, 4] # the first four seeds are each for item, wrong filler verb, wrong filler agent, and wrong filler patient. again, "wrong". I lazily increment to the last until there is no repetition in the more yes, verison, and modifiy the more no version if there is still repetition.
# the last one is for trial shuffling, I tried up to 4, 4 and 2 create one neighbouring repetition.

#nth_exp = 0
#for iExp in [3]:
for iExp in range(num_exp):
    exp_name = exps_names[iExp]
    exp_lan = ['ch', 'en', 'en', # 0 1 2
               'en', 'en', 'en', # 3 4 5
               'en', 'en', 'en', # 6 7 8 
               'en', 'en', 'en',
               'en'][iExp] # 9 10 11
    exp_questioner = ['cindy','ted','ted', # 0 1 2
                      'ted','ted','ted', # 3 4 5
                      'ted','ted','ted', # 6 7 8 
                      'ted','computer', 'text', # 9 10 11
                      'computer' # 12 13 14
                      ][iExp]
#    exp_num_of_items = np.append(np.repeat(4, 9), 1)[iExp]
    exp_num_of_items = np.repeat(4, num_exp)[iExp]

    exp_yes_to_no_ratio = [2, 2, 0.5, # 0 1 2
                           0.125, 0.125, 2, # 3 4 5
                           0.125, 2, 0.5, # 6 7 8
                           0.125, 2, 2, # 9 10 11
                           2
                           ][iExp] # 9 10 11
    exp_num_trials = np.repeat(72, num_exp)[iExp] #72 allows 1:2, 1:1, and 2:1 4 items and 2 trials each
#

    locations = [['Agent', 'Verb', 'Patient'], ['Agent', 'Verb', 'Patient'], ['Agent', 'Verb', 'Patient'], # 0 1 2
                 ['Agent', 'Verb', 'Patient'], ['Agent'], ['Agent', 'Verb', 'Patient'], # 3 4 5
                 ['Agent'], ['Agent', 'Verb', 'Patient'], ['Agent'], # 6 7 8
                 ['Agent'], ['Agent', 'Verb', 'Patient'], ['Agent', 'Verb', 'Patient'], # 9 10 11
                 ['Agent', 'Verb', 'Patient'] # 12 13 14
                 ][iExp]
    num_locations = len(locations)

#    exp_num_of_correction_for_each_location_for_each_item = np.repeat(2, num_exp)[iExp]
    # * exp_num_of_items / 4 was made to accomodate exp9
#    exp_num_of_control_for_each_item = 2 * 4 / exp_num_of_items
#    exp_num_of_correction_for_each_location_for_each_item = int(exp_num_of_control_for_each_item * 3 /num_locations) * 4 / exp_num_of_items
    exp_num_of_control_for_each_item = 2 
    exp_num_of_correction_for_each_location_for_each_item = int(exp_num_of_control_for_each_item * 3 /num_locations) 
   
    # exp_num_of_control_for_each_item = np.repeat(2, 3)[iExp]

    item_num_trial_yes = exp_num_of_items * exp_num_of_control_for_each_item
    item_num_trial_no = exp_num_of_items * exp_num_of_correction_for_each_location_for_each_item * num_locations
    item_num_trial_for_each_item = exp_num_of_control_for_each_item + exp_num_of_correction_for_each_location_for_each_item * num_locations
    item_num_trial_total = item_num_trial_yes + item_num_trial_no
    exp_num_trial_yes = int(exp_num_trials / (exp_yes_to_no_ratio + 1 ) * exp_yes_to_no_ratio)
    exp_num_trial_no = exp_num_trials - exp_num_trial_yes


    filler_num_trial_yes = exp_num_trial_yes - item_num_trial_yes
    filler_num_trial_no = exp_num_trial_no - item_num_trial_no
    filler_num_trial_total = filler_num_trial_yes + filler_num_trial_no

# when you change this, remember to change in psiturk accordingly!!!! 
# no need to change pisturk if you keep appending new parameters    
    tCur_exp = pd.DataFrame([[exp_name, exp_lan, exp_num_trials, locations, num_locations, exp_num_of_items,
                              exp_yes_to_no_ratio, exp_num_trial_yes,
                              exp_num_trial_no, exp_num_of_control_for_each_item,
                              exp_num_of_correction_for_each_location_for_each_item,
                              item_num_trial_total, item_num_trial_yes, item_num_trial_no,
                              item_num_trial_for_each_item, filler_num_trial_total,
                              filler_num_trial_yes, filler_num_trial_no, my_seed, exp_questioner]], 
    columns = ["exp_name", "exp_lan", "exp_num_trials", "locations", "num_location", "exp_num_of_items", # 0 1 2 3 4 5
               "exp_yes_to_no_ratio", "exp_num_trial_yes", # 6 7
               "exp_num_trial_no", "exp_num_of_control_for_each_item", # 8 9 
               "exp_num_of_correction_for_each_location_for_each_item", # 10 
               "item_num_trial_total", "item_num_trial_yes", "item_num_trial_no", #11 12 13
               "item_num_trial_for_each_item", "filler_num_trial_total", # 14 15 
               "filler_num_trial_yes", "filler_num_trial_no", "my_seed", "exp_questioner"]) # 16 17 18 19


    if iExp == 0:
        tAll_exps = tCur_exp
    else:
        tAll_exps = tAll_exps.append(tCur_exp)


    if iExp == 12:
        create_stimuli.create_stimuli(bCreate_stimuli, iExp,
                                      exp_name, exp_lan, exp_num_trials, locations, num_locations, exp_num_of_items,
                                      exp_yes_to_no_ratio, exp_num_trial_yes,
                                      exp_num_trial_no, exp_num_of_control_for_each_item,
                                      exp_num_of_correction_for_each_location_for_each_item,
                                      item_num_trial_total, item_num_trial_yes, item_num_trial_no,
                                      item_num_trial_for_each_item, filler_num_trial_total,
                                      filler_num_trial_yes, filler_num_trial_no, my_seed, exp_questioner)

tAll_exps.to_csv('tAll_exps.csv', encoding='utf-8', index=False)
