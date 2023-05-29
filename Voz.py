import speech_recognition as sr
import pyaudio
import wave

app = Flask(__name__)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

frames = []

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/record', methods=['POST'])
def record():
    action = request.form['action']

    if action == 'start':
        frames.clear()

        def audio_callback(in_data, frame_count, time_info, status):
            frames.append(in_data)
            return (None, pyaudio.paContinue)

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,
                        stream_callback=audio_callback)
        stream.start_stream()

        return {'status': 'success', 'message': 'Recording started'}

    elif action == 'stop':
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        stream.stop_stream()
        stream.close()
        p.terminate()

        wav_filename = 'audio.wav'
        with wave.open(wav_filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            r = sr.Recognizer()

            with sr.AudioFile('audio.wav') as source:
                audio = r.record(source)
                texto1= r.recognize_google(audio, language='es-ES').lower()
                print (texto1)

        return {'status': 'success', 'message': 'Recording stopped', 'filename': wav_filename }
    return "<h2>{texto1}</h2>"

if __name__ == '__main__':
    app.run(debug=True)