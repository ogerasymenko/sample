import webbrowser
import time

while True:
    time.sleep(60*20)
    webbrowser.open_new("https://www.youtube.com/watch?v=IQfwgzoiq4c")
    print(time.ctime(), 'Time to get a break')
