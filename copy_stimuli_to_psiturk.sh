current_exp=exp9
current_audio=audio_for_exp9_02_16_20

mkdir $current_exp/audio

cp $current_audio/responses_to_analyze/* $current_exp/audio/

psiturk_stimuli_dir=psiturk-prosody_study_exp0/static/stimuli
rm -r ../$psiturk_stimuli_dir/*
cp tAll_exps.csv  ../$psiturk_stimuli_dir

mkdir ../$psiturk_stimuli_dir/$current_exp

cp -r $current_exp/ ../$psiturk_stimuli_dir/$current_exp
