## Task organization
+ See `tAll_Exps.csv` for experiments parameters
+ See `[exp name]/tAll_trials.csv` for trials parameters for each exp. Each exp dir has its own `image/`.

## Task creation pipeline
+ use `word_manipulate.Rmd`to sort names, change cases, etc.
+ check the words you will use exist in the alignment model's dictionary with `check_words_in_model_dict.py`
+ use `create_exp.py` and `create_stimuli.py` to create all exps. 
+ `copy_stimuli_to_psiturk.sh`
+ must use python 3 for creating chinese versions. p2fa required pythong 2. 





## Caution
presentationnum decides the order of presentation, the index in the recording name is not the presentationnum but the trial_id. The trials were shuffled. 

## enhancement
search for the enhan tag in my prosody study issue
upsample 8hz occasional recording to 16 hz, most are 48hz


