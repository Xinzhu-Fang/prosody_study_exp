## Task organization
+ See `tAll_Exps.csv` for experiments parameters
+ See `[exp name]/tAll_trials.csv` for trials parameters for each exp. Each exp dir has its own `image/` and `audio/`.

## Task creation pipeline (python3 by default)
+ use `word_manipulate.Rmd`to sort names, change cases, etc.
+ check the words you will use exist in the alignment model's dictionary with `check_words_in_model_dict.py`
+ `create_exp.py` calls `create_stimuli.py` to create all exps conditions and images 
  + human questioners
    + `find_questions_needed.py`
    + `check_question_audio_py2.py` check they exist and are correct
  + computer questioners
    + `create_audio_for_questions.py` uses gTTS 
    + `create_audio_for_questions_py2.py` uses eSpeak
+ `copy_stimuli_to_psiturk.sh`
  + specify `exp_id`
+ in psiturk, specify `exp_ind`, in `task.js`, switch `bTestMode` as needed to test locally
  + language versions have to be manully specified for default, ad, and consent.
+ create hit, should copy `hit_id` to `non-psiturk/process_hit.sh` to save time for analysis. 

## analysis (python2 by default)
see `analysis/README.md`

## psiturk 
* on mturk, the first page shown is ad ASSIGNMENT_ID_NOT_AVAILABLE part, when they accept the hit, it goes to ad else part, then consent.
* if go to heroku directly, the first page shown is default, then ad else part.

## Caution
+ presentationnum decides the order of presentation, the index in the recording name is not the presentationnum but the trial_id. The trials were shuffled. 
+ task creation requires python 3 becuase of painting chinese character. analysis requires python 2 because of p2fa. 

## enhancement
+ search for the enhan tag in my prosody study issue
+ upsample 8hz occasional recording to 16 hz, most are 48hz
+ demo at the end


