import speech_recognition as sr

r=sr.Recognizer()

t=0
f = open("output.txt", "a")

with sr.Microphone() as source:
	print('Speak English :')
	
	while t==0:
		audio =r.listen(source)
		try:
			text =r.recognize_google(audio)
			print('you said :{}'.format(text), file=open("output.txt", "a"))
			print('you said :{}'.format(text))
			t=1

		except:
			print('Not understable')
			print('Try again')
			t==0

f.close()


from googlesearch import *
import webbrowser
#to search
query = text
#iexplorer_path = r'<Your browser path file> %s'
safari_path = r'/Applications/Safari.app %s'
for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
	webbrowser.open("https://google.com/search?q=%s" % query)