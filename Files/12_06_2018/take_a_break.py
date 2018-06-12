import time
import webbrowser

print("this program started at: "+time.ctime())
for i in range(3):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=op4B9sNGi0k")