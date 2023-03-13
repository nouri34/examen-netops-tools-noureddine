"""
Opdracht:

Bepalingen:
 - Je moet gebruik maken van de aangeleverde variable(n)
 - Je mag deze variable(n) niet aanpassen
 - Het is de bedoeling dat je op het einde 1 programma hebt
 - Inlever datum is zondag avond 13 maart 2023 18:00CET
 - Als inlever formaat wordt een git url verwacht die gecloned kan worden

/ 5 ptn 1 - Maak een public repository aan op jouw gitlab/github account voor dit project
/10 ptn 2 - Gebruik python om de gegeven api url aan te spreken
/20 ptn 3 - Gebruik regex om de volgende data te extracten:
    - Jaar, maand en dag van de created date
    - De provider van de nameservers (bijv voor 'ns3.combell.net' is de provider 'combell')
/15 ptn 4 - Verzamel onderstaande data en output alles als yaml. Een voorbeeld vind je hieronder.
    - Het land van het domein
    - Het ip van het domain
    - De DNS provider van het domein
    - Aparte jaar, maand en dag van de created date


Totaal  /50ptn
"""

""" voorbeeld yaml output

created:
  dag: '18'
  jaar: '2022'
  maand: '02'
ip: 185.162.31.124
land: BE
provider: combell

"""

url = "https://api.domainsdb.info/v1/domains/search?domain=syntra.be"
import yaml
import requests
import re
import json

api_base_url = "https://api.domainsdb.info/v1/domains/search?domain=syntra.be"
response = requests.get(f"{api_base_url}/broadcast_messages")
print(response.status_code)
print(response.text)



json = requests.get('https://api.domainsdb.info/v1/domains/search?domain=syntra.be').json()
domains = json["domains"]
createddate = domains[0]["create_date"]
nameserver = domains[0]["NS"][0]
ip = domains[0]["A"][0]
jaar = re.match("([0-9]+)-([0-9]+)-([0-9]+)",createddate).group(1)
maand = re.match("([0-9]+)-([0-9]+)-([0-9]+)",createddate).group(2)
dag = re.match("([0-9]+)-([0-9]+)-([0-9]+)",createddate).group(3)
provider = re.search("\.([^\.]+)\.",nameserver).group(1)
land = domains[0]["country"]
config = [{'created': {'dag':dag,'jaar':jaar,'maand':maand}},
         {'ip': ip},{'land': land},{'provider':provider}]
print(yaml.dump(config))