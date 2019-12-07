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

tTranscript = pd.DataFrame(zip(question_files, auto_transcripts), columns = ['question_file', 'auto_transcript'])

tTranscript.to_csv('tTranscript_questions_' + cur_exp + '.csv',  encoding='utf-8', index=False)


python Calign.py test/test_16000.wav test/test_16000.txt /Users/xzfang/Github/prosody_study_exp/audio_mandarin/经济自由.Textgrid


python .Zap.0.align.py test/test_16000.wav test/test_16000.txt /Users/xzfang/Github/prosody_study_exp/audio_mandarin/经济自由.Textgrid



python /Users/xzfang/Github/prosody_study_exp/analysis/downsampleWav.py /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小明推了小红吗.wav /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小明推了小红吗16000.wav
python /Users/xzfang/Github/prosody_study_exp/analysis/downsampleWav.py /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红推了小明.wav /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红推了小明16000.wav

python /Users/xzfang/Github/prosody_study_exp/analysis/new_downsample.py /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小明推了小红吗.wav /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小明推了小红吗16000.wav
python .Zap.0.align.py /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小明推了小红吗16000.wav /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小明.txt /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小明.Textgrid

python /Users/xzfang/Github/prosody_study_exp/analysis/new_downsample.py /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红推了小明.wav /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红推了小明16000NewDS.wav
python .Zap.0.align.py /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红推了小明16000NewDS.wav /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红.txt /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红.Textgrid
python .Zap.0.align.py /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红推了小明16000.wav /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红推.txt /Users/xzfang/Github/prosody_study_exp/audio_mandarin/小红推.Textgrid
python /Users/xzfang/Github/prosody_study_exp/analysis/downsampleWav.py /Users/xzfang/Github/prosody_study_exp/audio_mandarin/A2BNOEYZ3VRW2R_prosody_study_exp1_11_10_2019_trial_05.wav /Users/xzfang/Github/prosody_study_exp/audio_mandarin/16000_A2BNOEYZ3VRW2R_prosody_study_exp1_11_10_2019_trial_05.wav
