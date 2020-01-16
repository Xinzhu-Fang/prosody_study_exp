# process data
+ on tedlab, copy data from  `../ali26m/Experiment` to whereever they belong
  + e.g., `cp *exp4* ~/prosody_study_data/exp4/subject_responses_all/`
+ run `process_pipeline.sh` at stage 1 tutorial to copy data from tedlab to the local corresponding folder.
+ run `process_pipeline.sh` at stage 1 non-tutorial to filter data.
+ run `check_answer_audio_and_create_tTranscript.py` at multiple stages
  + heavy computing
  + human labor
+ run `process_pipeline.sh` at stage 2 for forced alignment and acoustic measurement. 
  + heavy computing
# analyse data
+ open Rproj `analysis`, knit `acoustic_analysis.Rmd`
# approve hit
+ do `bash non-psiturk/process_hit.sh` in `../psiturk-prosody_study_exp0`
  + you will get `non-psiturk/hit_summary.csv` and `non-psiturk/surveydata_corresponding_to_recording.csv`. 
  + go through the first csv to get a sense of how many couldn't get their data properly saved -- if this issue becomes too 
serious we need to enhance the pisutrk paradigm
  + go through the second csv to see their feedback -- should give people who spotted errors bonus. 
+ do `psiturk worker approve --hit [hit id]`
