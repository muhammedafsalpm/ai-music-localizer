import os
import yt_dlp

def download_audio(url):
    base_output = "data/input/song"
    output_template = f"{base_output}.%(ext)s"
    final_output = f"{base_output}.wav"

    # CRITICAL FIX: If the user already provided the file, DO NOT delete it!
    # Just return it so the rest of the pipeline can continue.
    if os.path.exists(final_output):
        print("YouTube video already exists locally! Skipping download to avoid blocks.")
        return final_output

    print("\n" + "="*80)
    print("ATTENTION: YouTube is actively blocking this video on your network!")
    print("To bypass this permanently without cookies, we are using Device OAuth.")
    print("If yt-dlp asks you to open google.com/device below, please open it")
    print("in your browser, enter the code it gives you, and press allow.")
    print("It will wait 3 minutes for you to do this before failing.")
    print("="*80 + "\n")

    base_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}],
        'outtmpl': output_template,
        'quiet': False,
        'no_warnings': True,
        'username': 'oauth2',
    }

    try:
        with yt_dlp.YoutubeDL(base_opts) as ydl:
            ydl.download([url])
            print("Successfully downloaded with yt-dlp OAuth2!")
            return final_output
    except Exception as e:
        error_msg = f"Failed to download video using OAuth2. Please check exactly what yt-dlp printed above.\nError details: {e}"
        raise Exception(error_msg)