import json
import csv

from data_processing import Data


# def reading_json(path_json):
    
#     dados_json = []
#     with open(path_json, 'r') as file:
#         dados_json = json.load(file)
    
#     return dados_json


# def reading_csv(path_csv):    
    
#     dados_csv = []
#     with open(path_csv, 'r') as file:
#         spamreader = csv.DictReader(file, delimiter=',')
#         for row in spamreader:
#             dados_csv.append(row)

#     return dados_csv


# def reading_data(path, file_type):
#     dados = []

#     if file_type == 'json':
#         dados = reading_json(path)
#     elif file_type == 'csv':
#         dados = reading_csv(path)
#     else:
#         print('Tipo de arquivo não suportado')
    
#     return dados


# def get_columns(dados):
#     return list(dados[-1].keys())

# def rename_columns(dados, key_mapping):
#     new_dados_csv = []

#     for old_dict in dados:
#         dict_temp = {}
#         for old_key, value in old_dict.items():
#             dict_temp[key_mapping[old_key]] = value
#     new_dados_csv.append(dict_temp)
        
#     return new_dados_csv


def size_data(dados):
    return len(dados)


def join_data(dadosA, dadosB):
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)

    return combined_list


def transform_data_table(dados, nome_colunas):
    dados_combinados_tabela = []
    for row in dados:
        linha = []
        for coluna in nome_colunas:
            linha.append(row.get(coluna, 'Indisponível'))
        dados_combinados_tabela.append(linha)
        
    return dados_combinados_tabela


def save_data(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        for row in dados:
            writer.writerows(dados)


path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#Extracting data

data_enterpriseA = Data(path_json, 'json')
print(data_enterpriseA.column_name)


data_enterpriseB = Data(path_csv, 'csv')

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

data_enterpriseB.rename_columns(key_mapping)

print(data_enterpriseB.column_name)

# # Iniciando a leitura
# dados_json = reading_data(path_json,'json')
# nome_colunas_json = get_columns(dados_json)
# tamanho_dados_json = size_data(dados_json)


# print(f"Nome colunas dados json: {nome_colunas_json}")
# print(f"Tamanho dos dados json: {size_data(dados_json)}")


# dados_csv = reading_data(path_csv, 'csv')
# nome_colunas_csv = get_columns(dados_csv)
# tamanho_dados_csv = size_data(dados_csv)

# print(nome_colunas_csv)
# print(f'Tamanho dos dados csv: {tamanho_dados_csv}')


# #Transformacao dos dados



# dados_csv = rename_columns(dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)
# print(nome_colunas_csv)

# dados_fusao = join_data(dados_json, dados_csv)
# nomes_colunas_fusao = get_columns(dados_fusao)
# tamanho_dados_fusao = size_data(dados_fusao)
# print(nomes_colunas_fusao)
# print(tamanho_dados_fusao)


# #Salvando os dados
# dados_fusao_tabela = transform_data_table(dados_fusao, nomes_colunas_fusao)

# path_dados_combinados = 'data_processed/dados_combinados.csv'

# save_data(dados_fusao_tabela, path_dados_combinados)

# print(f'Dados salvos em {path_dados_combinados}')