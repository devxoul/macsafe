# -*- coding: utf-8 -*-


from time import sleep
import subprocess


#: A location of siren sound file.
SOUND_LOCATION = "/Volumes/XOUL/Music/윤종신 - 너에게 간다 (With 김범수).mp3"

# Previous Volume Level
volume_level = '0'

def check():
    """Check whether adapter is connected or not.
    """
    cmd = "pmset -g ac"
    r = subprocess.Popen(cmd, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    return 'No adapter attached' not in r.stdout.read()

def volume_max(): 
    global volume_level
    cmd = "osascript -e 'output volume of (get volume settings)'; osascript -e 'set volume output volume 100'"
    r = subprocess.Popen(cmd, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    volume_level = r.stdout.read().split('\n')[0]

def volume_recover():
    cmd = "osascript -e 'set volume output volume %s'" % volume_level
    subprocess.Popen(cmd, shell=True)

def siren():
    """Ring the siren. RRRR!!!
    """
    volume_max()
    cmd = 'afplay "%s"' % SOUND_LOCATION
    subprocess.Popen(cmd, shell=True)
    print "Ring the siren. RRRRRRR!!! RRRRRR!!!"


def calmdown():
    """Calm down. Stop siren.
    """
    cmd = "ps aux | grep afplay | awk '{print $2}' | xargs kill -9"
    subprocess.Popen(cmd, shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    volume_recover()

def start():
    """Start macsafe.
    """
    print "MacSafe has been started. ლ(╹◡╹ლ)"

    # a flag for check being disconnected or reconnedted.
    has_been_disconnected = False

    while(True):
        status = check()

        # disconnect
        if not status:
            print "AWWWWW!!!! Somebody took my adapter off!!!! ლ(ಠ益ಠლ)"
            if not has_been_disconnected:
                siren()
            has_been_disconnected = True

        # re-connect
        elif has_been_disconnected:
            print "( ͡° ͜ʖ ͡°) I got you babe. Hahaha."
            if has_been_disconnected:
                calmdown()
            has_been_disconnected = False

        # sleep for a second. >->o zZZ
        sleep(1)


if __name__ == '__main__':
    start()
