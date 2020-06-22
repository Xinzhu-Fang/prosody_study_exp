import pandas as pd
import sys
import shutil
import os

import audioop
import wave

def downsampleWav(src, dst, outrate=16000, inchannels=1, outchannels=1):
# def downsampleWav(src, dst, inrate=44100, outrate=16000, inchannels=2, outchannels=1):
# def downsampleWav(src, dst, inrate=44100, outrate=11025, inchannels=2, outchannels=1):


    if not os.path.exists(src):
        print('Source not found!')
        return False

    try:
        s_read = wave.open(src, 'r')
        s_write = wave.open(dst, 'w')
    except:
        print('Failed to open files!')
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)
    inrate = s_read.getframerate()
    # print(inrate)

    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        converted = converted[0]
        # print(len(converted))
        # print(len(converted[0]))
        # if outchannels == 1:
        #     converted = audioop.tomono(converted[0], 2, 1, 0)
        #     print(len(converted))

    except:
        print('Failed to downsample wav')
        return False

    try:
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted)
    except:
        print('Failed to write wav')
        return False

    try:
        s_read.close()
        s_write.close()
    except:
        print('Failed to close wav files')
        return False

    return True

tTranscript = pd.read_csv(sys.argv[1])
old_dir = sys.argv[2]
new_dir = sys.argv[3]
for iFile, iRow in tTranscript.iterrows():
    trans = open(os.path.join(new_dir, iRow.question_file.replace("wav", "txt")), "w")
    trans.write(iRow.question_script[1:-1])
    trans.close()


    # shutil.copyfile(os.path.join(old_dir, iRow.question_file), os.path.join(new_dir, iRow.question_file))

    downsampleWav(os.path.join(old_dir, iRow.question_file), os.path.join(new_dir, iRow.question_file))
