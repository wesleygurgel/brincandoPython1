import os
import subprocess

command = 'C:/Riot Games/Riot Client/RiotClientServices.exe'

os.system('"%s"' % command)

subprocess.call(command, ' --launch-product=league_of_legends --launch-patchline=live')