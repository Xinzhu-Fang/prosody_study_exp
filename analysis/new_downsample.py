import librosa
import soundfile as sf
import sys
import numpy as np
def ds(srfile, dsfile):
    y, s = librosa.load(srfile, sr=16000) # Downsample 44.1kHz to 8kHz
    # librosa.output.write_wav(dsfile, y, sr=16000)

    # maxv = np.iinfo(np.int16).max
    # librosa.output.write_wav(dsfile, (y * maxv).astype(np.int16), sr=16000)
    # maxv = np.iinfo(np.int16).max
    # librosa.output.write_wav(dsfile, (y * maxv).astype(np.float16), sr=16000)
    sf.write(dsfile, y, 16000)
ds(sys.argv[1], sys.argv[2])
