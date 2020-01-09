#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:55:10 2020

@author: xzfang
"""
import numpy as np
import pandas as pd
import os

exps_names = ['exp1', 'exp2', 'exp3', 'exp4', 'exp5', 'exp6']
num_exp = len(exps_names)

first_exp = 1
for iExp in exps_names:
    iAll_trials = pd.read_csv(os.path.join(iExp, 'tAll_trials.csv'))
    if first_exp:
        tAll_exp_trials = iAll_trials
        first_exp = 0
    else:
        tAll_exp_trials = tAll_exp_trials.append(iAll_trials)
    print(iExp)
    print(len(tAll_exp_trials.question_file.unique()))


questions = tAll_exp_trials.question_file.unique()

tQuestions = pd.DataFrame({'question_file':questions})

tQuestions.to_csv('questions_ted_needs_to_make_for_exp1to6_jan_2020.csv')