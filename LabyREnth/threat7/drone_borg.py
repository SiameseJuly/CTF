#!/usr/bin/env python
import requests, time, sys, json, ast, logging, base64
logging.getLogger("scapy.runtime").setLevel(logging.CRITICAL)
from scapy.all import *

def AABBBC(AABBCF, AABBCE, AABBBF):
    AABBCC = len(AABBCF)/float(len(AABBCE))
    if str(AABBCC).split(".")[1] == "0":
        AABBCD = int(str((AABBCC)).split(".")[0]) * 8
    else:
        while str(AABBCC).split(".")[1] != "0":
            AABBCF += "@"
            AABBCC = len(AABBCF)/float(len(AABBCE))
        AABBCD = int(str((AABBCC)).split(".")[0]) * 8
    AABBB0 = []
    AABBCF = list(AABBCF)
    AABBCE = list(AABBCE)
    while AABBCF != []:
        p_AABBCF = AABBCF[0:8]
        p_AABBCE = AABBCE[0:8]
        AABBB1 = []
        for i in xrange(0,8):
            if type(p_AABBCE[i]) == int: # [+] *** ALERT ALERT *** [+]
                AABBB2 = (ord(chr(p_AABBCE[i])) ^ ord(p_AABBCF[0])) # [+] HUMANS HAVE BROKEN THROUGH [+]
            else: # [+] MODULATE SHIELDS [+]
                AABBB2 = (ord(p_AABBCE[i]) ^ ord(p_AABBCF[0])) # [+] *** ALERT ALERT *** [+]
            AABBB0.append(AABBB2)
            AABBB1.append(AABBB2)
            AABBCF.pop(0)
            p_AABBCF.pop(0)
            AABBCE = AABBB1
        AABBCE.reverse()
    AABBB0.reverse()
    AABBB4 = []
    for i in AABBB0:
        AABBB3 = hex(i)
        if len(AABBB3) != 4:
            AABBB4.append("0" + hex(i)[2:])
        else:
            AABBB4.append(hex(i)[2:])
    AABBB4 = "".join(AABBB4).upper()
    return AABBB4

def AABBB7(AABBBE):
    return AABBBE[::-1]

def AABBCB(AABBBE):
    print "\t[-] *** ERROR CONNECTING ***"
    print "\n[+] SHUTTING DOWN DRONE [+]\n"
    time.sleep(2)
    sys.exit()

