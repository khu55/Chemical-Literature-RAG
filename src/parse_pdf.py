import fitz
from pathlib import Path

raw_dir = Path("data/raw")
out_dir = Path("data/processed")
out_dir.mkdir(parents=True, exist_ok=True)

for pdf_path in raw_dir.glob("*.pdf"):
    doc = fitz.open(pdf_path)

    text = ""
    for page in doc:
        text += page.get_text() + "\n"

    output_path = out_dir / f"{pdf_path.stem}.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Saved: {output_path}")