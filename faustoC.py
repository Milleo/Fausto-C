import FaustoC
import sys

if len(sys.argv) == 1:
    print("Como usar: %s nome do arquivo" % __file__)
else:
    with open(sys.argv[1]) as f:
        FaustoC.execute(f.read())