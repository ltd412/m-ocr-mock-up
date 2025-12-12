import sys
sys.path.append('src')
from m_identify_ocr.mrz import parse_mrz

# Noisy MRZ simulating 'Sarah Lklk...'
# SARAH followed by LKLK... which should be cleaned
mrz_lines = """PPCANMARTIN<<SARAH<LKLKLLLLLLLLLLLLLLLLLLLL
P123456AA0CAN9008010F3301144<<<<<<<<<LKLKLKL<L<<LKO6"""

print("Input MRZ:")
print(mrz_lines)
print("\nResult:")
result = parse_mrz(mrz_lines)
print(result)
