import requests
from bs4 import BeautifulSoup

# Target URL
url = "https://www.nobroker.in/property/1-bhk-apartment-for-rent-in-18-12th-cross-rd-shreya-colony-jp-nagar-7th-phase-j--p--nagar-bengaluru-kothnur-karnataka-560078-india-bangalore-for-rs-14000/8a9fb4827d0d32b0017d0d64b5821870/detail?nbFr=list-rent"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
# Send request
response = requests.get(url, headers=headers)
print(response.status_code)  # should be 200
soup = BeautifulSoup(response.text, 'html.parser')
print("\n[INFO] All <span> tags with 'id' attribute:")
found = False
for span in soup.find_all("span"):
    if span.has_attr("id"):
        found = True
        print(f"Text: {span.get_text(strip=True)} | ID: {span['id']}")

if not found:
    print("No <span> elements with an 'id' attribute were found.")
target_text = "1 BHK Apartment for Rent in 18, 12th Cross Rd" 
span_with_text = soup.find("span", string=target_text)
if span_with_text:
    print(f"\n[INFO] Found span with text '{target_text}' and ID: {span_with_text.get('id')}")
else:
    print(f"\n[WARN] No span found with text: {target_text}")
