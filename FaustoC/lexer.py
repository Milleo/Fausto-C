import ply.lex as lex

reserved = {}

tokens = [
    'NUMERO',
    'SOMA',
    'SUBTR',
    'MULTIP',
    'DIVISAO',
    'APAREN',
    'FPAREN'
]

t_NUMERO = r'\d+'
t_SOMA = r'\+'
t_SUBTR = r'\-'
t_MULTIP = r'\*'
t_DIVISAO = r'/'
t_APAREN = r'\('
t_FPAREN = r'\)'
