# dput(sort(unique()))
# Three navtive speaekers were asked to classifiy sex for these namees into Female (F), Male (M), and Ambiguous (A). For each name, if at least two people both chose F of M and the third one chose A, the name is put in the majority sex category, otherwise the name is discarded.

# In order to have the filler questions being the same indepdent of the correction condition, the "wrong" list which is the question list is the same acroos exps' on control trials, the correct version is the same as the "wrong" version -- the "wrong" is actaully correct.

import numpy as np
import pandas as pd
import create_stimuli


exps_names = ['exp0', 'exp1', 'exp2']
bCreate_stimuli = 1

positions = ['Agent', 'Verb', 'Patient']
num_positions = len(positions)
my_seed = [1, 1, 1, 5] # the four seeds are each for item, wrong filler verb, wrong filler agent, and wrong filler patient. again, "wrong". I lazily increment to the last until there is no repetition
#for iExp in [1]:
for iExp in range(len(exps_names)):
    exp_name = exps_names[iExp]
    exp_num_of_items = np.repeat(4, 3)[iExp]
    exp_yes_to_no_ratio = [1, 2, 0.5][iExp]
    exp_num_trials = np.repeat(72, 3)[iExp] #72 allows 1:2, 1:1, and 2:1 4 items and 2 trials each
    exp_num_of_correction_for_each_position_for_each_item = np.repeat(2, 3)[iExp]
    exp_num_of_control_for_each_item = exp_num_of_correction_for_each_position_for_each_item
    # exp_num_of_control_for_each_item = np.repeat(2, 3)[iExp]



    item_num_trial_yes = exp_num_of_items * exp_num_of_control_for_each_item
    item_num_trial_no = exp_num_of_items * exp_num_of_correction_for_each_position_for_each_item * num_positions
    item_num_trial_for_each_item = exp_num_of_control_for_each_item + exp_num_of_correction_for_each_position_for_each_item * num_positions
    item_num_trial_total = item_num_trial_yes + item_num_trial_no
    exp_num_trial_yes = int(exp_num_trials / (exp_yes_to_no_ratio + 1 ) * exp_yes_to_no_ratio)
    exp_num_trial_no = exp_num_trials - exp_num_trial_yes


    filler_num_trial_yes = exp_num_trial_yes - item_num_trial_yes
    filler_num_trial_no = exp_num_trial_no - item_num_trial_no
    filler_num_trial_total = filler_num_trial_yes + filler_num_trial_no


    tCur_exp = pd.DataFrame([[exp_name, exp_num_of_items, exp_yes_to_no_ratio, exp_num_trials, exp_num_trial_yes, exp_num_trial_no, exp_num_of_control_for_each_item, exp_num_of_correction_for_each_position_for_each_item, item_num_trial_total, item_num_trial_yes, item_num_trial_no, item_num_trial_for_each_item, filler_num_trial_total, filler_num_trial_yes, filler_num_trial_no, my_seed]], columns = ["exp_name", "exp_num_of_items", "exp_yes_to_no_ratio", "exp_num_trials", "exp_num_trial_yes", "exp_num_trial_no", "exp_num_of_control_for_each_item", "exp_num_of_correction_for_each_position_for_each_item", "item_num_trial_total", "item_num_trial_yes", "item_num_trial_no", "item_num_trial_for_each_item", "filler_num_trial_total", "filler_num_trial_yes", "filler_num_trial_no", "my_seed"])

    if iExp == 0:
        tAll_exps = tCur_exp
    else:
        tAll_exps = tAll_exps.append(tCur_exp)

    create_stimuli.create_stimuli(bCreate_stimuli, iExp, positions, num_positions, exp_name, exp_num_of_items, exp_yes_to_no_ratio, exp_num_trials, exp_num_trial_yes, exp_num_trial_no, exp_num_of_control_for_each_item, exp_num_of_correction_for_each_position_for_each_item, item_num_trial_total, item_num_trial_yes, item_num_trial_no, item_num_trial_for_each_item, filler_num_trial_total, filler_num_trial_yes, filler_num_trial_no, my_seed)

tAll_exps.to_csv('tAll_exps.csv', encoding='utf-8', index=False)
