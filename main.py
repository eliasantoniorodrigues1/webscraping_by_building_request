import requests
import json
import pprint
from time import sleep
import pandas as pd

def tag_collect(id_uf):
  '''
    this function will collect all tags from tourist municipalies in Brazil
  '''
  url = "http://sidtur.turismo.gov.br/sidtur-backend/rest/consulta-externa/todos"

  payload = json.dumps({
    "currentPage": 1,
    "pageSize": 15,
    "filtros": {
      "idUf": id_uf,
      "nomMunicipio": None,
      "nomDestino": None,
      "nomAtrativo": None,
      "nomProducao": None,
      "tags": [],
      "tagsId": []
    }
  })
  headers = {
    'Content-Type': 'application/json',
    'Cookie': 'JSESSIONID=gEkBNn7k12zIwYw_kk6eD9gdu98Q6jU5nLCZSrd7.pvlsede045'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  return response

if __name__ == '__main__':
  consolidado = []
  for i in range(1,28):
    r = tag_collect(id_uf=i)
    d = json.loads(r.text)
    df = pd.DataFrame(d['list'])
    df.to_csv(f'df_codmun_{i}.csv')
    consolidado.append(df)
    sleep(1.5)
    
  # saving collected data
  df_final = pd.concat(consolidado)
  df_final.to_csv('df_final.csv')
