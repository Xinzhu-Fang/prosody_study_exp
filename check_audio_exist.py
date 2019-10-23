import pandas as pd
import os

cur_exp = 'exp0'
audio_dir = 'audio'
tAll_trials = pd.read_csv(ps.path.join(cur_exp, 'tAll_trials.csv'))
for iAudio in tAll_trials.question_file:
    if not os.path.isfile(os.path.join(audio_dir, iAudio)):
        print("we still need " + iAudio)
