import time
import sys
import os
sys.path.append('src')
from identity_ocr import read_passport
import cv2
import numpy as np

# Create a dummy passport image for testing if one doesn't exist
# Or use an existing one if available.
# I'll create a synthetic one with text to ensure Tesseract has something to do.

def create_dummy_image():
    # 4K resolution (approx)
    img = np.ones((3000, 4000, 3), dtype=np.uint8) * 255
    
    # Simulate Photo on Left (Gray box)
    cv2.rectangle(img, (100, 500), (1300, 2100), (200, 200, 200), -1)
    cv2.putText(img, "PHOTO", (400, 1300), cv2.FONT_HERSHEY_SIMPLEX, 5, (100, 100, 100), 10)
    
    # Add Text on Right (Visual Zone)
    # Place of Issue is usually what we look for in full text
    cv2.putText(img, "PASSPORT", (1500, 300), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 10)
    cv2.putText(img, "Surname / Nom", (1500, 600), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 100, 100), 4)
    cv2.putText(img, "DOE", (1500, 750), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)
    
    cv2.putText(img, "Given Names / Prenoms", (1500, 900), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 100, 100), 4)
    cv2.putText(img, "JOHN", (1500, 1050), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)
    
    cv2.putText(img, "Date of birth / Date de naissance", (1500, 1200), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 100, 100), 4)
    cv2.putText(img, "01 JAN / JAN 1980", (1500, 1350), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)
    
    cv2.putText(img, "Place of issue / Lieu de delivrance", (1500, 1500), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 100, 100), 4)
    cv2.putText(img, "WASHINGTON, USA", (1500, 1650), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)
    
    cv2.putText(img, "Date of issue / Date de delivrance", (1500, 1800), cv2.FONT_HERSHEY_SIMPLEX, 2, (100, 100, 100), 4)
    cv2.putText(img, "01 JAN / JAN 2015", (1500, 1950), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 5)

    # Add MRZ
    mrz_font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "P<USADOE<<JOHN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<", (150, 2400), mrz_font, 3.5, (0, 0, 0), 5)
    cv2.putText(img, "1234567897USA8001019M2501015<<<<<<<<<<<<<<<<<<", (150, 2600), mrz_font, 3.5, (0, 0, 0), 5)
    
    cv2.imwrite("benchmark_passport.jpg", img)
    return "benchmark_passport.jpg"

img_path = create_dummy_image()

print("Starting benchmark...")
start_time = time.time()
for i in range(3):
    print(f"Run {i+1}...")
    t0 = time.time()
    res = read_passport(img_path)
    t1 = time.time()
    print(f"  Total: {t1-t0:.4f}s")
    
end_time = time.time()

avg_time = (end_time - start_time) / 3
print(f"Average time per call: {avg_time:.4f} seconds")
print(res)
