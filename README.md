## telegram-text-to-speech

A telegram bot convert text into natural-sounding speech using an API powered by Google’s AI technologies.

Reference Tutorial video : https://www.youtube.com/watch?v=Z8t-XGbUFnw

I used google text to speech service instead

## Create GOOGLE_APPLICATION_CREDENTIALS in .env

https://cloud.google.com/docs/authentication/getting-started

after downloading, Replace KEY_PATH with the path of the JSON file in .env

```python
GOOGLE_APPLICATION_CREDENTIALS = C:\YOUR_CREDENTIALS_FILE.json
```

## Suport languages
language		male/women voice	command
Afrikaans (South Africa)	af-ZA-Standard-A	FEMALE	ZAA
Arabic	ar-XA-Standard-A	FEMALE	XAA
Arabic	ar-XA-Standard-B	MALE	XAB
Arabic	ar-XA-Standard-C	MALE	XAC
Arabic	ar-XA-Standard-D	FEMALE	XAD
Bulgarian (Bulgaria)	bg-bg-Standard-A	FEMALE	BGA
Chinese (Hong Kong)	yue-HK-Standard-A	FEMALE	HKA
Chinese (Hong Kong)	yue-HK-Standard-B	MALE	HKB
Chinese (Hong Kong)	yue-HK-Standard-C	FEMALE	HKC
Chinese (Hong Kong)	yue-HK-Standard-D	MALE	HKD
Czech (Czech Republic)	cs-CZ-Standard-A	FEMALE	CZA
Danish (Denmark)	da-DK-Standard-A	FEMALE	DKA
Danish (Denmark)	da-DK-Standard-C	MALE	DKC
Danish (Denmark)	da-DK-Standard-D	FEMALE	DKD
Danish (Denmark)	da-DK-Standard-E	FEMALE	DKE
Dutch (Netherlands)	nl-NL-Standard-A	FEMALE	NLA
Dutch (Netherlands)	nl-NL-Standard-B	MALE	NLB
Dutch (Netherlands)	nl-NL-Standard-C	MALE	NLC
Dutch (Netherlands)	nl-NL-Standard-D	FEMALE	NLD
Dutch (Netherlands)	nl-NL-Standard-E	FEMALE	NLE
English (Australia)	en-AU-Standard-A	FEMALE	AUA
English (Australia)	en-AU-Standard-B	MALE	AUB
English (Australia)	en-AU-Standard-C	FEMALE	AUC
English (Australia)	en-AU-Standard-D	MALE	AUD
English (India)	en-IN-Standard-A	FEMALE	INA
English (India)	en-IN-Standard-B	MALE	INB
English (India)	en-IN-Standard-C	MALE	INC
English (UK)	en-GB-Standard-A	FEMALE	GBA
English (UK)	en-GB-Standard-B	MALE	GBB
English (UK)	en-GB-Standard-C	FEMALE	GBC
English (UK)	en-GB-Standard-D	MALE	GBD
English (UK)	en-GB-Standard-F	FEMALE	GBF
English (US)	en-US-Standard-A	MALE	USA
English (US)	en-US-Standard-B	MALE	USB
English (US)	en-US-Standard-C	FEMALE	USC
English (US)	en-US-Standard-D	MALE	USD
English (US)	en-US-Standard-E	FEMALE	USE
English (US)	en-US-Standard-F	FEMALE	USF
English (US)	en-US-Standard-G	FEMALE	USG
English (US)	en-US-Standard-H	FEMALE	USH
English (US)	en-US-Standard-I	MALE	USI
English (US)	en-US-Standard-J	MALE	USJ
Filipino (Philippines)	fil-PH-Standard-A	FEMALE	PHA
Filipino (Philippines)	fil-PH-Standard-B	FEMALE	PHB
Filipino (Philippines)	fil-PH-Standard-C	MALE	PHC
Filipino (Philippines)	fil-PH-Standard-D	MALE	PHD
Finnish (Finland)	fi-FI-Standard-A	FEMALE	FIA
French (Canada)	fr-CA-Standard-A	FEMALE	CAA
French (Canada)	fr-CA-Standard-B	MALE	CAB
French (Canada)	fr-CA-Standard-C	FEMALE	CAC
French (Canada)	fr-CA-Standard-D	MALE	CAD
French (France)	fr-FR-Standard-A	FEMALE	FRA
French (France)	fr-FR-Standard-B	MALE	FRB
French (France)	fr-FR-Standard-C	FEMALE	FRC
French (France)	fr-FR-Standard-D	MALE	FRD
French (France)	fr-FR-Standard-E	FEMALE	FRE
German (Germany)	de-DE-Standard-A	FEMALE	DEA
German (Germany)	de-DE-Standard-B	MALE	DEB
German (Germany)	de-DE-Standard-C	FEMALE	DEC
German (Germany)	de-DE-Standard-D	MALE	DED
German (Germany)	de-DE-Standard-E	MALE	DEE
German (Germany)	de-DE-Standard-F	FEMALE	DEF
Greek (Greece)	el-GR-Standard-A	FEMALE	GRA
Hungarian (Hungary)	hu-HU-Standard-A	FEMALE	HUA
Icelandic (Iceland)	is-is-Standard-A	FEMALE	ISA
Indonesian (Indonesia)	id-ID-Standard-A	FEMALE	IDA
Indonesian (Indonesia)	id-ID-Standard-B	MALE	IDB
Indonesian (Indonesia)	id-ID-Standard-C	MALE	IDC
Indonesian (Indonesia)	id-ID-Standard-D	FEMALE	IDD
Italian (Italy)	it-IT-Standard-A	FEMALE	ITA
Italian (Italy)	it-IT-Standard-B	FEMALE	ITB
Italian (Italy)	it-IT-Standard-C	MALE	ITC
Italian (Italy)	it-IT-Standard-D	MALE	ITD
Japanese (Japan)	ja-JP-Standard-A	FEMALE	JPA
Japanese (Japan)	ja-JP-Standard-B	FEMALE	JPB
Japanese (Japan)	ja-JP-Standard-C	MALE	JPC
Japanese (Japan)	ja-JP-Standard-D	MALE	JPD
Korean (South Korea)	ko-KR-Standard-A	FEMALE	KRA
Korean (South Korea)	ko-KR-Standard-B	FEMALE	KRB
Korean (South Korea)	ko-KR-Standard-C	MALE	KRC
Korean (South Korea)	ko-KR-Standard-D	MALE	KRD
Latvian (Latvia)	lv-lv-Standard-A	MALE	LVA
Mandarin Chinese	cmn-CN-Standard-A	FEMALE	CNA
Mandarin Chinese	cmn-CN-Standard-B	MALE	CNB
Mandarin Chinese	cmn-CN-Standard-C	MALE	CNC
Mandarin Chinese	cmn-CN-Standard-D	FEMALE	CND
Mandarin Chinese	cmn-TW-Standard-A	FEMALE	TWA
Mandarin Chinese	cmn-TW-Standard-B	MALE	TWB
Mandarin Chinese	cmn-TW-Standard-C	MALE	TWC
Norwegian (Norway)	nb-NO-Standard-A	FEMALE	NOA
Norwegian (Norway)	nb-NO-Standard-B	MALE	NOB
Norwegian (Norway)	nb-NO-Standard-C	FEMALE	NOC
Norwegian (Norway)	nb-NO-Standard-D	MALE	NOD
Norwegian (Norway)	nb-no-Standard-E	FEMALE	NOE
Polish (Poland)	pl-PL-Standard-A	FEMALE	PLA
Polish (Poland)	pl-PL-Standard-B	MALE	PLB
Polish (Poland)	pl-PL-Standard-C	MALE	PLC
Polish (Poland)	pl-PL-Standard-D	FEMALE	PLD
Polish (Poland)	pl-PL-Standard-E	FEMALE	PLE
Portuguese (Brazil)	pt-BR-Standard-A	FEMALE	BRA
Portuguese (Portugal)	pt-PT-Standard-A	FEMALE	PTA
Portuguese (Portugal)	pt-PT-Standard-B	MALE	PTB
Portuguese (Portugal)	pt-PT-Standard-C	MALE	PTC
Portuguese (Portugal)	pt-PT-Standard-D	FEMALE	PTD
Romanian (Romania)	ro-RO-Standard-A	FEMALE	ROA
Russian (Russia)	ru-RU-Standard-A	FEMALE	RUA
Russian (Russia)	ru-RU-Standard-B	MALE	RUB
Russian (Russia)	ru-RU-Standard-C	FEMALE	RUC
Russian (Russia)	ru-RU-Standard-D	MALE	RUD
Russian (Russia)	ru-RU-Standard-E	FEMALE	RUE
Serbian (Cyrillic)	sr-rs-Standard-A	FEMALE	RSA
Slovak (Slovakia)	sk-SK-Standard-A	FEMALE	SKA
Spanish (Spain)	es-ES-Standard-A	FEMALE	ESA
Spanish (Spain)	es-ES-Standard-B	MALE	ESB
Spanish (Spain)	es-ES-Standard-C	FEMALE	ESC
Spanish (Spain)	es-ES-Standard-D	FEMALE	ESD
Swedish (Sweden)	sv-SE-Standard-A	FEMALE	SEA
Thai (Thailand)	th-TH-Standard-A	FEMALE	THA
Turkish (Turkey)	tr-TR-Standard-A	FEMALE	TRA
Turkish (Turkey)	tr-TR-Standard-B	MALE	TRB
Turkish (Turkey)	tr-TR-Standard-C	FEMALE	TRC
Turkish (Turkey)	tr-TR-Standard-D	FEMALE	TRD
Turkish (Turkey)	tr-TR-Standard-E	MALE	TRE
Ukrainian (Ukraine)	uk-UA-Standard-A	FEMALE	UAA
Vietnamese (Vietnam)	vi-VN-Standard-A	FEMALE	VNA
Vietnamese (Vietnam)	vi-VN-Standard-B	MALE	VNB
Vietnamese (Vietnam)	vi-VN-Standard-C	FEMALE	VNC
Vietnamese (Vietnam)	vi-VN-Standard-D	MALE	VND
![image](https://user-images.githubusercontent.com/28686176/125229681-db656c00-e309-11eb-8c3d-c96750cb6651.png)
