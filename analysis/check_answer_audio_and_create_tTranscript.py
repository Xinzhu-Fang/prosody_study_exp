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
495,
731,
134,
873,
87,
44,
99,
289,
412,
439,
806,
426,
216,
147,
954,
368,
271,
171,
701,
281,
857,
277,
133,
363,
394,
503,
276,
710,
85,
432,
67,
157,
357,
729,
790,
294,
123,
548,
852,
118,
687,
18,
220,
1022,
283,
172,
512,
484,
288,
149,
337,
656,
351,
115,
905,
185,
789,
267,
198,
465,
298,
605,
811,
181,
823,
673,
694,
366,
42,
121,
11,
169,
442,
906,
37,
354,
449,
164,
345,
506,
633,
292,
1001,
419,
816,
663,
139,
568,
170,
453,
843,
615,
941,
897,
664,
200,
966,
989,
502,
911,
251,
916,
609,
697,
990,
761,
254,
894,
100,
691,
587,
467,
667,
959,
1025,
818,
915,
601,
204,
110,
290,
685,
558,
719,
487,
32,
378,
861,
76,
1010,
536,
848,
825,
444,
350,
71,
97,
287,
229,
947,
896,
688,
594,
1020,
918,
675,










] #manual copy to reject index file, these will be replaced
reject_worker_id = [
       'APORXBJ0D4CMZ', # 8 hz
'AXKVHJHF1EOVT',#     20 noise
'A37AWU2VH1ZIXX',#     20 button sound
'A1969Q0R4Y0E3J',#     19 button sound at start
'A1B5O1E2T429ET',#     16 some missing
'AJM4334V07JDQ',#      13 some silent
'AU9LWTQSNY73',#        6 old male horse voice, data missing
'A1DD23J1WBGQUU',#     3 returned hit
        ] #manual
bStrigent = 0
#bStrigent = 1 #manual
import pandas as pd
import os
import speech_recognition as sr

cur_exp = 'exp12'


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
            
#            for like exp4, worker id should start at the 67th, and ends at len(cur_file)-43:
#            cur_worker = cur_file[67:len(cur_file)-43]
            cur_worker = cur_file[(63+len(cur_exp)): (len(cur_file)-len(cur_exp)-39)]
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
            tTranscript1 = tTranscript0[~tTranscript0.worker_id.isin(reject_worker_id)]
                    
    else:
        tTranscript0 = tTranscript_auto_pass    
    
    
    

    tTranscript2 = tTranscript1[['trial_id', 'supposed_answer_transcript', 'answer_files']]
    tTranscript2['answer_textgrid'] = [a.replace('wav', 'TextGrid') for a in tTranscript2.answer_files]
    tTranscript2['answer_downsampled'] = tTranscript2['answer_files']
    tTranscript2['answer_downsampled'] = [a.replace('responses_to_analyze', 'responses_to_analyze_downsampled') for a in tTranscript2.answer_downsampled]
    tTranscript2['answer_textgrid'] = [a.replace('responses_to_analyze', 'responses_to_analyze_textgrid') for a in tTranscript2.answer_textgrid]
    tTranscript2['supposed_answer_transcript'] = [a.replace('Kimmy', 'Kimmey') for a in tTranscript2.supposed_answer_transcript]
    
        
    
    tTranscript2.to_csv('tTranscript_' + cur_exp + '.csv',  encoding='utf-8')
