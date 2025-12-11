import sys
import os

sys.path.append('src')
from identity_ocr.mrz import parse_mrz

mrz_lines = """P<VNMCHAU<<HA<YEN<NHI<<<LLLLLLLLLLKLKL
B7902778<3VNM7707021F230411502299376"""

print("Input MRZ:")
print(mrz_lines)
print("\nResult:")
result = parse_mrz(mrz_lines)
print(result)

if 'warning' in result:
    print("\nIssue Reproduced: Warning found.")
else:
    print("\nIssue Not Reproduced: Parsed successfully.")
