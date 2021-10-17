import json
import requests
from requests.structures import CaseInsensitiveDict

f = open('_metadata.json',)
count = 1
data = json.load(f)
url = 'https://api.nft-maker.io/UploadNft/45695b5532024df8804631b51f5e5124/19651'
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

for nft in data:
  mensaje = {
			    "assetName": "ToughPenguin" + str(count),
			    "previewImageNft": {
			    "mimetype": "image/png",
			    "fileFromIPFS": "QmQu7DAi9k4aDXCbpzXdDxVuMtha5mWJgm58mZEPUsx6vQ/" + str(count) + ".png",
			    "description": "10k Tough Penguins rockin' on the Cardano blockchain"
			    }
			}
  resp = requests.post(url, headers=headers, data=json.dumps(mensaje))
  print(resp.text)
  count += 1

f.close()
