import os
import sys
import random
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from __designer__ import __designer_viws__,__designer_viws2__
import time
__code_ao__ = "+2449"
__code_pt__ = "+3519"
__code_mq__ = "+2582"
__code_br__ = "+5519"
class __main__:
    def __init__(self):
        os.system("clear")
        __designer_viws__()
        #print ("\33[1m"+"\33[31m"+"\n [+] 1 -\33[0m \33[1mANGOLA \33[31m[+] 2 -\33[0m \33[1mPORTUGAL\n \33[31m[+] 3 -\33[0m \33[1mBRASIL \33[31m[+] 4 -\33[0m \33[1mMOÇAMBIQUE\n"+"\33[0m")
class __main_execute__(__main__):
    def __execute__(self):
        while True:
            #__choice__ = input ("\33[1m [?]:: ")
            from __main__ import options_var
            from __main__ import country
            from __main__ import options_var2
            from __main__ import file_name

            #ANGOLA
            if (country.lower() == "angola"):
                #print (" ANGOLA")
                for __numberPhone__ in range(48524979,999999999):
                    __designer_viws2__()
                    #time.sleep(1)
                    __number_complete = str(__code_ao__)+str(__numberPhone__)
                    phone_number = phonenumbers.parse(__number_complete)
                    #print (len(__number_complete), __number_complete)
                    num_ctive = 0
                    num_offline = 0
                    
                    if (phonenumbers.is_valid_number(phone_number) == True):
                        #print (__number_complete)
                        num_ctive = num_ctive + 1
                        country_code = phone_number.country_code
                        national_number = phone_number.national_number
                        time_zone = timezone.time_zones_for_number(phone_number)
                        location = geocoder.description_for_number(phone_number, "en")
                        service_provider = carrier.name_for_number(phone_number, "en")
                        all_localize = str(time_zone)
                        continente, countrys = all_localize.split('/',2)
                        print ("\n \33[97m=================================")
                        print(" \33[97m=[+]\33[0m\33[96m NÚMERO:", "+"+str(country_code)+str(national_number))
                        print(" \33[97m=[+]\33[0m\33[96m CÓDIGO DO PAÍS:", "+"+str(country_code))
                        print(" \33[97m=[+]\33[0m\33[96m NÚMERO DE ANGOLA:", national_number)
                        print(" \33[97m=[+]\33[0m\33[96m OPERADORA:", service_provider)
                        print(" \33[97m=[+]\33[0m\33[96m CONTINENTE:", continente[2:])
                        print(" \33[97m=[+]\33[0m\33[96m LOCALIZAÇÃO:","PAIS:", location)
                        print(" \33[97m=[+]\33[0m\33[96m LOCALIZAÇÃO:","PROVINCIA:", countrys[:-3])
                        print (" \33[97m=================================")
                        arquivo = open(file_name, 'a')
                        os.system('chmod 777 *')
                        arquivo.writelines("ATIVO: {}\n".format(__number_complete))
                        #os.system("clear")
                    else:
                        num_offline = num_offline + 1

            #Portugal
            if (country.lower() == "portugal"):
                #print (" portugal")
                for __numberPhone__ in range(26458476,999999999):
                    __designer_viws2__()
                    #time.sleep(1)
                    __number_complete = str(__code_pt__)+str(__numberPhone__)
                    phone_number = phonenumbers.parse(__number_complete)
                    #print (len(__number_complete), __number_complete)
                    num_ctive = 0
                    num_offline = 0
                    
                    if (phonenumbers.is_valid_number(phone_number) == True):
                        #print (__number_complete)
                        num_ctive = num_ctive + 1
                        country_code = phone_number.country_code
                        national_number = phone_number.national_number
                        time_zone = timezone.time_zones_for_number(phone_number)
                        location = geocoder.description_for_number(phone_number, "en")
                        service_provider = carrier.name_for_number(phone_number, "en")
                        all_localize = str(time_zone)
                        #continente, countrys = all_localize.split('/',2)
                        print ("\n \33[97m=================================")
                        print(" \33[97m=[+]\33[0m\33[96m NÚMERO:", "+"+str(country_code)+str(national_number))
                        print(" \33[97m=[+]\33[0m\33[96m CÓDIGO DO PAÍS:", "+"+str(country_code))
                        print(" \33[97m=[+]\33[0m\33[96m NÚMERO DE PORTUGAL:", national_number)
                        print(" \33[97m=[+]\33[0m\33[96m OPERADORA:", service_provider)
                        print(" \33[97m=[+]\33[0m\33[96m ALL INFO:", all_localize)
                        print(" \33[97m=[+]\33[0m\33[96m LOCALIZAÇÃO:","PAIS:", location)
                        print (" \33[97m=================================")
                        arquivo = open(file_name, 'a')
                        os.system('chmod 777 *')
                        arquivo.writelines("ATIVO: {}\n".format(__number_complete))
                        #os.system("clear")
                    else:
                        num_offline = num_offline + 1
            
            #MOÇAMBIQUE
            if (country.lower() == "moçambique"):
                #print (" MOÇAMBIQUE")
                for __numberPhone__ in range(6043867,999999999):
                    __designer_viws2__()
                    #time.sleep(1)
                    __number_complete = str(__code_mq__)+str(__numberPhone__)
                    phone_number = phonenumbers.parse(__number_complete)
                    #print (len(__number_complete), __number_complete)
                    num_ctive = 0
                    num_offline = 0
                    
                    if (phonenumbers.is_valid_number(phone_number) == True):
                        num_ctive = num_ctive + 1
                        country_code = phone_number.country_code
                        national_number = phone_number.national_number
                        time_zone = timezone.time_zones_for_number(phone_number)
                        location = geocoder.description_for_number(phone_number, "en")
                        service_provider = carrier.name_for_number(phone_number, "en")
                        all_localize = str(time_zone)
                        continente, countrys = all_localize.split('/',2)
                        print ("\n \33[97m=================================")
                        print(" \33[97m=[+]\33[0m\33[96m NÚMERO:", "+"+str(country_code)+str(national_number))
                        print(" \33[97m=[+]\33[0m\33[96m CÓDIGO DO PAÍS:", "+"+str(country_code))
                        print(" \33[97m=[+]\33[0m\33[96m NÚMERO DE MOÇAMBIQUE:", national_number)
                        print(" \33[97m=[+]\33[0m\33[96m OPERADORA:", None)
                        print(" \33[97m=[+]\33[0m\33[96m CONTINENTE:", continente[2:])
                        print(" \33[97m=[+]\33[0m\33[96m LOCALIZAÇÃO:","PAIS:", "MOÇAMBIQUE")
                        print(" \33[97m=[+]\33[0m\33[96m LOCALIZAÇÃO:","PROVINCIA:", countrys[:-3])
                        print (" \33[97m=================================")
                        arquivo = open(file_name, 'a')
                        os.system('chmod 777 *')
                        arquivo.writelines("ATIVO: {}\n".format(__number_complete))
                    else:
                        num_offline = num_offline + 1

            #BRSIL
            if (country.lower() == "brasil") or (country.lower() == "brazil"):
                #print (" BRSIL")
                for __numberPhone__ in range(46531276,999999999):
                    __designer_viws2__()
                    #time.sleep(1)
                    __number_complete = str(__code_br__)+str(__numberPhone__)
                    phone_number = phonenumbers.parse(__number_complete)
                    #print (len(__number_complete), __number_complete)
                    num_ctive = 0
                    num_offline = 0
                    
                    if (phonenumbers.is_valid_number(phone_number) == True):
                        num_ctive = num_ctive + 1
                        country_code = phone_number.country_code
                        national_number = phone_number.national_number
                        time_zone = timezone.time_zones_for_number(phone_number)
                        location = geocoder.description_for_number(phone_number, "en")
                        service_provider = carrier.name_for_number(phone_number, "en")
                        all_localize = str(time_zone)
                        continente, countrys = all_localize.split('/',2)
                        print ("\n \33[97m=================================")
                        print(" \33[97m=[+]\33[0m\33[96m NÚMERO:", "+"+str(country_code)+str(national_number))
                        print(" \33[97m=[+]\33[0m\33[96m CÓDIGO DO PAÍS:", "+"+str(country_code))
                        print(" \33[97m=[+]\33[0m\33[96m NÚMERO DE BRASIL:", national_number)
                        print(" \33[97m=[+]\33[0m\33[96m OPERADORA:", None)
                        print(" \33[97m=[+]\33[0m\33[96m CONTINENTE:", continente[2:])
                        print(" \33[97m=[+]\33[0m\33[96m LOCALIZAÇÃO:","PAIS:", "BRASIL")
                        print(" \33[97m=[+]\33[0m\33[96m LOCALIZAÇÃO:","PROVINCIA:", countrys[:-3])
                        print (" \33[97m=================================")
                        arquivo = open(file_name, 'a')
                        os.system('chmod 777 *')
                        arquivo.writelines("ATIVO: {}\n".format(__number_complete))
                    else:
                        num_offline = num_offline + 1

            else:
                os.system("clear")
                __designer_viws2__()
                print ("\33[3m"+"\33[1m"+" [+] DEGITE UMA PAÍS VALIDO. /EXE: ANGOLA,PORTUGAL,BRASIL,MOÇAMBIQUE.")
                exit()
#if __name__ == "__main__":
#    __code__execute__ = __main_execute__()
#    __code__execute__.__execute__()
#DONE