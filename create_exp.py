# dput(sort(unique()))
# Three navtive speaekers were asked to classifiy sex for these namees. For each name, if at least two people both chose F, M, or A and the last chose A, the name is put in the majority category, otherwise the name is put in that ambiguous.
import numpy as np
import pandas as pd

positions = ['Agent', 'Verb', 'Patient']
num_positions = len(positions)


exps_names = ['exp0', 'exp1', 'exp2']

for iExp in range(len(exps_names)):
    exp_name = exps_names[iExp]
    exp_num_of_items = np.repeat(4, 3)[iExp]
    exp_yes_to_no_ratio = [1, 2, 0.5][iExp]
    exp_num_trials = np.repeat(72, 3)[iExp] #72 allows 1:2, 1:1, and 2:1 4 items and 2 trials each
    exp_num_of_correction_for_each_position_for_each_item = np.repeat(2, 3)[iExp]
    exp_num_of_control_for_each_item = np.repeat(2, 3)[iExp]



    item_num_trial_yes = exp_num_of_items * exp_num_of_control_for_each_item
    item_num_trial_no = exp_num_of_items * exp_num_of_correction_for_each_position_for_each_item * num_positions
    item_num_trial_for_each_item = exp_num_of_control_for_each_item + exp_num_of_correction_for_each_position_for_each_item * num_positions
    item_num_trial_total = item_num_trial_yes + item_num_trial_no
    exp_num_trial_yes = int(exp_num_trials / (exp_yes_to_no_ratio + 1 ) * exp_yes_to_no_ratio)
    exp_num_trial_no = exp_num_trials - exp_num_trial_yes


    filler_num_trial_yes = exp_num_trial_yes - item_num_trial_yes
    filler_num_trial_no = exp_num_trial_no - item_num_trial_no
    filler_num_trial_total = filler_num_trial_yes + filler_num_trial_no
    filler_id0 = ["{:02d}".format(i) for i in range(1, filler_num_trial_total + 1)]
    filler_id = ["filler_" + i for i in filler_id0]

    tCur_exp = pd.DataFrame([[exp_name, exp_num_of_items, exp_yes_to_no_ratio, exp_num_trials, exp_num_trial_yes, exp_num_trial_no, exp_num_of_control_for_each_item, exp_num_of_correction_for_each_position_for_each_item, item_num_trial_total, item_num_trial_yes, item_num_trial_no, item_num_trial_for_each_item, filler_num_trial_total, filler_num_trial_yes, filler_num_trial_no]], columns = ["exp_name", "exp_num_of_items", "exp_yes_to_no_ratio", "exp_num_trials", "exp_num_trial_yes", "exp_num_trial_no", "exp_num_of_control_for_each_item", "exp_num_of_correction_for_each_position_for_each_item", "item_num_trial_total", "item_num_trial_yes", "item_num_trial_no", "item_num_trial_for_each_item", "filler_num_trial_total", "filler_num_trial_yes", "filler_num_trial_no"])

    if iExp == 0:
        tAll_exps = tCur_exp
    else:
        tAll_exps = tAll_exps.append(tCur_exp)

    create_stimuli(iExp, exp_name, exp_num_of_items, exp_yes_to_no_ratio, exp_num_trials, exp_num_trial_yes, exp_num_trial_no, exp_num_of_control_for_each_item, exp_num_of_correction_for_each_position_for_each_item, item_num_trial_total, item_num_trial_yes, item_num_trial_no, item_num_trial_for_each_item, filler_num_trial_total, filler_num_trial_yes, filler_num_trial_no)

tAll_exps.to_csv('tAll_exps.csv', encoding='utf-8', index=False)
