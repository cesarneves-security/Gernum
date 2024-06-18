import os
choice = input('[+] PARA INSTALAR PRESS (Y)/ PARA REMOVER PRESS (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 __main__.py')
    run('mkdir /usr/share/Gernum')
    run('cp -r * /usr/share/Gernum')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/Gernum/__main__.py "$@"')
    with open('/usr/bin/Gernum','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/Gernum & chmod +x /usr/share/Gernum/__main__.py')
    print('''\n\n FERRAMENTA INSTALADA COM SUCESSO...''')
if str(choice)=='N' or str(choice)=='n':
    os.system("clear")
    print(" [X] SAINDO...")
    exit()
