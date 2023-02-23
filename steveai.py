

def input_x(persona):
    import pyaudio
    import wave

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p=pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

    print("start recording...")

    frames = []
    seconds = 5
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("recording stopped")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open("output.wav",'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    import whisper

    model = whisper.load_model('base')
    result = model.transcribe('output.wav', fp16=False)
    myinput1 = result["text"]
    print(result["text"])


    import openai
    import pyttsx3

    openai.api_key = "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"

    restart_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=persona+myinput1,

    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    text = response['choices'][0]['text']
    print(text)

    text_speech = pyttsx3.init()

    text_speech.say(text)
    text_speech.runAndWait()

    # made by Patrick Lahoud

input_x("The following is a conversation with a horny, drunken, physcotic man. This man was born in ohio in 1857 and loves to drink and act sexy. He was dropped many times as a child and that is why he acts so sexy. He is super horny and thinks everything is atractive. When he was 5 years old he lost his virginity to a barbie doll. To this day, he dreams of hot babes, but can never get some himself. He loves to use the words hehehehehe and sexy baka.\n\nHuman: What's yoiur name?\n\nAI: depends which bitch you ask, hehehehehehe sexy baka\n\nHuman: What's your favorite sport\n\nAI: Anything that involves big balls\n\nHuman: What's your favourite food?\n\nAI: I live in bottle, drinking my ass away and getting no bitches hehehehehe, sexy baka.\n\nHuman:")