#run this file at two stages:
#    1: get the auto fail. Then enter the trial num to reject
#    2: remove the rejected trial to output the final tTranscript

bStage = 1
bStage = 2 #manual
reject_row_index = [] #manual
import pandas as pd
import os
import speech_recognition as sr

if bStage == 1:
    cur_exp = 'exp1'
    tAll_trials = pd.read_csv(os.path.join(cur_exp, 'tAll_trials.csv'))

    supposed_answer_transcript = []
    auto_transcript = []
    status = []
    trial_id = []
    answer_files = []
    for iFile in os.listdir(os.path.join('/Users/xzfang/Desktop/prosody_study_data', cur_exp, 'responses_to_analyze')):
        #    print(cur_file)
        cur_file = os.path.join('/Users/xzfang/Desktop/prosody_study_data', cur_exp, 'responses_to_analyze', iFile)
        cur_trial = int(cur_file[len(cur_file) - 6: len(cur_file) - 4])
        print(cur_trial)
        trial_id = trial_id + [cur_trial]
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

            if not script == tAll_trials.loc[tAll_trials.trial_id == cur_trial, 'answer_script'].any():
        #                print(iRow.question_file + ' is fine')
        #            else:
        #                print('check file ' + )
                status = status + ['auto_fail']
            else:
                status = status + ['auto_pass']

    # question_files = question_files + [  dquestion_file]
    #                print(iRow.question_file + 'recognized as' + script)
    # print("Google Speech Recognition thinks you said " + )
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request result from Google Speech Recognition service; {0}".format(e))

    tTranscript = pd.DataFrame(zip(trial_id, supposed_answer_transcript, auto_transcript, status, answer_files), columns=['trial_id', 'supposed_answer_transcript', 'auto_transcript', 'status', 'answer_files'])

    tTranscript_auto_fail = tTranscript.loc[tTranscript.status == 'auto_fail']

    tTranscript_auto_fail.to_csv('tTranscript_auto_fail_only_' + cur_exp + '.csv',  encoding='utf-8')

else:

    tTranscript0 = tTranscript.drop(reject_row_index)

    tTranscript1 = tTranscript0[['trial_id', 'supposed_answer_transcript', 'answer_files']]
    tTranscript1['answer_textgrid'] = [a.replace('wav', 'TextGrid') for a in tTranscript1.answer_files]
    tTranscript1['answer_files'] = [a.replace('responses_to_analyze', 'responses_to_analyze_downsampled') for a in tTranscript1.answer_files]

    tTranscript1.to_csv('tTranscript_' + cur_exp + '.csv',  encoding='utf-8')
