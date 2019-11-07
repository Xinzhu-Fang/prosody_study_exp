mkdir exp0/audio/
mkdir exp1/audio/
mkdir exp2/audio/

cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp0/audio/
cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp1/audio/
cp audio_for_exp0_to_exp2_11_04_19/responses_to_analyze/* exp2/audio/

psiturk_dir=psiturk-prosody_study_exp0/static/stimuli
cp -r exp0/ ../$psiturk_dir
cp -r exp1/ ../$psiturk_dir
cp -r exp2/ ../$psiturk_dir
cp tAll_exps.csv ../$psiturk_dir
