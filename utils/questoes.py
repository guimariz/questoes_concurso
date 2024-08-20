import re

def setar_questoes(nome, texto):
    padrao = r"(\d+)\s([^\n]+(?:\n[^\d]+)*)"

    questoes = re.findall(padrao, texto)
    questoes_dic = {}

    for questao in questoes:
        numero = questao[0]
        enunciado = ' '.join(questao[1].split())
        questoes_dic[numero] = enunciado

    return {'nome': nome, 'questoes': questoes_dic}
