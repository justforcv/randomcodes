# Bing URL Extractor

This Python script extracts 'u' parameters from Bing URLs, decodes them, and stores the results in a JSON file.

## Motivation
The `http://bing.com/ck/a` is a URL redirection service provided by Bing. It is used to redirect users from one website to another. When a user clicks on a link that uses `http://bing.com/ck/a`, they are redirected to the destination website.

This service is often used by marketers to track clicks on their links. When a user clicks on a link that uses `http://bing.com/ck/a`, the marketer can track the click and determine how many people clicked on the link.

However, cybercriminals can also use `http://bing.com/ck/a` to spread malicious links. They can create a link that appears to be a legitimate website, but when a user clicks on the link, they are redirected to a malicious website.

Modus operandi in news
- [Novel phishing ploy uses QR codes, Bing URL redirects, fake Microsoft security alerts](https://www.scmagazine.com/news/novel-phishing-qr-codes-bing-url-microsoft-security)
- [QR codes used to phish for Microsoft credentials](https://www.malwarebytes.com/blog/news/2023/08/qr-codes-deployed-in-targeted-phishing-campaigns)

## Usage

1. **Input File**: Provide a text file containing Bing URLs as input to the script.

2. **Output File**: The script will generate a JSON file with the extracted data.

### Running the Script

```bash
python script_name.py input.txt output.json
```

### Data Source

The initial Bing URLs were extracted from urlscan.io. 

---

# Thanks!
