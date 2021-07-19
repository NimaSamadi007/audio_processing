import pydub
import numpy as np
import sounddevice as sd
from matplotlib import pyplot as plt
from scipy.io.wavfile import read, write


class Music: # static class for music I/O standard
    
    @staticmethod
    def plotter(x=None, y=None, title="", xlabel="", ylabel="", figsize=(20, 12), subplt=(1, 1, 1)):
        """
            East plotter
        """
        if x is None:
            x = np.arange(y.shape[0])
        plt.figure(figsize=figsize)
        plt.subplot(subplt)
        plt.plot(x, y)
        
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
        return
    
    @staticmethod
    def frequencies(x, fs):
        """
            Audio vector to frequencies with FFT ratio
        """
        Fd = np.fft.fft(x)
        Fx = np.linspace(0, fs, max(x.shape))
        return Fd, Fx
    
    @staticmethod
    def read_mp3(filename, normalized=False):
        """
            MP3 to numpy array
        """
        a = pydub.AudioSegment.from_mp3(filename)
        y = np.array(a.get_array_of_samples(), dtype=np.int16)
        if a.channels == 2:
            y = y.reshape((-1, 2))
        if normalized:
            return a.frame_rate, np.float32(y) / 2**15
        else:
            return a.frame_rate, y
    
    @staticmethod
    def write_mp3(filename, Fs, x, normalized=False):
        """ 
            numpy array to MP3 
        """
        channels = 2 if (x.ndim == 2 and x.shape[1] == 2) else 1
        if normalized:  
            y = np.int16(x * 2 ** 15)
        else:
            y = np.int16(x)
        song = pydub.AudioSegment(y.tobytes(), frame_rate=Fs, sample_width=2, channels=channels)
        song.export(filename, format="mp3", bitrate="320k")
        return

