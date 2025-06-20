📝 Subtitle Translator (SRT)
<p align="center"> <img src="https://img.shields.io/badge/python-async%2Fawait-blue?logo=python"> <img src="https://img.shields.io/badge/aiohttp-fast%20HTTP%20client-brightgreen"> <img src="https://img.shields.io/badge/srt-parser-orange"> <img src="https://img.shields.io/badge/translation-Google%20API-red?logo=googletranslate"> </p>
🎯 Purpose:

This script translates .srt (SubRip Subtitle) files into any language using Google Translate API, with support for async batch processing.
🚀 Usage

python translator.py input.srt output.srt <language_code>

    input.srt — the original subtitle file

    output.srt — the file where the translated subtitles will be saved

    <language_code> — target language code (e.g. ru, es, uz, etc.)

🌍 Language Code Examples
| Language       | Code |
|----------------|------|
| 🇷🇺 Russian     | ru   |
| 🇬🇧 English     | en   |
| 🇪🇸 Spanish     | es   |
| 🇫🇷 French      | fr   |
| 🇯🇵 Japanese    | ja   |
| 🇩🇪 German      | de   |
| 🇨🇳 Chinese     | zh   |
| 🇹🇷 Turkish     | tr   |
| 🇮🇹 Italian     | it   |


    ✅ You can use any language code supported by Google Translate.

📦 Requirements

```bash
pip install aiohttp srt deep-translator
```

💡 Examples

```bash
python translator.py movie.srt movie_ru.srt ru
python translator.py talk.srt talk_es.srt es
python translator.py lecture.srt lecture_uz.srt uz
```
🔧 Features

    ✅ Supports .srt subtitle format

    ✅ Fast translation using asyncio and aiohttp

    ✅ Uses Google Translate API (no key required)

    ✅ Language code customizable (e.g. ru, uz, es, etc.)

    ✅ Subtitles are processed in batches for efficiency

⚠️ Notes

    Large subtitle batches may cause API rate limits. You can tweak BATCH_SIZE in the code if needed.

    .ass format (Advanced SubStation Alpha) is not supported yet, but planned for future versions.

📄 License

MIT — Free to use, modify, and distribute.

Let me know if you'd like to add:

    📽️ GIF/video demo

    🌐 Live translation preview

    📂 Drag-and-drop GUI

    💬 Discord/Telegram bot version

I can help you upgrade the repo anytime!


