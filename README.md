# Translator
- A Translator Application using <a href="https://python.org/downloads">Python</a> ang <a href="https://google.com">Google</a>.

<img src="https://img.shields.io/badge/Test-pass-green" width="80px"> <a href="https://pypi.org/project/googletrans/4.0.0rc1/"><img src="https://img.shields.io/badge/googletrans-4.0.0rc1-yellow" width="150px"></a>
<a href="https://pypi.org/project/googletrans/4.0.0rc1/"><img src="https://img.shields.io/badge/PyQt-5-blue" width="58px"></a>
<a href="https://pypi.org/project/gTTS/"><img src="https://img.shields.io/badge/gTTS-2.2.2-red" width="80px"></a>

- Notice : தமிழ், हिन्दी, English are Pre-coded your Languages should be coded by You.
- Language Keyword:
```python
{'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}
```
**Features**
- Translate your Text to All Languages.
- Translate From Speech
- Translate to Selected Language and hear the transtaled Audio.

<img src="https://raw.githubusercontent.com/sijey-praveen/Translator/Sijey/demo/01.png" width="400px"> <img src="https://raw.githubusercontent.com/sijey-praveen/Translator/Sijey/demo/02.png" width="400px">

**How This Works**
- This Application build using Python,<a href="https://riverbankcomputing.com/software/pyqt/"> PyQt</a>, Google.
- This Application collect users Query and send To <a href="https://translate.google.com/intl/en/about/forbusiness/">Google Translator API</a> and get Results.
- PyQt for building the application interface.
- Google <a href="https://cloud.google.com/text-to-speech/">Text-To-Speak-Engine</a> used for Featuring the Audio Option.

# Support
- Executable Application using PyInstaller supports <a href="https://en.wikipedia.org/wiki/Microsoft_Windows">Windows</a>, <a href="https://en.wikipedia.org/wiki/MacOS">Mac</a>, <a href="https://en.wikipedia.org/wiki/Linux">Linux</a>.

# Requirement 
- <a href="https://python.org/downloads">Python 3.6 or Latest Version.</a>
- <a href="https://en.wikipedia.org/wiki/Internet">Internet</a>

# Installation
```python
# Step 1
python setup.py

# Step 2
python Translator.py
```
