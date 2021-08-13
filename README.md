## telegram-text-to-speech

A telegram bot convert text into natural-sounding speech using an API powered by Google’s AI technologies.

Reference Tutorial video : https://www.youtube.com/watch?v=Z8t-XGbUFnw

I used Google Cloud Text-to-Speech service instead

## Create GOOGLE_APPLICATION_CREDENTIALS in .env

https://cloud.google.com/docs/authentication/getting-started

Replace KEY_PATH with the path of the JSON file in .env

```python
GOOGLE_APPLICATION_CREDENTIALS = C:\YOUR_CREDENTIALS_FILE.json
```

## Demo

You can try it in mybot https://t.me/Toohardtomakeabot just ```/start``` it and send the command ```/say whatever you want to say```

## Suport languages


For example : To convent hello world to speech and speak in english , just type ```/say usa Hello World```

Supported languages with the command as below:

![image](https://user-images.githubusercontent.com/28686176/125229775-0354cf80-e30a-11eb-821b-ec54f2ebb206.png)

FYI:https://cloud.google.com/text-to-speech/docs/voices
