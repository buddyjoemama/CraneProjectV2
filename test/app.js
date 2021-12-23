var http = require('http');

for(var i = 0; i <= 10001; i++) {
    const req = http.request(options, res => {
        console.log(`statusCode: ${res.statusCode}`)

        res.on('data', d => {
            process.stdout.write(d)
        })
    })

    req.on('error', error => {
        console.error(error)
    })

    req.end();

    var options = {
        hostname: 'localhost',
        port: 80,
        path: `/py/control/hook/up/0/down/${i%2}`,
        method: 'GET'
      }
}