# Audio To Voice Convert Telegram Bot

This is a telegram bot bult with Python and `aiogram` library that converts audio files into voice messages. The bot allows users to send an audio file and add a caption, and it will convert the audio file into a voice message with the provided caption. The converted voice message will be sent back to the user.

## Features
- Converts audio files into voice messages
- Allows adding a caption to the converted voice message
- Automatic deletion of local files after conversion

## Conditions
- Python 3.8 and above versions installed on your PC
- Bot Token. You can get it by creating a new bot [Telegram's BotFather](https://t.me/BotFather)
- ffmpeg. you need to install it and add to your PATH ([FFMPeg](https://ffmpeg.org/download.html))

## Getting Started

1. **Clone this repository:**
    ```bash
   git clone https://github.com/YOUR-USERNAME/audio-to-voice-convert-bot.git

2. **Install dependencies:**
    ```bash
   cd audio_convert_bot
   pip install aiogram==2.5.0
   pip install python-dotenv
   pip install ffmpeg-python
   
3. **Install FFmpeg:**

   Make sure FFmpeg is installed and available in your system's PATH. You can download FFmpeg from the official website: [FFmpeg Download](https://ffmpeg.org/download.html)

   Follow the installation instructions specific to your operating system. Once FFmpeg is installed, you should be able to access it from the command line by running the `ffmpeg -version` command.

4. **Create a `.env` File:**

   Create a `.env` file in the root directory of the project. This file will store your Telegram bot token. Open the `.env` file and add the following line:<br>
   `TOKEN="your-telegram-bot-token"`

5. **Start the bot:**

   ```bash
   python main.py
   
6. Start a conversation with your bot on Telegram and send an audio file to convert it into a voice message.
