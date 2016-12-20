def r():
    with open('docker_image_tag', 'r') as test:
        string = test.readlines()[0]
        if string.find(',') == -1:
            text = int(string[-3:-2]) + 1
            return str(text)
        else:
            text = int(string.split(',')[-1][-3])+1
            return str(text)

        
def w():
    with open('docker_next_tag', 'w') as test:
        test.write("[command]\ncommand=docker build -t 172.16.0.100:5000/flask_app_v"+r()+" .")
        test.write("\n[tag]\ntag=172.16.0.100:5000/flask_app_v"+r())

w()
