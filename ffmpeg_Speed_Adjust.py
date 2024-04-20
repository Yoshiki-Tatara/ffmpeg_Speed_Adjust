import os
import subprocess

def change_audio_speed(audio_file, speed):
    output_file = f"changed_{audio_file}"
    cmd = [
        'ffmpeg', '-i', audio_file, '-filter:a', f"atempo={speed}", '-vn', output_file
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main():
    speed = input("速度を0.1から9.9の間で入力してください（例: 1.5）: ")
    try:
        speed = float(speed)
        if not 0.1 <= speed <= 9.9:
            raise ValueError
    except ValueError:
        print("入力された速度が不正です。0.1から9.9の間の数値を入力してください。")
        return

    audio_files = [f for f in os.listdir() if f.endswith('.mp3') or f.endswith('.wav')]
    if not audio_files:
        print("音声ファイルが見つかりません。")
        return

    for audio_file in audio_files:
        change_audio_speed(audio_file, speed)
        print(f"{audio_file} の速度を {speed} 倍に変更しました。")

if __name__ == "__main__":
    main()
