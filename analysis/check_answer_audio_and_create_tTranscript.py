#run this file at three stages:
#    1: get the auto fail. Then enter the trial num to reject
#    2: remove the rejected trial to output the final tTranscript
# in number, select the row index by holding cmd, copy to atom. Once done, repleace \r?\n\s*\n with \n
# and then https://discuss.atom.io/t/add-a-at-the-end-of-each-line/59492/4. Save the file as [exp_id]_reject_index.py, and save notes to there too. 
#    3: find out if there is a speaker who has only a few trials, exclude them, there are two reasons behind this:
# one is that they were rejected a lot, probably not a native speaker
# the other is that there were not many files which could be caused by that 1) this person sent empty data, 2)most of this person's data
# was not succefully transmitted, 3) this person returned the hit. 
bTest = 0
#bTest = 1 # manual
bStage = 1
bStage = 2 #manual
bStage = 3 #manual
reject_row_index = [
215,
223,
475,
558,
274,
288,
521,
520,
584,
317,
622,
301,
36,
375,
624,
500,
419,
156,
633,
201,
416,
634,
643,
597,
629,
135,
146,
158,
357,
609,
127,
358,
98,
606,
452,
539,
2,
238,
468,
8,
237,
488,
11,
493,
632,
418,
165,
155,
102,
621,
635,
417,
202,
145,
356,
608,
607,
163,
99,
359,
598,
559,
259,
471,
234,
557,
552,
474,
214,
522,
582,
275,
285,
346,
583,
592,
519,
316,
176,
439,
81,
331,
89,
381,
181,
80,
396,
455,
9,
239,
490,
10,
236,
38,
33,
540,
295,
483,
296,
32,
502,
82,
177,
442,
23,
413,
79,
180,
397,
393,
352,
330,
47,
55,
123,
382,
57,
66,
122,
261,
472,
560,
473,
212,
556,
83,
443,
91,
178,
392,
412,
78,
179,
71,
56,
46,
333,
614,
124,






] #manual
reject_worker_id = [
'A3KS8NN4LZ0L4W'
        
        
        ] #manual
bStrigent = 0
#bStrigent = 1 #manual
import pandas as pd
import os
import speech_recognition as sr

cur_exp = 'exp8'


if bStage == 1:
    tAll_trials = pd.read_csv(os.path.join('..', cur_exp, 'tAll_trials.csv'))

    supposed_answer_transcript = []
    auto_transcript = []
    status = []
    trial_id = []
    answer_files = []
    worker_id = []
    for iFile in os.listdir(os.path.join('/Users/xzfang/Desktop/prosody_study_data', cur_exp, 'responses_to_analyze')):
        #    print(cur_file)
        if bTest and len(status)> 10:
            break
        
        cur_file = os.path.join('/Users/xzfang/Desktop/prosody_study_data', cur_exp, 'responses_to_analyze', iFile)
        cur_trial = int(cur_file[len(cur_file) - 6: len(cur_file) - 4])
        if cur_trial < 33:
            
            cur_worker = cur_file[67:len(cur_file)-43]
            print(cur_trial)
            trial_id = trial_id + [cur_trial]
            worker_id = worker_id + [cur_worker]
            supposed_answer_transcript = supposed_answer_transcript + [str(x) for x in tAll_trials.loc[tAll_trials.trial_id == cur_trial, 'answer_script']]
            answer_files = answer_files + [cur_file]
            AUDIO_FILE = cur_file
            # use the audio file as the audio source
            r = sr.Recognizer()
            with sr.AudioFile(AUDIO_FILE) as source:
                audio = r.record(source)  # read the entire audio file
                # recognize speech using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                script = r.recognize_google(audio)
                auto_transcript = auto_transcript + [script]
    
                if script != tAll_trials.loc[tAll_trials.trial_id == cur_trial, 'answer_script'].any():
            #                print(iRow.question_file + ' is fine')
            #            else:
            #                print('check file ' + )
                    status = status + ['auto_fail']
                    print('fail')
                else:
                    status = status + ['auto_pass']
                    print('pass')
    
        # question_files = question_files + [  dquestion_file]
        #                print(iRow.question_file + 'recognized as' + script)
        # print("Google Speech Recognition thinks you said " + )
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                auto_transcript = auto_transcript + ['NA']
                status = status + ['auto_fail']
            except sr.RequestError as e:
                print("Could not request result from Google Speech Recognition service; {0}".format(e))
                auto_transcript = auto_transcript + ['NA']
                status = status + ['auto_fail']
    tTranscript = pd.DataFrame(zip(trial_id, worker_id ,supposed_answer_transcript, auto_transcript, status, answer_files), columns=['trial_id', 'worker_id', 'supposed_answer_transcript', 'auto_transcript', 'status', 'answer_files'])

    tTranscript = tTranscript.sort_values(['trial_id'], ascending=True)
    
    tTranscript_auto_fail = tTranscript.loc[tTranscript.status == 'auto_fail']
    
    tTranscript_auto_pass= tTranscript.loc[tTranscript.status == 'auto_pass']
    
    tTranscript_auto_fail.to_csv('tTranscript_auto_fail_only_' + cur_exp + '.csv',  encoding='utf-8')
    tTranscript.to_csv('tTranscript_all_' + cur_exp + '.csv',  encoding='utf-8')

    
elif bStage == 2: 

    tTranscript = pd.read_csv('tTranscript_all_' + cur_exp + '.csv', index_col=0)    

    if bStrigent == 0:
        if reject_row_index != []:
            tTranscript0 = tTranscript.drop(reject_row_index)
#        if reject_worker_id != []:
#            tTranscript0 = tTranscript0[tTranscript0.worker_id not in reject_worker_id]
    else:
        tTranscript0 = tTranscript_auto_pass
    
    print(tTranscript0.worker_id.value_counts())
    print(len(tTranscript0.worker_id.value_counts()))
else:
    
    if bStrigent == 0:
#        if reject_row_index != []:
#            tTranscript0 = tTranscript.drop(reject_row_index)
        if reject_worker_id != []:
            tTranscript0 = tTranscript0[~tTranscript0.worker_id.isin(reject_worker_id)]
                    
    else:
        tTranscript0 = tTranscript_auto_pass    
    
    
    
    tTranscript1 = tTranscript0[['trial_id', 'supposed_answer_transcript', 'answer_files']]
    tTranscript1['answer_textgrid'] = [a.replace('wav', 'TextGrid') for a in tTranscript1.answer_files]
    tTranscript1['answer_downsampled'] = tTranscript1['answer_files']
    tTranscript1['answer_downsampled'] = [a.replace('responses_to_analyze', 'responses_to_analyze_downsampled') for a in tTranscript1.answer_downsampled]
    tTranscript1['answer_textgrid'] = [a.replace('responses_to_analyze', 'responses_to_analyze_textgrid') for a in tTranscript1.answer_textgrid]
    tTranscript1['supposed_answer_transcript'] = [a.replace('Kimmy', 'Kimmey') for a in tTranscript1.supposed_answer_transcript]
    
        

    tTranscript1.to_csv('tTranscript_' + cur_exp + '.csv',  encoding='utf-8')
