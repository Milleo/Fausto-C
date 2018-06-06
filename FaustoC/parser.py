import ply.yacc as yacc
from FaustoC.lexer import *


def get_parser():
    return yacc.yacc()