def main():
    AABBBD = """
            ___________
           /-/_"/-/_/-/|
          /"-/-_"/-_//||
         /__________/|/|
         |"|_'='-]:+|/||
         |-+-|.|_'-"||//
         |[".[:!+-'=|//
         |='!+|-:]|-|/
          ----------
"""
    print AABBBD
    print "[+] BORG DRONE BOOTUP STARTING [+]"
    time.sleep(2)
    try:
        AABBBA = json.load(open("borgstruct.cfg"))
        print "\t[-] CONFIGURATION", str(AABBBA['key'][1]) + ".0 LOADED"
    except:
        AABBBA = {"warp": ["d0rw$54p", "lss", "p//:ptth", "nimda//:ptf"],
                  "coil": ["r/moc.nibets", "exe.1\:c", "tropmmoc"],
                  "dilithium": ["praw", "-redrocirt", "FfPE6AFw/w"],
                  "scalar": [874, 34, 666],
                  "array": [69, 80, 443, 25, 22, 2600, 666, 8443, 27500],
                  "LoadLibraryA": ["IsDebuggerPresent", "IsDebuggerDetected", "NtQueryInformationProcess", "GetTickCount"],
                  "LoadLibraryB": ["CheckRemoteDebuggerPresent", "UnhandledExceptionFilter", "CloseHandle", "QueryPerformanceCounter"],
                  "LoadLibraryC": ["NtGetContextThread", "NtSetContextThread", "NtClose"],
                  "adb": ["0xCD", "0x03"],
                  "targets": ["squirtle", "humans", "ferengi", "rick astley"],
                  "key": ["borgdata", 1, 2, 3, 4, 5, 6, 7, 8, "startrek", "cloaking"],
                  "commands": ["ping", "shutdown", "nslookup"],
                  "lore": ["grab", "the", "flag"]}
        json.dump(AABBBA, open("borgstruct.cfg", "w"))
        print "\t[-] CONFIGURATION VERSION", str(AABBBA['key'][1]) + ".0 WRITTEN"
    if AABBBA['key'][1] == 1:
        print "\n[+] FETCHING STARTUP VALUE FROM MATRIX"
        time.sleep(2)
        try:
            AABBB5 = AABBB7((AABBBA['dilithium'][2]) + "a" + (AABBBA['coil'][0]) + "a" + (AABBBA['warp'][2]))
            AABBB6 = requests.get(AABBB5, verify=False)
        except:
            AABBCB(AABBBA['LoadLibraryA'][0])
        AABBCE = AABBB6.content.split("\n")[1]
        print "\t[-] DATA =", AABBCE
    if AABBBA['key'][1] == 2: # [+] *** ALERT ALERT *** [+]
        print "\n[+] SEND FLAG REQUEST WITH ENCRYPTED DATA AND CODE [+]" # [+] HUMANS HAVE BROKE NEXT DEFENSE [+]
        AABBCE = AABBB7((AABBBA['dilithium'][2]) + "o" + (AABBBA['coil'][0]) + "o" + (AABBBA['warp'][2])) # [+] INITIATE LOW ORBIT ION CANNON [+]
        print "\t[-] DATA =", AABBCE # [+] *** ALERT ALERT *** [+]
    AABBCF = AABBBA['key'][0]
    print "\t[-] INITIALIZATION KEY =", AABBCF
    if len(AABBCF) != 8:
        sys.exit()
    print "\n[+] STARTING BORG ENCRYPTION ROUTINE [+]"
    time.sleep(2)
    AABBBB = AABBBC(AABBCE, AABBCF, AABBBA['array'][3])
    print "\t[-] RESULT = " + AABBBB
    print "\n[+] STARTING DRONE COMMUNICATION PROTOCOLS [+]"
    time.sleep(2)
    scalar_array = AABBBA['scalar'][0]
    FEEDDEAD = base64.b64decode('cGFuYm9yZ2Ryb25lLmNvbQ==')
    try:
        AABBB8 = IP(dst=FEEDDEAD)/TCP(dport=AABBBA['array'][5],window=scalar_array,flags="S")/AABBBB
        AABBB9 = sr1(AABBB8, verbose=True)
    except:
        AABBCB(AABBBA['LoadLibraryB'][1])
    if AABBB9[TCP].window == 666:
        print "\t*** ERROR RECEIVED ***"
        print "\t[-] RETURNED = ", AABBB9[Raw]
        print "\n[+] SHUTTING DOWN DRONE [+]\n"
        time.sleep(2)
        sys.exit()
    elif AABBB9[TCP].window == 34:
        print "\t[-] UPDATE SUCCESSFUL"
        AABBBA = ast.literal_eval(str(AABBB9[Raw]).strip("\n"))
        print "\t[-] CONFIGURATION VERSION", str(AABBBA['key'][1]) + ".0 WRITTEN"
        json.dump(AABBBA, open("borgstruct.cfg", "w"))
        print "\t[-] PROCESSING COMMANDS"
        print "\t[-] EXECUTING COMMAND =", AABBBA['commands'][3], AABBBA['adb'][2], "/"
        time.sleep(10)
        print "\t*** ERROR WITH COMMAND ***"
        print "\t[-] NEW SERVER FUNCTION ADDED - FLAG REQUEST"
        print "\t[-] FLAG REQUEST REQUIRED FOR CURRENT ENCRYPTED DATA"
        print "\n[+] SHUTTING DOWN DRONE [+]\n"
        time.sleep(2)
        sys.exit()
    else:
        print "\t[-] RETURNED = ", AABBB9[Raw], "\n"

if __name__ == "__main__":
    main()
 