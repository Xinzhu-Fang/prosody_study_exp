# mkdir exp0/audio/
# mkdir exp1/audio/
# mkdir exp2/audio/
#
# cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp0/audio/
# cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp1/audio/
# cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp2/audio/

psiturk_dir=psiturk-prosody_study_exp0/static/stimuli
rm -r ../$psiturk_dir/*
mkdir ../$psiturk_dir/exp0
mkdir ../$psiturk_dir/exp1
mkdir ../$psiturk_dir/exp2
cp -r exp0/ ../$psiturk_dir/exp0
cp -r exp1/ ../$psiturk_dir/exp1
cp -r exp2/ ../$psiturk_dir/exp2
cp tAll_exps.csv  ../$psiturk_dir
