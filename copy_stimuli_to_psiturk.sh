# mkdir exp0/audio/
# mkdir exp1/audio/
# mkdir exp2/audio/
# mkdir exp3/audio/
# mkdir exp4/audio/
mkdir exp5/audio/
# mkdir exp6/audio/
# mkdir exp7/audio/
# mkdir exp8/audio/




# cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp0/audio/
# cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp1/audio/
# cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp2/audio/
# cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp3/audio/
# cp audio_for_exp1_to_6_01_10_20/responses_to_analyze/* exp4/audio/
cp audio_for_exp1_to_6_01_10_20/responses_to_analyze/* exp5/audio/


psiturk_stimuli_dir=psiturk-prosody_study_exp0/static/stimuli
rm -r ../$psiturk_stimuli_dir/*
cp tAll_exps.csv  ../$psiturk_dir
# mkdir ../$psiturk_dir/exp0
# mkdir ../$psiturk_dir/exp1
# mkdir ../$psiturk_dir/exp2
# mkdir ../$psiturk_dir/exp3
# mkdir ../$psiturk_dir/exp4
mkdir ../$psiturk_dir/exp5

# cp -r exp0/ ../$psiturk_dir/exp0
# cp -r exp1/ ../$psiturk_dir/exp1
# cp -r exp2/ ../$psiturk_dir/exp2
# cp -r exp3/ ../$psiturk_dir/exp3
# cp -r exp4/ ../$psiturk_dir/exp4
cp -r exp5/ ../$psiturk_dir/exp5
