current_data_dir=/Users/xzfang/Github/prosody_study_exp/audio_for_exp14_06_19_20

mfa_dir=/Users/xzfang/Desktop/montreal-forced-aligner
my_praat_location=/Applications/Praat.app/Contents/MacOS/Praat


function make_dir(){
  if [ -d $@ ];
  then rm -Rf $@;
fi
mkdir $@
}

echo Forced alignment

make_dir $current_data_dir/responses_to_analyze_mfa

python prepare_files_for_mfa.py $current_data_dir/tAll_questions.csv $current_data_dir/responses_to_analyze $current_data_dir/responses_to_analyze_mfa

$mfa_dir/bin/mfa_generate_dictionary/ $mfa_dir/spanish_g2p.zip $current_data_dir/responses_to_analyze_mfa $current_data_dir/spanish_dict.txt

make_dir $current_data_dir/responses_to_analyze_textgrid

# bin/mfa_generate_dictionary/ spanish_g2p.zip sample_spanish_wav/ sample_spanish_dict.txt
#
# bin/mfa_align sample_spanish_wav sample_spanish_dict.txt pretrained_models/spanish.zip output

$mfa_dir/bin/mfa_align $current_data_dir/responses_to_analyze_mfa $current_data_dir/spanish_dict.txt $mfa_dir/pretrained_models/spanish.zip $current_data_dir/responses_to_analyze_textgrid

echo Computing dependent variables
# http://www.fon.hum.uva.nl/praat/manual/Scripting_6_9__Calling_from_the_command_line.html
$my_praat_location --run 0_extractAcoustics_woi.praat measure_$current_exp $current_data_dir/responses_to_analyze_downsampled/ $current_data_dir/responses_to_analyze_textgrid/ 1 2 2 ","

echo see output file measure_$current_exp in the same dir as this file
