import srt
import asyncio
import aiohttp
from deep_translator import GoogleTranslator

BATCH_SIZE = 20  


def load_srt_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    subtitles = list(srt.parse(content))
    return subtitles


def chunk_texts(subtitles, size):
    for i in range(0, len(subtitles), size):
        yield subtitles[i:i + size]


async def translate_text(session, text, target_lang):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={target_lang}&dt=t&q=" + aiohttp.helpers.quote(text)
    async with session.get(url) as resp:
        data = await resp.json()
        translated = ''.join([item[0] for item in data[0]])
        return translated


async def batch_translate(subs_chunks, target_lang):
    translated_subtitles = []
    async with aiohttp.ClientSession() as session:
        for chunk in subs_chunks:
            texts = [sub.content for sub in chunk]
            combined_text = ' ||| '.join(texts)
            translated_text = await translate_text(session, combined_text, target_lang)
            split_translations = translated_text.split(' ||| ')

            for i in range(len(chunk)):
                sub = chunk[i]
                sub.content = split_translations[i] if i < len(split_translations) else sub.content
                translated_subtitles.append(sub)
    return translated_subtitles


def save_srt_file(subtitles, output_path):
    translated_srt = srt.compose(subtitles)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated_srt)


async def main(input_file, output_file, target_lang):
    print("📥 downloading...")
    subtitles = load_srt_file(input_file)
    print(f"🎬 found: {len(subtitles)} subtitles")

    subs_chunks = list(chunk_texts(subtitles, BATCH_SIZE))

    print(f"🔁 Batching ({BATCH_SIZE})...")
    translated = await batch_translate(subs_chunks, target_lang)

    print("💾 Saving...")
    save_srt_file(translated, output_file)
    print(f"✅ : {output_file} ({target_lang} ")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("how to use: python translator.py input.srt output.srt ru/es/uz/...")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        target_lang = sys.argv[3]
        asyncio.run(main(input_file, output_file, target_lang))
