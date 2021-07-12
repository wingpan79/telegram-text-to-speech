# python3, text-to-speach, telegram-bot-api, simple responsive bot
from dotenv import load_dotenv  # for python-dotenv method
import requests
import json
import os
import threading
import time
import config
from datetime import datetime

load_dotenv()  # find .env file in same folder


class TelegramBot:
    def __init__(self):
        self.__YOURAPIKEY = os.environ.get('YOURAPIKEY')
        self.__URL = f"https://api.telegram.org/bot{self.__YOURAPIKEY}/"
        self.__last_update_id = 0
        self.__setLastUpdate()

    def runUpdate(self):
        # process updates every 3 seconds
        threading.Timer(3.0, self.runUpdate).start()
        self.index()

    def synthesize_text(self, text, language):
        """Synthesizes speech from the input string of text."""
        from google.cloud import texttospeech

        client = texttospeech.TextToSpeechClient()

        input_text = texttospeech.SynthesisInput(text=text)

        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.VoiceSelectionParams(
            language_code="yue-HK",
            name=language,
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            request={"input": input_text, "voice": voice,
                     "audio_config": audio_config}
        )

        with open("voice.mp3", "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "voice.mp3"')
        # time.sleep(1)

    def __setLastUpdate(self):
        # not to send two responses
        response = requests.get(self.__URL + "getUpdates").json()
        result = response['result']
        if len(result) > 0:
            self.__last_update_id = result[len(result)-1]['update_id']

    def index(self):
        offset = self.__last_update_id + 1

        response = requests.get(
            self.__URL + "getUpdates?offset={offset}").json()
        result = response['result']

        if len(result) > 0:
            # respond to all new messages, and save the last update_id to the session
            for update in result:
                update_id = update['update_id']
                if(update_id > self.__last_update_id):
                    # line below should be here, otherwise bot sends us more than one replies,
                    # because code doesn't catch up with the logic sometimes
                    self.__last_update_id = update_id
                    # print("new update")
                    message = update.get('message')
                    chat_id = message['chat']['id']
                    first_name = message['chat'].get('first_name')
                    last_name = message['chat'].get('last_name')
                    language_list = config.language_list #get supported languages list
                    # username        = message['chat']['username']
                    if("text" in message):
                        now = datetime.now()
                        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                        print(chat_id, first_name, last_name,
                              message['text'], dt_string)
                        text = message['text']
                        if(text == "/start"):
                            answer = "可以將文字轉做語音 唔好一次輸入太多字\n<pre><code class='language-python'>/hka 你想打既字</code></pre>"
                            requests.get(
                                f'{self.__URL}sendMessage?chat_id={chat_id}&text={answer}&parse_mode=HTML')
                        else:
                            key = text[text.find('/')+1:text.find(' ')].upper()
                            if key in language_list:
                                x = text.replace(
                                text[text.find('/'):text.find(' ')], "")
                                self.synthesize_text(x, language_list[key])
                                files = {'voice': open('voice.mp3', 'rb')}
                            requests.post(f'{self.__URL}sendVoice?chat_id={chat_id}', files=files).json() #send requested speech to client
        return 0


telegramBot = TelegramBot()
telegramBot.runUpdate()
