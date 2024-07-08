from pydub import AudioSegment

def conv_to_ogg(file_path):
    audio = AudioSegment.from_mp3(file_path)
    audio.export("output.ogg", format="ogg")