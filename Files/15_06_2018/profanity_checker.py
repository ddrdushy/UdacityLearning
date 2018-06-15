import urllib.request
import urllib.parse

def readFile():
    quotes=open("./movie_quotes.txt")
    content_of_file=quotes.read()
    #print(content_of_file)
    quotes.close()
    checkProfanity(content_of_file.replace("\n",""))

def checkProfanity(text_to_check):
    
    conn = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+urllib.parse.quote(text_to_check))
    output = conn.read()
    conn.close()

    if 'true' in output.decode('utf-8'):
        print("Profanity Alert!!")
    elif 'false' in output.decode('utf-8'):
        print('no curse words')
    else:
        print('could not scan the docment properly')


readFile()