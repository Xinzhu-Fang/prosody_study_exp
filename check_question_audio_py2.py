# py2
import pandas as pd
import os
import speech_recognition as sr


#audio_dir = 'audio_for_exp0_to_exp2_11_04_19'
#audio_dir = 'audio_for_exp1_to_6_01_10_20'
#audio_dir = 'audio_for_exp10_02_17_20'
#audio_dir = 'audio_for_exp9_02_16_20'
audio_dir = 'audio_for_exp0_04_12_20'
audio_dir = 'audio_for_exp0_04_19_20'
audio_dir = 'audio_for_exp14_09_17_20_saima'

tAll_questions = pd.read_csv(os.path.join(audio_dir, 'tAll_questions.csv'))
question_files = []
auto_transcripts = []
for iTrial, iRow in tAll_questions.iterrows():
    cur_file = os.path.join(
        audio_dir, 'responses_to_analyze', iRow.question_file)
    if not os.path.isfile(cur_file):
        print("we still need " + iRow.question_file)
    else:

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
            #           script = r.recognize_google(audio)
            #           script = r.recognize_sphinx(audio, 'zh-CN') # terrible performance
            script = 'na'

            if not script == iRow.question_script:
                #                print(iRow.question_file + ' is fine')
                #            else:
                #                print('check file ' + )
                question_files = question_files + [iRow.question_file]
                auto_transcripts = auto_transcripts + [script]
#                print(iRow.question_file + 'recognized as' + script)
            # print("Google Speech Recognition thinks you said " + )
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            question_files = question_files + [iRow.question_file]
            auto_transcripts = auto_transcripts + ['na']
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
            question_files = question_files + [iRow.question_file]
            auto_transcripts = auto_transcripts + ['na']
tTranscript = pd.DataFrame(zip(question_files, auto_transcripts), columns=[
                           'question_file', 'auto_transcript'])

tTranscript.to_csv('tTranscript_questions_' + audio_dir +
                   '.csv',  encoding='utf-8', index=False)
