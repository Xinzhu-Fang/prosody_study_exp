# process data
+ on tedlab, copy data from  `../ali26m/Experiment` to whereever they belong
+ run `process_pipeline.sh` at stage 1 to copy data from tedlab to the local corresponding folder.
+ run `check_answer_audio_and_create_tTranscript.py`, which has two stages. 

+ open process_pipeline.sh, search for manual and make changes in those sections for yourself. Run the script `bash process_pipeline.sh`, you will be prompted to enter your tedlab server acct password to get some recordings from there, if you have data locally, search for alternative and follow the instruction in that section.
+ when in doubt, search for [note]
+ caveats:
  + There are currently 3044 wav files for nonrhyming_84total_60No_24Yes_20181210. The filly.txt there has only 1061 lines (e.g., subject A0629003TXZF828GVFIT is not included), why when you run the script some wav files are skipped.
  + I have a few hundreds recordings on tedlab.
