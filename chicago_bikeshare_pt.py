"""
chicago.bikeshare_pt.py

Projeto 1 do Nanodegree Fundamentos de AI & Machine Learning da Udacity. O Projeto em Python consiste na exploração de
dados relacionados aos sistemas de compartilhamento de bicicletas. O código entregue importa os dados de uma arquivo CSV
e responde a algumas perguntas sobre eles. O script recebe uma entrada bruta que cria uma experiência interativa no
terminal, a fim de apresentar estas estatísticas.

Exercício entregue em 07/10/2018 (Prazo máximo: 25/10/2018)

@author: Rafael Vidal
"""
# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt


# Importa os dados do CSV em uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas: {}".format(len(data_list)))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
# É o cabeçalho dos dados, para que possamos identificar as colunas.
print("Linha 0.........: {}".format(data_list[0]))

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1.........: {}".format(data_list[1]))

input("Aperte Enter para continuar...")


# --------------------------------------------------------------------------------
# TAREFA 1
# ========
#
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
# --------------------------------------------------------------------------------
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for row, data in enumerate(data_list[0: 20]):
    print("Row {}: {}".format(row+1, data))

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:len(data_list)]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")


# --------------------------------------------------------------------------------
# TAREFA 2
# ========
#
# TODO: Imprima o `gênero` das primeiras 20 linhas
# --------------------------------------------------------------------------------
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for row, data in enumerate(data_list[0: 20]):
    print("Row {}: {}".format(row+1, data[6]))

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")


# --------------------------------------------------------------------------------
# TAREFA 3
# ========
#
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# --------------------------------------------------------------------------------
def column_to_list(data_list: list, index: int) -> list:
    """
    Adiciona as colunas(features) de uma lista em outra lista, na mesma ordem

    Attributes:
        data_list (list): Lista de dados
        index (int): Índice da coluna a ser buscada

    Returns:
        list: Retorna uma list simples com a coluna desejada
    """
    # iteraração sobre as amostras, pegando a feature pelo seu índice, e inserindo na lista 'column_list'
    column_list = []
    for row in data_list:
        column_list.append(row[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem


# --------------------------------------------------------------------------------
# TAREFA 4
# ========
#
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
# --------------------------------------------------------------------------------
genere_list = column_to_list(data_list, -2)

# Contagem de "Male" utilizando lambda
male = len(list(filter(lambda genere: genere == "Male", genere_list)))

# Contagem de "Female" utilizando uma maneira mais "limpa" de fazer a contagem
female = genere_list.count("Female")

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?


# --------------------------------------------------------------------------------
# TAREFA 5
# ========
#
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female]
#
# Exemplo:
# --------
#   [10, 15] significa 10 Masculinos, 15 Femininos
# --------------------------------------------------------------------------------
def count_gender(data_list: list) -> list:
    """
    Função que retorna uma lista indicando os gênereos

    Attributes:
        data_list (list): Lista dos dados

    Returns:
        list: Retorna uma lista com [count_male, count_female] (ex.: [10, 15] significa 10 Masculinos, 15 Femininos)
    """
    male = 0
    female = 0
    for i, data in enumerate(data_list):
        if data[-2] == "Male":
            male += 1
        elif data[-2] == "Female":
            female += 1
        else:
            # Neither Male and Female
            pass
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?


# --------------------------------------------------------------------------------
# TAREFA 6
# ========
#
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
# --------------------------------------------------------------------------------
def most_popular_gender(data_list: list) -> str:
    """
    Retorna o gênero mais popular

    Attributes:
        data_list (list): Lista dos dados

    Returns:
        str: Retorna "Male", "Female", ou "Equal" como resposta.
    """
    count_male, count_female = count_gender(data_list)
    if count_male > count_female:
        answer = "Male"
    elif count_male < count_female:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")


# --------------------------------------------------------------------------------
# TAREFA 7
# ========
#
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
# --------------------------------------------------------------------------------

user_types = column_to_list(data_list, -3)
types = list(set(user_types))
quantity = [user_types.count(type) for type in types]

y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)
print("\nTAREFA 7: Verifique o gráfico!")
input("Aperte Enter para continuar...")


# --------------------------------------------------------------------------------
# TAREFA 8
# ========
#
# TODO: Responda a seguinte questão
# --------------------------------------------------------------------------------
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = """O motivo pelo qual a soma de usuários de ambos os sexos não bate com 
            o total de registros da lista é que existem registros vazios."""
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.


# --------------------------------------------------------------------------------
# TAREFA 9
# ========
#
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
# --------------------------------------------------------------------------------
def calculate_median(data_list: list) -> int:
    """
    Calcula o valor mediano.

    Referência:
    Rotina retirada do site Stack Overflow (https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python)

    Attributes:
        data_list (list): Lista dos dados

    Returns:
        int: Retorna o valor mediano
    """
    quotient, remainder = divmod(len(data_list), 2)
    if remainder:
        return sorted(data_list)[quotient]
    return sum(sorted(data_list)[quotient - 1:quotient + 1]) / 2.


trip_duration_list = list(map(int, column_to_list(data_list, 2)))
min_trip = sorted(trip_duration_list)[0]
max_trip = sorted(trip_duration_list)[-1]
mean_trip = sum(trip_duration_list) / float(len(trip_duration_list))
median_trip = calculate_median(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# --------------------------------------------------------------------------------
# TAREFA 10
# =========
#
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
# --------------------------------------------------------------------------------
start_stations = sorted(set(column_to_list(data_list, 3)))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")


# --------------------------------------------------------------------------------
# TAREFA 11
# =========
#
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
# --------------------------------------------------------------------------------
"""
Função de exemplo com anotações.
Argumentos:
  param1: O primeiro parâmetro.
  param2: O segundo parâmetro.
Retorna:
  Uma lista de valores x.

"""
input("Aperte Enter para continuar...")


# --------------------------------------------------------------------------------
# TAREFA 12 - Desafio! (Opcional)
# ===============================
#
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
# --------------------------------------------------------------------------------
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"
print("Resposta: Yes -> Desafio aceito!")


def count_items(column_list: list) -> list:
    """
    Contar todos tipos de usuários, sem definir os tipos

    Attributes:
        column_list (list): Lista de tipos de usuários

    Returns:
        list: Lista com contagem de todos os tipos de usuários
    """
    item_types = list(set(column_list))
    count_items = []
    for type in item_types:
        count_items.append(column_list.count(type))
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
