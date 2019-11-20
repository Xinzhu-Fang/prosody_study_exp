import os
import audioop
import wave
import sys
import pandas as pd
def downsampleWav(src, dst, inrate=44100, outrate=16000, inchannels=2, outchannels=1):
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

    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1:
            converted = audioop.tomono(converted[0], 2, 1, 0)
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

# source_dir = sys.argv[1]
# dest_dir = sys.argv[2]
# # Listing all files in current directory.
# listofFiles = os.listdir(os.path.join(source_dir))
# # print(listofFiles[3])
#
# for thisFile in listofFiles:
#     if thisFile[-4:] == '.wav':
#         downsampleWav(os.path.join(source_dir, thisFile), os.path.join(dest_dir, thisFile))
#     else:
#         print("not processed: " + thisFile)

tTranscript = pd.read_csv(sys.argv[1])
for iFile, iRow in tTranscript.iterrows():
    downsampleWav(iRow.answer_files, iRow.answer_downsampled)
