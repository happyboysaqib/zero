import os, platform, time
print('\n\x1b[1;37m[•] Checking Update...');time.sleep(0.5)
os.system('git pull')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':                                                                          
            print("\x1b[1;92m[•] Congratulations ! Your Device Support this Tools")
            print('[•] This Tools is Paid Not Free')
            import AKING
            AKING.Main()
        elif bit == '32bit':
            print("\n\x1b[1;92m[•] Congratulations ! Your Device Support this Tools")
            print('[•] This Tools is Paid Not Free')
            import AKING32
            SAQIB UR REHMAN 32.Main()
        else:
            exit('\033[1;31m[×] Error')
Run()
