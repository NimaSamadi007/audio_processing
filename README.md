# audio_processing
Multiple audio processing applications

# Descriptions:
This project contains 4 sperate GUI which each of them does processing on audio and music signals. First GUI is about filtering signal which you can filter signal and play it again to compare the results.

Next GUI is devoted to understanding the effect of chorous (delay) on music.

The third one is about some 3D effect on signal which you can move the sound source between your speakers. You can change the sound source place in real time.

Finally, the last GUI is used for musical note detection. You can enter the music you want and specify the desired time period, and get the notes in a pdf file. A sample output of this GUI is as follow:

<img src="/audio_proc1.png">

This notes are extracted from the music inside the repo.

# Usage
You had better run this code on windows, especially to see th GUI well, and not to get error because of using some fonts that I used to print notes on the pdf file. 

After cloning repository, make sure that you have python3 on your machine plus installing this libraries:

```
pydub
numpy
sounddevice
tkinter 
scipy
matplotlib
pillow
```
furthermore, this project has been written using jupyter lab. So, you should use jupyter to run it. Don't for get to put Music class alongside the .ipynb file
