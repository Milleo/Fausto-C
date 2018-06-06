import FaustoC.parser as parser

def execute(codigoFonte):
    res = parser.get_parser().parse(codigoFonte)
    print(res)