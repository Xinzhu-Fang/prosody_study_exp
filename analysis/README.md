# process data
+ on tedlab, copy data from  `../ali26m/Experiment` to whereever they belong
  + e.g., `cp *exp4* ~/prosody_study_data/exp4/subject_responses_all/`
+ run `process_pipeline.sh` at stage 1 tutorial to copy data from tedlab to the local corresponding folder.
  + specify `exp_id`
+ run `process_pipeline.sh` at stage 1 non-tutorial to filter data.
+ (you can process hit now but you shouldn't approve the hit until you have assessed the data quality in the next step)
+ run `check_answer_audio_and_create_tTranscript.py` at multiple stages
  + heavy computing
  + human labor
+ run `process_pipeline.sh` at stage 2 for forced alignment and acoustic measurement. 
  + heavy computing
# analyse data
+ open Rproj `analysis`, knit `acoustic_analysis.Rmd`
# approve hit
+ do `bash non-psiturk/process_hit.sh` in `../psiturk-prosody_study_exp0`
  + specify `exp_id` and `hit_id`
  + you will get `non-psiturk/hit_summary.csv`, `non-psiturk/surveydata_corresponding_to_recording.csv`, and `non-psiturk/surveydata.csv`. 
  + go through the first csv to get a sense of how many couldn't get their data properly saved -- if this issue becomes too 
serious we need to enhance the pisutrk paradigm.  
  + go through the second csv to see their feedback -- should give people who spotted errors bonus. 
  + [enhan]
+ in psiturk, do `mode`, do `worker approve --hit [hit id]`
  + have to be in live mode 
