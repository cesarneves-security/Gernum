import os
choice = "y"
run = os.system
if str(choice)=='Y' or str(choice)=='y':
    run('rm -r /usr/share/Gernum ')
    run('rm /usr/bin/Gernum ')
    print('[!] FERRAMENTA REMOVIDA COM SUCESSO!')

