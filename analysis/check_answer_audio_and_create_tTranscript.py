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
#bStage = 2 #manual
#bStage = 3 #manual
reject_row_index = [
882,
586,
877,
861,
221,
413,
559,
839,
924,
758,
771			,
790			,
795			,
612			,
538			,
1025			,
1013			,
362			,
295			,
275			,
327			,
775			,
814			,
1080			,
781			,
1092			,
577			,
607			,
662			,
800			,
761			,
469			,
724			,
637			,
126,
974,
935,
952,
840,
966,
833,
1009,
809,
271,
915,
957,
435,
965,
1019,
980,
999,
115,
713,
99,
690,
739,
491,
1079,
1065,
827,
1051,
36,
824,
25,
365,
697,
657,
524,
670,
1039,
1054,
31,
1024,
747,
43,
695,
374,
979,
625,
352,
162,
121,
98,
114,
82,
338,
421,
234,
584,
103,
111,
127,
971,
954,
245,
594,
143,
764,
831,
124,
936,
468,
1086,
951,
638,
841,
109,
728,
978,
968,
712,
916,
100,
472,
687,
963,
436,
955,
997,
982,
24,
35,
490,
742,
1082,
823,
816,
658,
1046,
1063,
1052,
32,
45,
1040,
525,
750,
1053,
616,
756,
694,
667,
1023,
1058,
553,
868,
414,
630,
206,
717,
1011,
890,
907,
187,
380,
858,
937,
560,
923,
842,
880,
588,
884,
412,
220,
201,
536,
1014,
788,
282,
296,
773,
363,
611,
755,
815,
272,
610,
837,
799,
286,
578,
1081,
779,
326,
1089,
783,
683,
929,
644,
144,
155,
195,
200,
235,
432,
217,
474,
507,
857,
873,
681,
430,
210,
72,
171,
509,
188,
893,
207,
101,
83,
119,
118,
116,
591,
981,
626,
964,
159,
347,
375,
246,
141,
108,
506,
967,
418,
410,
110,
345,
125,
593,
950,
29,
44,
395,
1041,
27,
61,
1076,
541,
318,
310,
574,
367,
250,
1064,
398,
23,
323,
10,
182,
40,
38,
573,
878,
645,
238,
859,
150,
219,
502,
478,
193,
142,
203,
84,
891,
76,
204,
680,
514,
169,
186,
427,
213,
2,
459,
486,
780,
798,
259,
273,
287,
294,
446,
699,
528,
67,
276,
281,
297,
943,
791,
772,
633,
1007,
20,
373,
550,
381,
189,
863,
892,
870,
909,
876,
379,
218,
411,
887,
856,
585,
563,
927,
838,
236,
151,
860,
684,
639,
222,
646,
341,
191,
879,
501,
140,
202,
475,
869,
889,
428,
185,
170,
516,
73,
205,
679,
284,
274,
4,
258,
784,
737,
456,
485,
801,
291,
8,








] #manual
reject_worker_id = [
'AWVIOLZUKBNV',    # 17 old man mumble
'A2YTQDLACTLIB',     #5 some resonance
'AFKB7F09OVKV'  ,   # 3 dropped out
'A15PUZKRWJH0E'  ,   #3 dropped out
'A3GITKS8VABUN'   ,  #2 dropped out
'A31DHCPF9VKR8'    ,# 1 no sound       
        
        ] #manual
bStrigent = 0
#bStrigent = 1 #manual
import pandas as pd
import os
import speech_recognition as sr

cur_exp = 'exp11'


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
