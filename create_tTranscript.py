import  numpy as np
#This is for audio
cur_exp = 'exp0'
tAll_trials = pd.read_csv(os.path.join(cur_exp, 'tAll_trials.csv'))
tTranscript = tAll_trials[['question_file', 'question_script']]
#tTranscript['question_textgrid'] = tTranscript.question_file.replace({'m4a', 'TextGrid'}, regex=True)
tTranscript['question_textgrid'] = [a.replace('m4a', 'TextGrid') for a in tTranscript.question_file]
tTranscript['question_file'] = [a.replace('m4a', 'wav') for a in tTranscript.question_file]
#np.savetxt(r'filley.txt', tTranscript.values)
tTranscript.to_csv('filey.txt', encoding='utf-8', index=False, header=False)
