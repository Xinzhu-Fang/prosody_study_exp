## Task organization
+ See `tAll_Exps.csv` for experiments parameters
+ See `[exp name]/tAll_trials.csv` for trials parameters for each exp. Each exp dir has its own `image/`.

There are three English versions of this as of Nov, 2019: `exp0`, `exp1`, and `exp2`. The questions are the same across exps for all trials, the pictures and answers are the same across exps for all ITEM trials, but different for fillers trials depending on if we need more no or yes. For trials parameters, see
  + https://github.com/Xinzhu-Fang/prosody_study_exp/blob/a/exp0/tAll_trials.csv
  + https://github.com/Xinzhu-Fang/prosody_study_exp/blob/a/exp1/tAll_trials.csv
  + https://github.com/Xinzhu-Fang/prosody_study_exp/blob/a/exp2/tAll_trials.csv

## Task creation
+ use `word_manipulate.Rmd`to sort names and change their cases.
+ check the words you will use exist in the alignment model's dictionary with `check_words_in_model_dict.py`


## Caution
presentationnum decides the order of presentation, the index in the recording name is no presentationnum but trial_id. The trials were shuffled. 
