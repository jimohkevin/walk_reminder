import time
from win10toast import ToastNotifier
from pydub import AudioSegment
from pydub.playback import play

def remind_to_walk():
    toast = ToastNotifier()

    # Display the notification
    toast.show_toast(
        "Take a Walk!",
        "Time to take a walk!",
        duration=20,
        icon_path="icon.ico",
        threaded=True
    )

    # Load sound and reduce volume
    sound = AudioSegment.from_mp3("sounds\\raymond_scott_calm.wav")
    quieter_sound = sound - 10  # Reduce volume by 10 dB (adjust as needed)

    # Play the quieter sound
    play(quieter_sound)

if __name__ == "__main__":
    remind_to_walk()
