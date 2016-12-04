import web
from web import form
import time
import urllib

render = web.template.render('templates/', base='layout')

urls = (
	'/','index', '/about.html', 'about', '/memories.html', 'memories'
)

db = web.database(dbn='mysql', user='harambe', pw='love', db='harambe')

app = web.application(urls, globals())

entry = form.Form(
	form.Textarea("message"),
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
		len_table = len(table)
		posts = []
		i = 0
		for p in table:
			posts.append(p.message)
		posts.reverse()
		another_list = []
		for p in posts:
			if(i>7):
				break;
			another_list.append(p)
			i+=1
		return render.memories(remember, another_list)


	def POST(self):
		
		remember = entry()
		comment = web.data()[8:]
		print comment
		comment = comment.replace('+',' ')
		print comment
		comment = urllib.unquote(comment).decode('ascii')
		print comment
		table = db.select('memories')
		date = time.strftime('%Y-%m-%d %X')
		n = db.insert('memories', time=date,name='n/a',message=comment)
		raise web.seeother('/memories.html')
		#return render.memories(remember, table)

if __name__=="__main__":
	app.run()
