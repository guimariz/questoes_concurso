import re

def setar_questoes_ce(nome, nome_banca, texto):
    padrao = r"(\d+)\s([^\n]+(?:\n[^\d]+)*)"

    questoes = re.findall(padrao, texto)
    questoes_dic = {}

    for questao in questoes:
        numero = questao[0]
        if int(numero) >= 51:
            enunciado = ' '.join(questao[1].split())
            questoes_dic[numero] = enunciado

    return {'nome': nome, 'nome_banca': nome_banca, 'questoes': questoes_dic}

def setar_questoes_ae(nome, nome_banca, texto):
    padrao = r"(?P<numero>\d+)\s*\n(?P<enunciado>.+?(?=\s*\n\([ABCDE]\)))\s*\n\(A\)\s*(?P<alternativaA>.+?)\s*\n\(B\)\s*(?P<alternativaB>.+?)\s*\n\(C\)\s*(?P<alternativaC>.+?)\s*\n\(D\)\s*(?P<alternativaD>.+?)\s*\n\(E\)\s*(?P<alternativaE>.+?)"

    questoes = re.finditer(padrao, texto, re.DOTALL)
    questoes_dic = {}

    for questao in questoes:
        numero = questao.group("numero")
        enunciado = ' '.join(questao.group("enunciado").split())
        alternativas = {
            "A": ' '.join(questao.group("alternativaA").split()),
            "B": ' '.join(questao.group("alternativaB").split()),
            "C": ' '.join(questao.group("alternativaC").split()),
            "D": ' '.join(questao.group("alternativaD").split()),
            "E": ' '.join(questao.group("alternativaE").split())
        }
        questoes_dic[numero] = {"enunciado": enunciado, "alternativas": alternativas}

    return {'nome': nome, 'nome_banca': nome_banca, 'questoes': questoes_dic}

