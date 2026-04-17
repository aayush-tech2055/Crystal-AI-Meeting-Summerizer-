import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    
    with open("data/transcript.txt", "w") as f:
        f.write(result["text"])
    
    return result["text"]