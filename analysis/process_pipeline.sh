# This file contains two stages and a tuorial mode
# Piloting:  make head argument small like 10
#   stage 1 tutorial: tranfer data from server to local, prepare a few data to process
#   stage 2: process
#   stage 1 non-tutorial: prepare all data to process
#   stage 2: process
# Running on mturk with worker id:
#   stage 1 tutorial: tranfer data from server to local
#   stage 1 non-tutorial: prepare all data to process
#   stage 2: process
# Running with debug worker id: make head argument big like 100
#   stage 1 tutorial: tranfer data from server to local
#   stage 2: process
# Before stage 2 you need to run the check_answer.py file for further preparation

bTutorial_mode=1
# bTutorial_mode=0 #manual
bStage=1
bStage=2 # manual
current_exp=exp0

function make_dir(){
  if [ -d $@ ];
  then rm -Rf $@;
fi
mkdir $@
}

# # [note] in the most recent recordings from the dropbox folder shared by misha, there are two copies of the data because of the file naming thing, and other files helped perform this operation. To sift out wav file I need.
# find . ! -name "*.wav" -exec rm {} \;
# find . -name "* *" -exec rm {} \;



# [manual] specify paths here and make sure they all exist
my_praat_location=/Applications/Praat.app/Contents/MacOS/Praat
data_dir=/Users/xzfang/Desktop/prosody_study_data/


my_dropbox_location=/Users/xzfang/Dropbox\ \(MIT\)/Apps/mturk_recording/api-test


# stimuli_dir=/Users/xzfang/Github/stressTurk_tutorial/
# current_exp=nonrhyming_84total_60No_24Yes_20181210

# stimuli_dir=/Users/xzfang/Github/prosody_study_exp/

# current_exp=Ted
# current_exp=Cindy
#
# data_dir=/Users/xzfang/Github/prosody_study_exp/audio_for_exp0_to_exp2_11_04_19/
# stimuli_dir=/Users/xzfang/Github/prosody_study_exp/
#
# data_dir=/Users/xzfang/Github/prosody_study_exp/forced_alignment_sensitivity_test
# stimuli_dir=/Users/xzfang/Github/prosody_study_exp/forced_alignment_sensitivity_test

# tedlab_acct=xzfang
# scripts_acct=xzfang
##




current_data_dir=$data_dir$current_exp
# current_stimuli_dir=$stimuli_dir$current_exp

if [ $bStage == 1 ];
then
  # current_data_dir=$data_dir
  # current_stimuli_dir=$stimuli_dir
  echo You should always start with a few data, when tutorial mode if off, I assume you already got all the data
  if [ $bTutorial_mode == 1 ];
  then
    make_dir $current_data_dir
    make_dir $current_data_dir/subject_responses_all

    # scp -r $current_data_dir/subject_responses_all xzfang@tedlab.mit.edu:~/prosody_study_data/$current_exp/subject_responses_all
    # scp -r $tedlab_acct@tedlab.mit.edu:/home/xzfang/prosody_study_data/$current_exp/subject_responses_all $current_data_dir/
    # scp -r $scripts_acct@athena.dialup.mit.edu:/afs/athena.mit.edu/user/x/z/xzfang/web_scripts/data/*$current_exp*.wav $current_data_dir/subject_responses_all
    # scp -r $scripts_acct@bcs-prod-www-4.mit.edu:/var/www/html/tedlab/uploads/*$current_exp*.wav $current_data_dir/subject_responses_all
    # [Alternative] if already have the recordings locally, you can make_dir $current_data_dir/subject_responses_all, and move recordings to that folder. Remember to comment out the make_dir line above that you would have done yourself.
    # echo "$my_dropbox_location"/*$current_exp*.wav
    # cp "$my_dropbox_location"/*$current_exp*.wav $current_data_dir/subject_responses_all
    find "$my_dropbox_location" -name \*$current_exp*.wav -exec cp {} $current_data_dir/subject_responses_all \;
    # python remove_failed_attempts_of_recording_that_are_not_overwritten_in_dropbox.py $current_data_dir/subject_responses_all

  fi

  echo Sift out filler, debug, and empty .wav files
  make_dir $current_data_dir/responses_to_analyze
  if [ $bTutorial_mode == 1 ];
  then
    echo for tutorial, move the first 10 files in _all dir to _partial dir, and work from the _partial dir
    make_dir $current_data_dir/subject_responses_partial
    for file in $(ls $current_data_dir/subject_responses_all | head -10000)
    do
      cp  $current_data_dir/subject_responses_all/$file $current_data_dir/subject_responses_partial/
    done
  # [open] I said skip ., don't why they still try to remove the dir. You will see this innocuous but humiliating warning:
  # cp: /Users/xzfang/Desktop/prosody_study_data/nonrhyming_84total_60No_24Yes_20181210/subject_responses_all is a directory (not copied).
    # find $current_data_dir/subject_responses_partial ! \( -name \*Filler*.wav -o -name debug*.wav -o -name . \) -size +44 -exec cp {} $current_data_dir/responses_to_analyze \;
    find $current_data_dir/subject_responses_partial ! \( -name \*Filler*.wav -o -name . \) -size +44 -exec cp {} $current_data_dir/responses_to_analyze \;
  else
    find $current_data_dir/subject_responses_all ! \( -name \*Filler*.wav -o -name debug*.wav -o -name . \) -size +44 -exec cp {} $current_data_dir/responses_to_analyze \;
  fi

else


  echo Downsampling
  make_dir $current_data_dir/responses_to_analyze_downsampled
  # python downsampler.py $current_data_dir/responses_to_analyze $current_data_dir/responses_to_analyze_downsampled
  python downsampler.py tTranscript_$current_exp.csv

  echo Forced alignment
  make_dir $current_data_dir/responses_to_analyze_textgrid
  # python align1.py $current_data_dir/responses_to_analyze_downsampledtTranscript_$current_exp.csv $current_data_dir/responses_to_analyze_textgrid
  python p2fa_mandarin/align1.py tTranscript_$current_exp.csv

  echo Computing dependent variables
  # http://www.fon.hum.uva.nl/praat/manual/Scripting_6_9__Calling_from_the_command_line.html
  $my_praat_location --run 0_extractAcoustics_woi.praat measure_$current_exp $current_data_dir/responses_to_analyze_downsampled/ $current_data_dir/responses_to_analyze_textgrid/ 1 2 2 ","

  echo see output file measure_$current_exp in the same dir as this file
fi
