webpage_to_parse = "https://mevzuat.gov.tr/anasayfa/MevzuatFihristDetayIframe?MevzuatTur=1&MevzuatNo=2709&MevzuatTertip=5"

import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

response = requests.get(webpage_to_parse)
soup = BeautifulSoup(response.content, "html.parser")

for line in soup.get_text().split("\n"):
    if line.strip():
        print(line)
