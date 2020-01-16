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
86, 
644, 
347, 
586, 
610, 
412, 
710, 
37, 
674, 
151, 
771, 
474, 
468, 
749, 
440, 
220, 
16, 
139, 
288, 
142, 
633, 
585, 
920, 
505, 
55, 
724, 
312, 
126, 
544, 
123, 
187, 
485, 
426, 
282, 
692, 
554, 
518, 
196, 
698, 
820, 
394, 
798, 
358, 
582, 
143, 
361, 
122, 
128, 
831, 
341, 
545, 
484, 
183, 
521, 
571, 
883, 
722, 
742, 
535, 
611, 
643, 
87, 
411, 
711, 
438, 
671, 
242, 
19, 
858, 
300, 
594, 
617, 
255, 
374, 
634, 
534, 
870, 
877, 
314, 
114, 
818, 
393, 
805, 
800, 
359, 
23, 
744, 
423, 
456, 
592, 
246, 
862, 
857, 
297, 
833, 
878, 
137, 
536, 
560, 
335, 
638, 
717, 
271, 
323, 
476, 
929, 
924, 
466, 
334, 
233, 
914, 
529, 
441, 
48, 
66, 
74, 
608, 
712, 
372, 
446, 
90, 
351, 
646, 
854, 
416, 
379, 
298, 
590, 
863, 
333, 
538, 
782, 
373, 
475, 
274, 
406, 
926, 
928



] #manual
reject_worker_id = [
        'A2SYTRKH1JWJO5',
        'A2B4GWF7MF7AOB',
        'A1L09S3NEEE0GW',
        'AXKTYKCT9NGHS',
        'A19IJGQM429LMC',
        'AOHKDHUX8XL5I',
        'A39KUEDR8ZS1CF',
        'A2ASTDMWBCFIP0',
        'A21Q7FCKM86VL8',
        
        
        ] #manual
bStrigent = 0
#bStrigent = 1 #manual
import pandas as pd
import os
import speech_recognition as sr

cur_exp = 'exp5'


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
