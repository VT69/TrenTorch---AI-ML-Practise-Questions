import fitz
import sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open('out/main.pdf')
print(f"Pages: {doc.page_count}")

page = doc[0]
if doc.page_count > 1:
    print("\n--- PAGE 2 ---")
    print(doc[1].get_text("text")[:500])
print("\n--- TEXT EXTRACTION ---")
print(page.get_text("text")[:500])  # Print first 500 chars to verify

print("\n--- COLLISION CHECK ---")
blocks = page.get_text("dict")["blocks"]

lines = []
for block in blocks:
    if "lines" in block:
        for line in block["lines"]:
            text_parts = []
            min_x = 9999
            max_x = 0
            for span in line["spans"]:
                if span["text"].strip():
                    text_parts.append((span["text"], span["bbox"]))
            if len(text_parts) >= 2:
                # Compare the leftmost and rightmost parts of a line
                # specifically checking the longest lines as mentioned in the prompt
                pass
            
            # Print long lines to see coordinates
            full_text = "".join([t[0] for t in text_parts])
            if "Software Engineering Intern" in full_text or "AlphaVol-NeuralHAR" in full_text or "NexusRAG" in full_text:
                print(f"LINE: {full_text}")
                # We need to find the gap between the title and the right-aligned text.
                # Usually, they are in different spans within the same line.
                if len(text_parts) >= 2:
                    left_text = text_parts[0][0]
                    left_max = text_parts[0][1][2] # x1 of first span
                    
                    right_text = text_parts[-1][0]
                    right_min = text_parts[-1][1][0] # x0 of last span
                    
                    gap = right_min - left_max
                    print(f"  Left part ends at: {left_max:.2f}")
                    print(f"  Right part starts at: {right_min:.2f}")
                    print(f"  Gap (pts): {gap:.2f}")

doc.close()
