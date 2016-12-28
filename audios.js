fs = require('fs')
fs.readdir('./static/sounds/', (err,files)=>{
	var i = 0
	files.forEach(file=>{
		console.log("<audio id=\"sound"+i+"\" src=\"/static/sounds/"+file+"\"></audio>")
		i++
	})
})
