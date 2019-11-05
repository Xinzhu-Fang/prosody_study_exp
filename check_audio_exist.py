import pandas as pd
import os
import speech_recognition as sr

cur_exp = 'exp0'
audio_dir = 'audio_for_exp0_to_exp2_11_04_19'
tAll_trials = pd.read_csv(os.path.join(cur_exp, 'tAll_trials.csv'))
question_files = []
auto_transcripts = []
for iTrial, iRow in tAll_trials.iterrows():
    cur_file = os.path.join(audio_dir, 'responses_to_analyze', iRow.question_file)
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
            script = r.recognize_google(audio)
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
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

tAudio_transcription = pd.DataFrame(zip(question_files, auto_transcripts), columns = ['question_file', 'auto_transcript'])

tAudio_transcription.to_csv('tAudio_transcription_' + cur_exp + '.csv',  encoding='utf-8', index=False)
