import json

f = open('_metadata.json',)
count = 1
data = json.load(f)

for nft in data:
  description = nft['attributes'][0]['value'] + " background\n" + nft['attributes'][5]['value'] + " eyes\n" + nft['attributes'][2]['value'] + " skin\n" + nft['attributes'][1]['value'] + " beak\n" + nft['attributes'][3]['value'] + " clothe\n" + nft['attributes'][6]['value'] + " hat\n" + nft['attributes'][4]['value'] + " accesory"
  mensaje = {
			    "assetName": "ToughPenguin" + str(count),
			    "previewImageNft": {
			    "mimetype": "image/png",
			    "fileFromIPFS": "QmQu7DAi9k4aDXCbpzXdDxVuMtha5mWJgm58mZEPUsx6vQ/" + str(count) + ".png",
			    "description": description
			    }
			}
  y = json.dumps(mensaje)
  print(y)
  count += 1

f.close()
