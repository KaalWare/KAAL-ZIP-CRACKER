'''imports'''
import zipfile
__banner__ = """
       +=======================================+
       |..........Zip  Cracker v 0.0.1.........|
       +---------------------------------------+
       |#Author: Devoloper.embuy <@KAAL>        |
       |#Contact: https://t.me/IAMKAAL            |
       |#Date: Thu jun 4 1:15:49 2020             |
       |#This Tool For Crack Zip File Password    |
       |#Changing the description of this tool      |
       |Won't made you the coder ^_^ !!!           |
       |#Respect Coderz ^_^                    |
       |#I take no responsibilities for the    |
       |  use of this program !                |
       +=======================================+
       |..........Zip Cracker v 1.0.0..........|
       +---------------------------------------+
"""

count = 1

with open('passlist.txt','rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile('crack.zip','r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print(__banner__,'''*****PASSWORD CRACKED*****\n******************************\n[+] Password Found! ~ %s\n ~%s\n ~%s\n******************************''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] [-] Trying... - %s' % (number,password.decode('utf8')),'[-] failed')
            count += 1
            pass
