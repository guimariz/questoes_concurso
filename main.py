from utils.extrair_pdf import *
from utils.questoes import *
from utils.adicionar_prova_mongo import *

nome_prova = 'fgv-analista-segurança-ti-tjms'
nome_banca = nome_prova.split('-')[0]
caminho_pdf = f'./data/provas/{nome_prova}.pdf'

texto = extrair_texto_do_pdf(caminho_pdf)

# questoes = setar_questoes_ce("cebraspe-cti-especifica", texto)
questoes = setar_questoes_ae(nome_prova, nome_banca, texto)

# print(questoes)

criar_banco('provas_concursos_ti', nome_prova, questoes)

