from pathlib import Path
import json
import re

processed_dir = Path("data/processed")
chunk_dir = Path("data/chunks")
chunk_dir.mkdir(parents=True, exist_ok=True)

max_chunk_size = 800
min_chunk_size = 150

all_chunks = []


def remove_headers_footers(text):
    text = re.sub(r"COMMUNICATIONS MATERIALS.*?www\.nature\.com/commsmat", "", text)
    text = re.sub(r"https://doi\.org/\S+", "", text)
    text = re.sub(r"REVIEW ARTICLE", "", text)
    text = re.sub(r"\n\d+\n", "\n", text)
    text = re.sub(r"\nOPEN\n", "\n", text)
    return text


def split_into_paragraphs(text):
    paragraphs = re.split(r"\n\s*\n", text)
    paragraphs = [p.strip() for p in paragraphs if len(p.strip()) > 30]
    return paragraphs


def split_long_paragraph(para):
    pieces = []
    start = 0

    while start < len(para):
        end = start + max_chunk_size

        cut = para.rfind(".", start, end)

        if cut == -1 or cut <= start + 100:
            cut = end
        else:
            cut = cut + 1

        piece = para[start:cut].strip()

        if len(piece) >= min_chunk_size:
            pieces.append(piece)

        start = cut

    return pieces


for txt_path in processed_dir.glob("*.txt"):
    text = txt_path.read_text(encoding="utf-8")
    text = remove_headers_footers(text)

    paragraphs = split_into_paragraphs(text)

    for para in paragraphs:
        if len(para) > max_chunk_size:
            pieces = split_long_paragraph(para)

            for piece in pieces:
                all_chunks.append({
                    "source": txt_path.name,
                    "text": piece
                })
        else:
            if len(para) >= min_chunk_size:
                all_chunks.append({
                    "source": txt_path.name,
                    "text": para
                })

output_path = chunk_dir / "chunks.json"

output_path.write_text(
    json.dumps(all_chunks, ensure_ascii=False, indent=2),
    encoding="utf-8"
)

print(f"Saved {len(all_chunks)} chunks to {output_path}")

max_len = max(len(chunk["text"]) for chunk in all_chunks)
print(f"Longest chunk length: {max_len}")