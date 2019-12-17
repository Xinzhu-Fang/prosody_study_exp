#run this file at two stages:
#    1: get the auto fail. Then enter the trial num to reject
#    2: remove the rejected trial to output the final tTranscript
# in number, select the row index holding cmd, copy to atom. Once done, repleace \r?\n\s*\n with \n
# and then https://discuss.atom.io/t/add-a-at-the-end-of-each-line/59492/4
#    3: find out if there is a speaker who was rejected a lot, probably not a native speaker, reject them
   
bTest = 0
#bTest = 1 # manual
bStage = 1
bStage = 2 #manual
bStage = 3 #manual
reject_row_index = [
620,
253,
415,
882,
171,
185,
746,
468,
956,
237,
471,
597,
455,
260,
958,
509,
801,
764,
156,
408,
430,
364,
699,
91,
585,
116,
811,
387,
967,
350,
969,
620,
253,
415,
882,
171,
185,
746,
468,
956,
237,
471,
597,
455,
260,
958,
509,
801,
764,
156,
408,
430,
364,
699,
91,
585,
116,
811,
387,
967,
350,
969,
528,
102,
46,
738,
315,
732,
940,
360,
635,
961,
176,
681,
622,
184,
675,
419,
900,
560,
310,
915,
90,
802,
349,
119,
809,
33,
43,
301,
741,
508,
731,
25,
314,
359,
637,
190,
887,
885,
540,
416,
7,
279,
470,
953,
752,
259,
175,
959,
684,
367,
814,
108,
165,
497,
582,
517,
798,
541,
103,
636,
177,
875,
327,
417,
181,
897,
294,
288,
673,
473,
879,
23,
966,
250,
248,
683,
945,
816,
112,
566,
580,
345,
649,
189,
99,
296,
524,
261,
31,
724,
511,
747,
37,
238,
890,
193,
400,
414,
881,
534,
164,
671,
815,
616,
821,
605,
449,
167,
109,
565,
581,
491,
100,
208,
794,
725,
274,
523,
497
] #manual
reject_worker_id = [
        'A1BQCRF5Q76YFY', #bad
        'A1AKL5YH9NLD2V', #broken exp
        ] #manual
bStrigent = 0
#bStrigent = 1 #manual
import pandas as pd
import os
import speech_recognition as sr

cur_exp = 'exp1'


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
            
            cur_worker = cur_file[67:len(cur_file)-42]
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
