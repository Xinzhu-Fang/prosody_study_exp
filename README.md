## Task organization
+ See `tAll_Exps.csv` for experiments parameters
+ See `[exp name]/tAll_trials.csv` for trials parameters for each exp. Each exp dir has its own `image/`.

There are three English versions of this as of Nov, 2019: `exp0`, `exp1`, and `exp2`. The questions are the same across exps for all trials, the pictures and answers are the same across exps for all ITEM trials, but different for fillers trials depending on if we need more no or yes. For trials parameters, see
  + https://github.com/Xinzhu-Fang/prosody_study_exp/blob/master/exp0/tAll_trials.csv
  + https://github.com/Xinzhu-Fang/prosody_study_exp/blob/master/exp1/tAll_trials.csv
  + https://github.com/Xinzhu-Fang/prosody_study_exp/blob/master/exp2/tAll_trials.csv

## Task creation pipeline
+ use `word_manipulate.Rmd`to sort names, change cases, etc.
+ check the words you will use exist in the alignment model's dictionary with `check_words_in_model_dict.py`
+ use `create_exp.py` and `create_stimuli.py` to create all exps. 
+ `copy_stimuli_to_psiturk.sh`
+ 
+ I do automatic speech recognition and automatic phonetic segmentation for questions too, and use the results as "benchmark" for answers. 
+ must use python 3 for chinese versions





## Caution
presentationnum decides the order of presentation, the index in the recording name is not the presentationnum but the trial_id. The trials were shuffled. 

## enhancement
search for the enhan tag in my prosody study issue

## Languages we can cover human-wise
+ Saima speaks Spanish, Catalan, Koshur, Hindi/Urdu, and French
