var express = require('express')
var app = express()

app.get('/', (req, res) => res.end('hello world'))

app.listen(3000)
