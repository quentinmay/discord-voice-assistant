# 🎤 Discord Voice Assistant

Discord Voice Assistant is a Discord Bot built using [discord.js](https://discord.js.org) and [python speech recognition](https://pypi.org/project/SpeechRecognition) to be a voice activated, multi-purpose discord bot. 

## ⚠Requirements
1. [Discord Bot Token](https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot)
2. [Node.js 14.0.0 or newer](https://nodejs.org/)
3. [Python 2.7.18](https://docs.python.org/release/2.7.18/)
4. [Python Speech Recognition](https://pypi.org/project/SpeechRecognition)

## ⚡Installation

Easily deployable using git clone:

```bash
git clone https://github.com/quentinmay/discord-voice-assistant.git
cd discord-voice-assistant
npm install
pip install SpeechRecognition

mkdir voicedata
```
Now you must configure the bot before running using config example file:
```bash
mv config.json.example config.json
```
## Simple Configuration (Required)
Only the top 2 are required for basic functionality.

```json
{
    "discordToken": "",
    "discordDevID": "",
    "commandPrefix": "0",
    "spotifyClientID": "",
    "spotifyClientSecret": "",
    "statusActivity": "status.",
    "statusURL": "https://www.twitch.tv/twitch",
    "statusType": "STREAMING"
}
```

## 🚀Initial Startup
Just startup the script now that everything has been built and you've filled your config file.
```bash
node index.js
```
Basic startup guide/instructions once you have the scripts running can be found on [issue #1](https://github.com/quentinmay/discord-voice-assistant/issues/1#issuecomment-909806831) 
