import whisper

model = whisper.load_model("medium.en")
result = model.transcribe("Dinosaur.wav")
print(result["segments"])


htmlOut = ""

for seg in result["segments"]:
    startTime = seg["start"]
    htmlOut += '<p><span data-time="{}">{}</span></p>\n'.format(seg["start"], seg["text"])

print(htmlOut)