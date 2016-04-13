# O compilador oficial do Fausto C

import sys
import re

comandos = ( 'Conta pra gente' )

def abrir_arquivo(arquivo):
	dados = open(arquivo, "r").read()
	return dados

# Aqui acontece a magia do cinema, onde o filho chora e a mãe não vê, sério
def interpretar(conteudo):
	if(comandos in conteudo):
		parametro = conteudo.replace('Conta pra gente(\"', '')
		parametro = parametro.replace('\")', '')
		print(parametro)
		
def executar():
	dados = abrir_arquivo(sys.argv[1])
	interpretar(dados)

executar()