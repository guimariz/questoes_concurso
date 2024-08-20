from utils.extrair_pdf import *
from utils.questoes import *
from utils.adicionar_prova_mongo import *

caminho_pdf = './data/provas/cebraspe-cti-especifica.pdf'

texto = extrair_texto_do_pdf(caminho_pdf)

questoes = setar_questoes("cebraspe-cti-especifica", texto)






# criar_banco('provas_concursos_ti', 'cebraspe-cti-especifica', questoes)

