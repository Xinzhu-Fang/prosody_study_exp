#run this file at two stages:
#    1: get the auto fail. Then enter the trial num to reject
#    2: remove the rejected trial to output the final tTranscript
# in number, select the row index holding cmd, copy to atom. Once done, repleace \r?\n\s*\n with \n
# and then https://discuss.atom.io/t/add-a-at-the-end-of-each-line/59492/4
bTest = 0
#bTest = 1 # manual
bStage = 1
bStage = 2 #manual
reject_row_index = [620,
253,
532,
110,
151,
415,
882,
380,
984,
836,
8,
171,
358,
73,
918,
719,
185,
746,
670,
468,
410,
956,
237,
471,
597,
618,
28,
722,
455,
133,
404,
260,
851,
535,
638,
558,
548,
686,
958,
906,
509,
801,
331,
764,
156,
223,
946,
922,
561,
408,
430,
690,
364,
699,
363,
91,
895,
275,
585,
307,
656,
526,
201,
847,
116,
34,
811,
69,
387,
967,
350,
300,
602,
303,
969,
583,
528,
102,
269,
209,
52,
46,
614,
255,
738,
312,
24,
487,
315,
845,
641,
732,
940,
693,
654,
360,
507,
233,
635,
633,
961,
396,
338,
330,
176,
861,
681,
454,
323,
870,
283,
622,
804,
184,
419,
900,
560,
365,
510,
432,
310,
222,
868,
915,
153,
182,
90,
802,
178,
349,
119,
809,
854,
33,
304,
973,
355,
43,
584,
603,
301,
302,
741,
562,
941,
508,
731,
25,
590,
865,
279,
469,
470,
953,
917,
752,
639,
705,
456,
259,
175,
820,
684,
367,
814,
564,
144,
165,
49,
497,
319,
582,
517,
19,
798,
927,
541,
295,
347,
192,
214,
103,
800,
636,
177,
678,
875,
962,
708,
85,
134,
327,
398,
417,
181,
897,
72,
546,
294,
288,
757,
418,
673,
336,
473,
879,
838,
23,
343,
966,
250,
627,
891,
248,
683,
945,
816,
112,
566,
437,
580,
207,
345,
216,
629,
795,
649,
736,
189,
489,
99,
296,
524,
807,
277,
853,
31,
724,
676,
511,
318,
747,
37,
754,
805,
264,
238,
265,
890,
193,
400,
492,
59,
245,
776,
459,
101,
356,
414,
378,
9,
881,
942,
988,
728,
534,
164,
671,
815,
592,
835,
107,
95,
616,
82,
543,
821,
605,
449,
141,
369,
167,
109,
565,
20,
783,
581,
215,
491,
100,
651,
208,
794,
478,
725,
274,
258,
523,
434,
30,
575,
282,
] #manual
reject_worker_id = [] #manual
bStrigent = 0
#bStrigent = 1 #manual
import pandas as pd
import os
import speech_recognition as sr

if bStage == 1:
    cur_exp = 'exp1'
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

    tTranscript = pd.DataFrame(zip(trial_id, worker_id ,supposed_answer_transcript, auto_transcript, status, answer_files), columns=['trial_id', 'worker_id', 'supposed_answer_transcript', 'auto_transcript', 'status', 'answer_files'])

    tTranscript = tTranscript.sort_values(['trial_id'], ascending=True)
    
    tTranscript_auto_fail = tTranscript.loc[tTranscript.status == 'auto_fail']
    
    tTranscript_auto_pass= tTranscript.loc[tTranscript.status == 'auto_pass']
    
    tTranscript_auto_fail.to_csv('tTranscript_auto_fail_only_' + cur_exp + '.csv',  encoding='utf-8')
    tTranscript.to_csv('tTranscript_all_' + cur_exp + '.csv',  encoding='utf-8')

    

else:

    if bStrigent == 0:
        if reject_row_index != []:
            tTranscript0 = tTranscript.drop(reject_row_index)
        if reject_worker_id != []:
            tTranscript0 = tTranscript0[tTranscript0.worker_id not in reject_worker_id]
    else:
        tTranscript0 = tTranscript_auto_pass
    
    tTranscript1 = tTranscript0[['trial_id', 'supposed_answer_transcript', 'answer_files']]
    tTranscript1['answer_textgrid'] = [a.replace('wav', 'TextGrid') for a in tTranscript1.answer_files]
    tTranscript1['answer_downsampled'] = tTranscript1['answer_files']
    tTranscript1['answer_downsampled'] = [a.replace('responses_to_analyze', 'responses_to_analyze_downsampled') for a in tTranscript1.answer_downsampled]
    tTranscript1['answer_textgrid'] = [a.replace('responses_to_analyze', 'responses_to_analyze_textgrid') for a in tTranscript1.answer_textgrid]
    tTranscript1['supposed_answer_transcript'] = [a.replace('Kimmy', 'Kimmey') for a in tTranscript1.supposed_answer_transcript]
    
        

    tTranscript1.to_csv('tTranscript_' + cur_exp + '.csv',  encoding='utf-8')
