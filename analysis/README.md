# processing
+ on tedlab, copy data from  `../ali26m/Experiment` to whereever they belong
  + e.g., `cp *exp4* ~/prosody_study_data/exp4/subject_responses_all/`
+ run `process_pipeline.sh` at stage 1 tutorial to copy data from tedlab to the local corresponding folder.
+ run `process_pipeline.sh` at stage 1 non-tutorial to filter data.
+ run `check_answer_audio_and_create_tTranscript.py`, which has two stages. 
+ run `process_survey_from_questiondata.Rmd` from the `[psiturk dir]/non-psiturk` R project. 
  + first, in psiturk do `download_datafiles` and `worker list --submitted --hit [hit id] >> worker.txt`
    + remove the worker file first 
  + you will then get `surveydata.csv` and `worker.csv` which are used in the next step. 
+ run `[psiturk dir]/non-psiturk/reject_hit.py`
  + you will get `hit_summary.csv` and `surveydata_corresponding_to_recording.csv`. 
  + go through the first csv to get a sense of how many couldn't get their data saved -- if this issue becomes too serious we need to enhance the pisutrk paradigm
  + go through the second csv to see their feedback -- should give people who spotted errors bonus. 
+ in psiturk, do `worker approve --hit [hit id]`
+ run `check_answer_audio_and_create_tTranscript.py` at multiple stages
  + heavy computing
+ run `process_pipeline.sh` at stage 2 for forced alignment and acoustic measurement. 
  + heavy computing
# analysis  
+ open Rproj `analysis`, knit `acoustic_analysis.Rmd`
