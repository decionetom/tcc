import pandas as pd
import json

def json_para_dataframe_com_head(caminho_arquivo_json, head_desejada):
    # Carregar o JSON para um dicionário
    with open(caminho_arquivo_json, 'r') as arquivo:
        data = json.load(arquivo)
    
    # Verificar se a cabeçalho desejada existe no JSON
    if head_desejada in data:
        # Criar o DataFrame usando apenas a cabeçalho desejada
        df = pd.DataFrame(data[head_desejada]['Materia'])
        caminho_arquivo_csv = 'trusted\saida.csv'

        df.to_csv(caminho_arquivo_csv, index=False)
        print(f"DataFrame salvo em '{caminho_arquivo_csv}' com sucesso.")
        return df
    else:
        print(f"A cabeçalho '{head_desejada}' não foi encontrada no JSON.")
        return None

# Exemplo de uso:
caminho_arquivo_json = 'trusted/materias.json'
head_desejada = 'Materias'
dataframe = json_para_dataframe_com_head(caminho_arquivo_json, head_desejada)





# Verificar se o DataFrame foi criado com sucesso
if dataframe is not None:
    # Agora você pode usar o DataFrame como quiser, por exemplo, exibir as primeiras linhas:
    print(dataframe.columns)
    primeiro_dicionario = dataframe["IdentificacaoMateria"].iloc[0]
    df = pd.DataFrame([primeiro_dicionario])
    print(df)