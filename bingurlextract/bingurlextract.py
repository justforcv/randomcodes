import argparse
import re
import base64
import json
import urllib.parse

def extract_redirect_url(url, success_count, failure_count):
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    if 'u' in query_params:
        u_param = query_params['u'][0]
        # Remove "a1" if followed by "aH"
        u_param = re.sub(r'a1(?=aH)', '', u_param)
        print("u:", u_param)
        # Pad the base64 encoded string if needed
        padding_needed = len(u_param) % 4
        u_param += '=' * padding_needed
        try:
            # Decode the base64 encoded string
            decoded_bytes = base64.b64decode(u_param)
            # Decode the decoded bytes into a string
            decoded_string = decoded_bytes.decode('utf-8')
            print("Decoded String:", decoded_string)
            success_count += 1
            return {'original_url': url, 'extracted_string': u_param, 'decoded_url': decoded_string}, success_count, failure_count
        except Exception as e:
            print("Base64 decoding error:", e)
            failure_count += 1
    return None, success_count, failure_count

def process_urls(input_file, output_file):
    success_count = 0
    failure_count = 0
    output_data = []
    with open(input_file, 'r') as file:
        for line in file:
            url = line.strip()
            print("\nURL:", url)
            extracted_data, success_count, failure_count = extract_redirect_url(url, success_count, failure_count)
            if extracted_data:
                output_data.append(extracted_data)
    
    with open(output_file, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)
    
    print("\nExtraction Summary:")
    print("Successful Extractions:", success_count)
    print("Failed Extractions:", failure_count)

def main():
    parser = argparse.ArgumentParser(description="Extract 'u' parameter from Bing URLs and store in JSON")
    parser.add_argument("input_file", help="Text file containing Bing URLs")
    parser.add_argument("output_file", help="JSON file to store extracted data")
    args = parser.parse_args()

    process_urls(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
