var fs = require('fs');
// console.log(fs);

fs.readFile('./user.txt','utf8',(err,data)=>{
    if(err) throw err;
    console.log(data);
});

// var http = require('http');
// var app = http.createServer(function (req,res) {
//     console.log(req.url);
//     res.setHeader('Content-Type','text/html');
//     res.setHeader('X-Foo','bar');
//     res.writeHead(200,{'Content-Type':'text/plain;charset=utf-8'});
//     res.end('哈哈哈哈哈');
// });
//
// app.listen(3000);