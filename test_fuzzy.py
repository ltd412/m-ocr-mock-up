from difflib import get_close_matches

known_places = [
    "Cuc Quan ly xuat nhap canh",
    "Immigration Department"
]

bad_ocr = "Cuc Quén 1y xudt nhap canh"

print(f"Bad OCR: {bad_ocr}")

# Try exact match (normalized)
# ...

# Try fuzzy match
matches = get_close_matches(bad_ocr, known_places, n=1, cutoff=0.6)
print(f"Fuzzy Matches: {matches}")

if matches:
    print(f"Corrected: {matches[0]}")
else:
    print("No correction found.")
