import sys
import os

sys.path.append('src')
from identity_ocr.mrz import parse_mrz

mrz_td3 = """P<UTOERIKSSON<<ANNA<MARIA<<<<<<<<<<<<<<<<<<<
L898902C36UTO6908061F9406236ZE184226B<<<<<14"""

print("TD3 Input:")
print(mrz_td3)
print("Result:")
print(parse_mrz(mrz_td3))

mrz_td1 = """I<UTOD231458907<<<<<<<<<<<<<<<
7408122F1204159UTO<<<<<<<<<<<6
ERIKSSON<<ANNA<MARIA<<<<<<<<<<"""

print("\nTD1 Input:")
print(mrz_td1)
print("Result:")
print(parse_mrz(mrz_td1))
