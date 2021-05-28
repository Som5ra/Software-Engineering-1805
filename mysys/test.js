var exec = require('child_process').exec

//var cmd = 'mysqldump -h localhost -u root -p142857 bilibili > d:/bilibili/bilibili--' + Date.now()+ '.sql' 

var cmd = 'mysql -h localhost -u root -p142857 vuenode < ' + 'd:/2020.sql'
exec(cmd, function(err, stdout, stderr){

})