import sys
import os

sys.path.append('src')
from identity_ocr.mrz import parse_mrz

mrz_lines = """PPCANMARTIN<<LKSARAH<<LLLLLLLLLLLLLLLLLLLLLKLLLKLKL
P123456AA0CAN9008010F3301144<<<<<<<<<LKLKLKL<L<<LKO6"""

print("Input MRZ:")
print(mrz_lines)
print("\nResult:")
result = parse_mrz(mrz_lines)
print(result)

if 'warning' in result:
    print("\nIssue Reproduced: Warning found.")
else:
    print("\nIssue Not Reproduced: Parsed successfully.")
