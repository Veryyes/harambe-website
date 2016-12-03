import web
from web import form

render = web.template.render('templates/', base='layout')
urls = (
	'/','index', '/about.html', 'about', '/memories.html', 'memories', '/tragedy.html', 'tragedy'
)

app = web.application(urls, globals())

entry = form.Form(
	form.Textbox("remember"),
	form.Button("submit")
)

class index:
	def GET(self):
		return render.home()

class about:
	def GET(self):
		return render.about()

class memories:
	def GET(self):
		remember = entry()
		#print remember.render()
		return render.memories(remember)

class tragedy:
	def GET(self):
		return render.tragedy()

if __name__=="__main__":
	app.run()
