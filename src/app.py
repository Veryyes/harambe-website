import web
from web import form
import time
import urllib

render = web.template.render('templates/', base='layout')

urls = (
	'/','index', '/about.html', 'about', '/memories.html', 'memories', '/tragedy.html', 'tragedy'
)

db = web.database(dbn='mysql', user='harambe', pw='love', db='harambe')

app = web.application(urls, globals())

entry = form.Form(
<<<<<<< HEAD
	form.Textarea("remember")
=======
	form.Textarea("message"),
>>>>>>> master
)

class index:
	def GET(self):
		return render.home()

class about:
	def GET(self):
		return render.about()

class memories:
	def GET(self):
		table = db.select('memories')
		remember = entry()
<<<<<<< HEAD
		#print remember.render()
		return render.memories(remember, table)
=======
		comment = web.data()[8:]
		
		return render.memories(remember)
>>>>>>> a176d45e7148400ce0a6a6a4500b053e8754cc2c

	def POST(self):
		
		remember = entry()
		comment = web.data()[8:]
		print comment
		comment = urllib.unquote(comment).decode('ascii')
		print comment
		table = db.select('memories')
		date = time.strftime('%Y-%m-%d %X')
		n = db.insert('memories', time=date,name='n/a',message=comment)
		raise web.seeother('/memories.html')
		#return render.memories(remember, table)

class tragedy:
	def GET(self):
		return render.tragedy()

if __name__=="__main__":
	app.run()
