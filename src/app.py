import web

render = web.template.render('templates/', base='layout')
urls = (
	'/','index', '/about', 'about'
)

app = web.application(urls, globals())

class index:
	def GET(self):
		
		return render.home()
class about:
	def GET(self):
		return "about"

if __name__=="__main__":
	app.run()
