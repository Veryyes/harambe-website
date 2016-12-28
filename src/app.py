import web
from web import form
import time
import urllib

def bad_words():
	bad_words = []
	f = open('profanity.txt', 'r')
	for line in f:
		bad_words.append(line.strip())
	return bad_words

def load_sounds():
	sounds = []
		

render = web.template.render('templates/', base='layout')

urls = (
	'/','index', '/about.html', 'about', '/memories.html', 'memories', '/all-memories.html', 'all_memories'
)

mysql_login = []
login_credentials = open('mysql_login','r')
for line in login_credentials:
	mysql_login.append(line.strip())

#login_credentials => username\npassword\ndatabase_name
db = web.database(dbn='mysql', user=mysql_login[0], pw=mysql_login[1], db=mysql_login[2])


app = web.application(urls, globals())

entry = form.Form(
	form.Textarea("message")
)

bad_words = bad_words()

class index:
	def GET(self):
		return render.home()

class about:
	def GET(self):
		return render.about()

class all_memories:
	def GET(self):
		table = db.select('memories')
		remember = entry()
		len_table = len(table)
		posts = []
		i = 0
		for p in table:
			posts.append(p.message)
		posts.reverse()
		return render.memories(remember, posts)

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
		comment = web.data()[8:] #removes prefix
		comment = comment.replace('+',' ')
		comment = urllib.unquote(comment).decode('ascii')#parses message
		bad_message = False
		for bad in bad_words:
			if bad in comment.lower():
				bad_message=True
				break
				
		date = time.strftime('%Y-%m-%d %X')
		ip = web.ctx.ip

		if bad_message:
			print "[{}] {}: Bad Word in Message: {} => skipping".format(date,ip,comment)
		elif len(comment) < 2:
			print "[{}] {}: Empty Message => skipping".format(date,ip)
		else:
			#Calculate the struct_time representing 1 minute ago
			minute_ago = time.strftime('%Y-%m-%d %X',time.localtime(time.time()-60))
			#Querying the data by the user starting from 1 minute ago
			curr_user = db.select('memories', where='name=\''+str(ip)+'\' and time >= \''+minute_ago+'\'')

			if len(curr_user) <= 4: #if there are more than 4 posts in the last minute it is spam
				n = db.insert('memories', time=date, name=ip, message=comment)
				print "[{}] {}: Message: {}".format(date, ip, comment)
			else:
				print "[{}] {}: User Spamming".format(date, ip)

		raise web.seeother('/memories.html')

	#4 posts per min

if __name__=="__main__":
	app.run()
