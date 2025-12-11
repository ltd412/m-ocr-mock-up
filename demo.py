import sys
import os

# Add src to path so we can import the library without installing it
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from passport_ocr import read_passport

def main():
    # if len(sys.argv) < 2:
    #     print("Usage: python demo.py <path_to_passport_image>")
    #     sys.exit(1)

    # image_path = "/home/ltd/Pictures/Screenshots/Screenshot from 2025-12-11 14-07-00.png"
    image_path = "/home/ltd/Downloads/hinh-anh-thong-tin-trong-ho-chieu.jpg"
    # image_path = "/home/ltd/Downloads/ltd.jpg"
    
    if not os.path.exists(image_path):
        print(f"Error: File {image_path} not found.")
        sys.exit(1)

    print(f"Processing {image_path}...")
    


    result = read_passport(image_path)
    
    import pprint
    print("--- Result from File Path ---")
    pprint.pprint(result)
    
    # Test Base64
    print("\n--- Testing Base64 Input ---")
    # import base64
    # with open(image_path, "rb") as image_file:
    #     encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
    # Add header to simulate data URI (optional, but good to test)
    # base64_input = f"data:image/jpeg;base64,{encoded_string}"
    
    result_b64 = read_passport(image_path)
    pprint.pprint(result_b64)
    
    if 'raw_mrz' in result:
        print("Line lengths:")
        for line in result['raw_mrz']:
            print(f"'{line}': {len(line)}")

if __name__ == "__main__":
    main()
