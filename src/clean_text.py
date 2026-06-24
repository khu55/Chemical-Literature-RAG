from pathlib import Path
import re

processed_dir = Path("data/processed")

def clean_text(text):
    text = re.sub(
        r'(\w)-\n(\w)',
        r'\1\2',
        text
    )

    text = text.replace("ﬀ", "ff")
    text = text.replace("ﬁ", "fi")
    text = text.replace("ﬂ", "fl")
    text = text.replace("ﬃ", "ffi")
    text = text.replace("ﬄ", "ffl")

    return text

for txt_path in processed_dir.glob("*.txt"):
    text = txt_path.read_text(encoding="utf-8")
    cleaned = clean_text(text)
    txt_path.write_text(cleaned, encoding="utf-8")

    print(f"Cleaned: {txt_path.name}")