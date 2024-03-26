import requests

# Função para baixar o XML online e salvar localmente
def download_and_save_xml(url, local_filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print(f"XML baixado e salvo como {local_filename} com sucesso!")
    else:
        print("Falha ao baixar o XML.")

# URL do arquivo XML online
url = "https://legis.senado.leg.br/dadosabertos/materia/atualizadas?sigla=PL&numdias=5"  # Substitua pelo seu URL XML

# Nome do arquivo local para salvar o XML
local_filename = "./landing/landing.xml"  # Nome do arquivo local que você deseja salvar

# Baixar o XML e salvar localmente
download_and_save_xml(url, local_filename)
