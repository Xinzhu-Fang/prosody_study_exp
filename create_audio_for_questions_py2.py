#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:39:20 2020

@author: xzfang
"""

import wave
from espeakng import ESpeakNG
import StringIO
import os
import pandas as pd
from pydub import AudioSegment 



#dir_name ='audio_for_exp12_03_19_20'
dir_name ='audio_for_exp12_03_23_20'
tQuestions = pd.read_csv(os.path.join(dir_name, 'tAll_questions.csv'))
esng = ESpeakNG()
esng.voice = 'english-us'
for iQ, iR in tQuestions.iterrows():
    
#        
#    #esng.say('Hello World!')
#    wavs = esng.synth_wav(iR.question_script)
#    #wavs = esng.synth_wav('Hello World!')
#    wav = wave.open(StringIO.StringIO(wavs))
#    print wav.getnchannels(), wav.getframerate(), wav.getnframes(), wav.getsampwidth(), len(wavs)
#    
#    
#    obj = wave.open(os.path.join(dir_name, iR.question_file), 'w')
#    obj.setnchannels(wav.getnchannels()) # mono
#    obj.setsampwidth(wav.getsampwidth())
#    obj.setframerate(wav.getframerate())
#    for i in range(100, wav.getnframes()*2):
#    #for i in range(len(wavs)):   
#        
#        obj.writeframesraw(wavs[i])
#    obj.close()
        
    words = iR.question_script.split(' ')
    wavs = esng.synth_wav(words[0])
    wav = wave.open(StringIO.StringIO(wavs))

    print wav.getnchannels(), wav.getframerate(), wav.getnframes(), wav.getsampwidth(), len(wavs)
    
    
    obj = wave.open(os.path.join(dir_name, 'constituents_wav', words[0]+'.wav'), 'w')
    obj.setnchannels(wav.getnchannels()) # mono
    obj.setsampwidth(wav.getsampwidth())
    obj.setframerate(wav.getframerate())
    #    for i in range(100, wav.getnframes()*2):
    for i in range(100, len(wavs)):   
        
        obj.writeframesraw(wavs[i])
    obj.close()
    
    song0 = AudioSegment.from_wav(os.path.join(dir_name,'constituents_wav', words[0]+ '.wav'))
        
    
    wavs = esng.synth_wav(words[1])
    
    print wav.getnchannels(), wav.getframerate(), wav.getnframes(), wav.getsampwidth(), len(wavs)
    
    
    obj = wave.open(os.path.join(dir_name, 'constituents_wav', words[1]+'.wav'), 'w')
    obj.setnchannels(wav.getnchannels()) # mono
    obj.setsampwidth(wav.getsampwidth())
    obj.setframerate(wav.getframerate())
    #    for i in range(100, wav.getnframes()*2):
    for i in range(100, len(wavs)):   
        
        obj.writeframesraw(wavs[i])
    obj.close()
    
    song1 = AudioSegment.from_wav(os.path.join(dir_name, 'constituents_wav', words[1]+ '.wav'))
    
    wavs = esng.synth_wav(words[2])
    
    print wav.getnchannels(), wav.getframerate(), wav.getnframes(), wav.getsampwidth(), len(wavs)
    
    
    obj = wave.open(os.path.join(dir_name, 'constituents_wav', words[2]+'.wav'), 'w')
    obj.setnchannels(wav.getnchannels()) # mono
    obj.setsampwidth(wav.getsampwidth())
    obj.setframerate(wav.getframerate())
    #    for i in range(100, wav.getnframes()*2):
    for i in range(100, len(wavs)):   
        
        obj.writeframesraw(wavs[i])
    obj.close()
    
    song2 = AudioSegment.from_wav(os.path.join(dir_name, 'constituents_wav', words[2]+ '.wav'))
    
    
    wavs = esng.synth_wav(words[3])
    
    print wav.getnchannels(), wav.getframerate(), wav.getnframes(), wav.getsampwidth(), len(wavs)
    
    
    obj = wave.open(os.path.join(dir_name, 'constituents_wav', words[3]+'.wav'), 'w')
    obj.setnchannels(wav.getnchannels()) # mono
    obj.setsampwidth(wav.getsampwidth())
    obj.setframerate(wav.getframerate())
    #    for i in range(100, wav.getnframes()*3):
    for i in range(100, len(wavs)):   
        
        obj.writeframesraw(wavs[i])
    obj.close()
    
    song3 = AudioSegment.from_wav(os.path.join(dir_name, 'constituents_wav', words[3]+ '.wav'))
    
    merged = song0 + song1 + song2 + song3
    
    merged.export(os.path.join(dir_name, 'responses_to_analyze', iR.question_file), format='wav')
    
    
