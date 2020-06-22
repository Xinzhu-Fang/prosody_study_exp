current_data_dir=/Users/xzfang/Github/prosody_study_exp/audio_for_exp14_06_19_20

mfa_dir=/Users/xzfang/Desktop/montreal-forced-aligner


function make_dir(){
  if [ -d $@ ];
  then rm -Rf $@;
fi
mkdir $@
}

make_dir $current_data_dir/responses_to_analyze_mfa

python prepare_files_for_mfa.py $current_data_dir/tAll_questions.csv $current_data_dir/responses_to_analyze $current_data_dir/responses_to_analyze_mfa

$mfa_dir/bin/mfa_generate_dictionary/ $mfa_dir/spanish_g2p.zip $current_data_dir/responses_to_analyze_mfa $current_data_dir/spanish_dict.txt

make_dir $current_data_dir/responses_to_analyze_textgrid

# bin/mfa_generate_dictionary/ spanish_g2p.zip sample_spanish_wav/ sample_spanish_dict.txt
#
# bin/mfa_align sample_spanish_wav sample_spanish_dict.txt pretrained_models/spanish.zip output

$mfa_dir/bin/mfa_align $current_data_dir/responses_to_analyze_mfa $current_data_dir/spanish_dict.txt $mfa_dir/pretrained_models/spanish.zip $current_data_dir/responses_to_analyze_textgrid
