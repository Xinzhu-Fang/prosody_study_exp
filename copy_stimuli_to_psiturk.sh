current_exp=exp14
current_audio=audio_for_exp14_06_19_20

mkdir $current_exp/audio

cp $current_audio/responses_to_analyze/* $current_exp/audio/

psiturk_stimuli_dir=psiturk-prosody_study_exp0/static/stimuli
rm -r ../$psiturk_stimuli_dir/*
cp tAll_exps.csv  ../$psiturk_stimuli_dir

mkdir ../$psiturk_stimuli_dir/$current_exp

cp -r $current_exp/ ../$psiturk_stimuli_dir/$current_exp
