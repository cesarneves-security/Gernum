import os
import sys
from __designer__ import __designer_viws2__,__designer_viws__
#python3 __main__.py --C portugal --file nome_do_ficheiro.txt
global options_var
options_var = None
try:
    options_var = sys.argv[1]
    country = sys.argv[2]
    options_var2 = sys.argv[3]
    file_name = sys.argv[4]
except IndexError:
    if (options_var == "--help") or (options_var == "-h"):
        __designer_viws2__()
        print ("\33[3m"+"\33[1m"+" [I] INFORMAÇÃO DO <.GERNUM.>\n")
        print ("\33[3m"+"\33[1m"+""" 
 [?] --help/ -h = VER AS OPÇÕES DO GERNUM.
 [?] --C/ --c = LISTAR O NOME DO PAÍS <.angola/ portugal/ brasil/ moçambique.>.
 [?] --file = NOMEAR O FICHEIRO EM QUE OS DADOS SERÃO SALVOS.\n
 [<.EXEMPLO.>] Gernum --C angola --file AngolaNumber.txt
 [<.EXEMPLO.>] Gernum --C portugal --file PortugalNumber.txt
 [<.EXEMPLO.>] Gernum --C brasil --file BrasilNumber.txt
 [<.EXEMPLO.>] Gernum --C moçambique --file moçambiqueNumber.txt
""")
        exit()
    elif (options_var == "") or (options_var == " ") or (options_var == None):
        __designer_viws2__()
        print ("\33[3m"+"\33[1m"+" [+] FORMA DE USO: python3 __main__.py --C nome_do_pais --file nome_do_ficheiro")
        print ("\33[3m"+"\33[1m"+" [+] FORMA DE USO: python3 __main__.py --C angola --file angolaNumber.txt\n")
        exit()
    else:
        __designer_viws2__()
        print ("\33[3m"+"\33[1m"+" [+] FORMA DE USO: python3 __main__.py --C nome_do_pais --file nome_do_ficheiro")
        print ("\33[3m"+"\33[1m"+" [+] FORMA DE USO: python3 __main__.py --C angola --file angolaNumber.txt\n")
        exit()

from __gerNum__ import __main_execute__
if __name__ == "__main__":
    __code__execute__ = __main_execute__()
    __code__execute__.__execute__()


