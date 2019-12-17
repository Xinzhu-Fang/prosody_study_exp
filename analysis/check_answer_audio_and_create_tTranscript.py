#run this file at two stages:
#    1: get the auto fail. Then enter the trial num to reject
#    2: remove the rejected trial to output the final tTranscript
# in number, select the row index holding cmd, copy to atom. Once done, repleace \r?\n\s*\n with \n
# and then https://discuss.atom.io/t/add-a-at-the-end-of-each-line/59492/4
bTest = 0
#bTest = 1 # manual
bStage = 1
bStage = 2 #manual
reject_row_index = [
138,
547,
180,
839,
17,
332,
86,
582,
575,
199,
277,
902,
11,
103,
196,
532,
540,
236,
910,
70,
168,
69,
812,
554,
302,
692,
418,
47,
699,
383,
776,
793,
653,
116,
660,
224,
4,
441,
931,
49,
592,
642,
444,
639,
10,
724,
823,
921,
558,
150,
317,
167,
339,
259,
868,
736,
778,
146,
71,
212,
115,
220,
651,
656,
877,
588,
50,
741,
372,
153,
666,
644,
8,
723,
851,
566,
176,
40,
526,
548,
248,
198,
500,
604,
81,
238,
536,
539,
602,
918,
800,
188,
127,
894,
768,
89,
721,
826,
151,
292,
247,
481,
867,
740,
163,
304,
923,
309,
281,
213,
780,
275,
886,
885,
804,
414,
106,
766,
371,
464,
900,
83,
446,
843,
715,
680,
710,
38,
848,
359,
748,
451,
478,
856,
35,
177,
838,
521,
136,
802,
718,
422,
760,
803,
467,
373,
767,
85,
677,
712,
410,
406,
840

] #manual
reject_worker_id = [] #manual
bStrigent = 0
#bStrigent = 1 #manual
import pandas as pd
import os
import speech_recognition as sr

if bStage == 1:
    cur_exp = 'exp2'
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

    

else:

#    cur_exp = 'exp2'
    tTranscript = pd.readcsv('tTranscript_all_' + cur_exp + '.csv')    
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
