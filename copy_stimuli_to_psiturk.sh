current_exp=exp5

mkdir $current_exp/audio

cp audio_for_exp1_to_6_01_10_20/responses_to_analyze/* $current_exp/audio/

psiturk_stimuli_dir=psiturk-prosody_study_exp0/static/stimuli
rm -r ../$psiturk_stimuli_dir/*
cp tAll_exps.csv  ../$psiturk_stimuli_dir

mkdir ../$psiturk_stimuli_dir/$current_exp

cp -r $current_exp/ ../$psiturk_stimuli_dir/$current_exp
