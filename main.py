import pyaudio
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

audio = AudioSegment.from_mp3("railway.mp3")

def textToSpeech(text, filename):
    my_text = str(text)
    language = "hi"
    my_obj = gTTS(text=my_text, lang=language, slow=False)
    my_obj.save(filename)

# This function returns pydub's audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    # No. 1 : Generate kripya dhyan dijiye
    start = 88000
    finish = 90200
    audioProccessed = audio[start:finish]
    audioProccessed.export("1_hindi.mp3", format="mp3")

    # No. 2 : Generate From city
    # No. 3 : Generate Se Chalkar
    start = 91000
    finish = 92200
    audioProccessed = audio[start:finish]
    audioProccessed.export("3_hindi.mp3", format="mp3")

    # No. 4 : Generate Via City
    # No. 5 : Generate Ke Raste
    start = 94000
    finish = 95000
    audioProccessed = audio[start:finish]
    audioProccessed.export("5_hindi.mp3", format="mp3")

    # No. 6 : Generate To City
    # No. 7 : Generate Ko Jaane Wali Gaadi Sankhya
    start = 96000
    finish = 98900
    audioProccessed = audio[start:finish]
    audioProccessed.export("7_hindi.mp3", format="mp3")

    # No. 8 : Generate Train No. and Train Name
    # No. 9 : Generate Kuch Hi Samay Me Platform Sankhya
    start = 105500
    finish = 108200
    audioProccessed = audio[start:finish]
    audioProccessed.export("9_hindi.mp3", format="mp3")

    # No. 10 : Generate Platform No.
    # No. 11 : Generate Pr Aa Rahi Hai
    start = 109000
    finish = 112250
    audioProccessed = audio[start:finish]
    audioProccessed.export("11_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel("announce_hindi.xlsx")
    print(df)
    for index, item in df.iterrows():
        # No. 2 : Generate From city
        textToSpeech(item["from"], "2_hindi.mp3")

        # No. 4 : Generate Via City
        textToSpeech(item["via"], "4_hindi.mp3")

        # No. 6 : Generate To City
        textToSpeech(item["to"], "6_hindi.mp3")

        # No. 8 : Generate Train No. and Train Name
        textToSpeech(item["train_no"] + " " + item["train_name"], "8_hindi.mp3")

        # No. 10 : Generate Platform No.
        textToSpeech(item["platform"], "10_hindi.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__ == '__main__':
    print("Genrating Skeleton....")
    generateSkeleton()
    print("Now Genrating Announcement....")
    generateAnnouncement("announce_hindi.xlsx")
