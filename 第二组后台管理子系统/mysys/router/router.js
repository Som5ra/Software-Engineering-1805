const express = require('express')
var exec = require('child_process').exec
const expressJwt = require('express-jwt')
const con = require('../modul/db.js')
const jwt= require('jsonwebtoken');
const router = express.Router()
const secret = 'mouchun'; //定义密钥
let db= con.handleDisconnection()

// 处理数据的函数
// data 数据
// root 顶级数据
let getChildren = function (data, root) {
  var children = [];
  for (var i = 0; i < data.length; i++) {
    if (root == data[i].super) {
      data[i].children = getChildren(data, data[i].id);
      children.push(data[i]);
    }
  }
  return children;
}

// 获取侧边栏
router.get('/getsection', (req, res) => {
  let sql = `SELECT * FROM section`
  db.query({
    sql: sql
  }, (err, results) => {
    if (err) {
      console.log(err)
    } else {
      res.send(getChildren(results, 0))
    }
  })
})

// 获取用户信息
router.get('/getstaff', (req, res) => {
  //let id = req.query.id
  let sql = `SELECT * FROM staff`
  db.query({
    sql: sql
  }, (err, results, fields) => {
    res.header('Content-type: application/json')
    res.send(results)
  })

})


// 获取用户类型
router.get('/getpost', (req, res) => {
  let sql = `SELECT * FROM post`
  db.query({
    sql: sql
  }, (err, results, fields) => {
    res.send(results)
  })

})

//// 添加用户数据
router.post('/addstaff', (req, res) => {
  console.log(req.query)
  //插入日志表
  let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{用户名称:${req.body.uname}};{用户密码:${req.body.upwd}};{用户联系方式:${req.body.uphone}};{用户id:${req.body.poid}}');`
  db.query(sql1, (err, result) => {
    if(err){
      console.log(err)
    }
    else{
      console.log(result)
    }
  })
  //插入用户表
  let sql = `INSERT INTO staff (uname,upwd,uphone,poid) values ('${req.body.uname}','${req.body.upwd}','${req.body.uphone}','${req.body.poid}')`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })

  
})

// 搜索用户信息
router.get('/findstaff', (req, res) => {
  let poid = req.query.poid //岗位id
  let name = req.query.uname //员工姓名
  if (poid) {
    sql = `SELECT * FROM staff WHERE staff.poid = '${poid}' and staff.uname LIKE '%${name}%';`
  } else {
    sql = `SELECT * FROM staff WHERE staff.uname LIKE '%${name}%';`
  }
  db.query({
    sql: sql
  }, (err, results, fields) => {
    console.log(results)
    res.send(results)
  })

})

// 删除用户
router.get('/removestaff', (req, res) => {
  console.log('123',req.query.username)
  let id = req.query.id
  let sql0 = `select * from staff where id = ${id}`
  db.query(sql0, (err, result) => {
    if (err) {
      console.log(err)
    } else {
     
    let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{用户名称:${result[0].uname}};{用户密码:${result[0].upwd}};{用户联系方式:${result[0].uphone}};{用户id:${result[0].poid}}');`
    db.query(sql1, (err1, result1) => {
      if(err1){
        console.log(err1)
     }
      else{
        console.log(result1)
     }
      })
      }
  })

  let sql = `DELETE FROM staff WHERE id = '${id}'`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })
})

// 根据用户id搜索用户
router.get('/staff_id', (req, res) => {
  let id = req.query.id
  let sql = `SELECT * FROM staff WHERE staff.id = ${id} `
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.send(result)
    }
  })
})

// 更新用户信息
router.post('/update', (req, res) => {
    let id = req.body.id,
        exi = req.body,
        newSta = [exi.uname, exi.upwd,exi.uphone,exi.poid]
  
    let sql0 = `select * from staff where id = ${id}`
    db.query(sql0, (err, result) => {
      if (err) 
      {
        console.log(err)
      }
      else
      {
        let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{原用户名:${result[0].uname}};{原用户密码:${result[0].upwd}};{原用户联系方式:${result[0].uphone}};{原用户id:${result[0].poid}};{新用户名:${exi.uname}};{新用户密码:${exi.upwd}};{新用户联系方式:${exi.uphone}};{新用户id:${exi.poid}}');`
        db.query(sql1, (err1, result1) => {
          if(err1)
          {
            console.log(err1)
          }
          else
          {
            console.log(result1)
          }
        })
  
      }
    })
      
    let sql = `UPDATE staff SET uname = ?, upwd = ?, uphone = ?, poid = ? WHERE id = '${req.body.id}'`
    db.query(sql, newSta, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })
})



//// 添加数据
router.post('/addmuseum', (req, res) => {

  let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${req.body.mname}};{博物馆介绍:${req.body.mintro}};{开放时间:${req.body.mtime}};{博物馆地址:${req.body.maddr}};{文教活动:${req.body.mactivity}};{科教活动:${req.body.mresearch}};{博物馆视频:${req.body.mvedio}}');`
  db.query(sql1, (err, result) => {
    if(err){
      console.log(err)
    }
    else{
      console.log(result)
    }
  })

  let sql = `INSERT INTO museum (mname,mintro,mtime,maddr,mactivity,mresearch,mvedio) values ('${req.body.mname}','${req.body.mintro}','${req.body.mtime}','${req.body.maddr}','${req.body.mactivity}','${req.body.mresearch}','${req.body.mvedio}')`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })


})

// 搜索博物馆信息
router.get('/findmuseum', (req, res) => {
  let name = req.query.mname //博物馆名称
  sql = `SELECT * FROM museum WHERE museum.mname LIKE '%${name}%';`

  db.query({
    sql: sql
  }, (err, results, fields) => {
    res.send(results)
  })

})

// 删除博物馆
router.get('/removemuseum', (req, res) => {

  let name = req.query.mname
 let sql0 = `select * from museum where mname = '${name}'`
  db.query(sql0, (err, result) => {
    if (err) {
      console.log(err)
    } else {
    let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${result[0].mname}};{博物馆介绍:${result[0].mintro}};{开放时间:${result[0].mtime}};{博物馆地址:${result[0].maddr}};{文教活动:${result[0].mactivity}};{科教活动:${result[0].mresearch}};{博物馆视频:${result[0].mvedio}}');`
    db.query(sql1, (err1, result1) => {
      if(err1){
        console.log(err1)
     }
      else{
        console.log(result1)
     }
      })
      }
  })
  let sql = `DELETE FROM museum WHERE mname = '${name}'`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })
})

// mname获取博物馆
router.get('/museum_mname', (req, res) => {
  let name = req.query.mname
  let sql = `SELECT * FROM museum WHERE museum.mname = '${name}' `
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.send(result)
    }
  })
})

// 更新museum信息
router.post('/updatemuseum', (req, res) => {

  let name = req.body.mname,
  exi = req.body,
  newSta = [exi.mname, exi.mtime, exi.maddr, exi.mactivity, exi.mresearch, exi.mvedio]
let sql0 = `select * from museum where mname = '${name}'`
db.query(sql0, (err, result) => {
if (err) 
{
  console.log(err)
}
else
{
  let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{原博物馆名称:${result[0].mname}};{原博物馆介绍:${result[0].mintro}};{原开放时间:${result[0].mtime}};{原博物馆地址:${result[0].maddr}};{原文教活动:${result[0].mactivity}};{原科教活动:${result[0].mresearch}};{原博物馆视频:${result[0].mvedio}};{新博物馆名称:${exi.mname}};{新博物馆介绍:${exi.mintro}};{新开放时间:${exi.mtime}};{新博物馆地址:${exi.maddr}};{新文教活动:${exi.mactivity}};{新科教活动:${exi.mresearch}};{新博物馆视频:${exi.mvedio}}');`
  db.query(sql1, (err1, result1) => {
    if(err1)
    {
      console.log(err1)
    }
    else
    {
      console.log(result1)
    }
  })

}
})

let sql = `UPDATE museum SET mintro = ?, mtime = ?, maddr = ?, mactivity = ?, mresearch = ?, mvedio = ? WHERE mname = '${req.body.mname}'`
db.query(sql, newSta, (err, result) => {
if (err) {
  console.log(err)
} else {
  res.json({
    code: 200
  })
}
})


})


//// 添加展览数据
router.post('/addexhibition', (req, res) => {

  let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${req.body.mname}};{展览名称:${req.body.exname}};{展览时间:${req.body.extime}};{展览地址:${req.body.exaddr}};{展览介绍:${req.body.exintro}};{展览视频:${req.body.exvedio}}');`
  db.query(sql1, (err, result) => {
    if(err){
      console.log(err)
    }
    else{
      console.log(result)
    }
  })

  let sql = `INSERT INTO exhibition (mname,exname,extime,exaddr,exintro,exvedio) values ('${req.body.mname}','${req.body.exname}','${req.body.extime}','${req.body.exaddr}','${req.body.exintro}','${req.body.exvedio}')`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })
})

// 根据mname搜索展览信息
router.get('/findexhibition', (req, res) => {
  let name = req.query.mname //博物馆或展览名称
  

  sql = `SELECT * FROM exhibition WHERE exhibition.mname LIKE '%${name}%' or exhibition.exname like '%${name}%';`
  db.query({
    sql: sql
  }, (err, results, fields) => {
    console.log(results)
    res.send(results)
  })

})

// 删除展览信息
router.get('/removeexhibition', (req, res) => {
  let id = req.query.id

  let sql0 = `select * from exhibition where id = ${id}`
  db.query(sql0, (err, result) => {
    if (err) {
      console.log(err)
    } else {
     
    let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${result[0].mname}};{展览名称:${result[0].exname}};{展览时间:${result[0].extime}};{展览地址:${result[0].exaddr}};{展览介绍:${result[0].exintro}};{展览视频:${result[0].exvedio}}');`
    db.query(sql1, (err1, result1) => {
      if(err1){
        console.log(err1)
     }
      else{
        console.log(result1)
     }
      })
      }
  })

  let sql = `DELETE FROM exhibition WHERE id = '${id}'`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })
})

// 根据id获取展览信息
router.get('/exhibition_id', (req, res) => {
  let id = req.query.id
  let sql = `SELECT * FROM exhibition WHERE exhibition.id = '${id}' `
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.send(result)
    }
  })
})


// 更新展览信息
router.post('/updateexhibition', (req, res) => {
  let name = req.body.mname,
      id = req.body.id,
      exi = req.body,
      newSta = [exi.mname, exi.exname, exi.extime, exi.exaddr, exi.exintro, exi.exvedio]

  let sql0 = `select * from exhibition where id = ${id}`
  db.query(sql0, (err, result) => {
    if (err) 
    {
      console.log(err)
    }
    else
    {
      let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{原博物馆名称:${result[0].mname}};{原展览名称:${result[0].exname}};{原展览时间:${result[0].extime}};{原展览地址:${result[0].exaddr}};{原展览介绍:${result[0].exintro}};{原展览视频:${result[0].exvedio}};{新博物馆名称:${exi.mname}};{新展览名称:${exi.exname}};{新展览时间:${exi.extime}};{新展览地址:${exi.exaddr}};{新展览介绍:${exi.exintro}};{新展览视频:${exi.exvedio}}');`
      db.query(sql1, (err1, result1) => {
        if(err1)
        {
          console.log(err1)
        }
        else
        {
          console.log(result1)
        }
      })

    }
  })
    
  let sql = `UPDATE exhibition SET mname = ?, exname = ?, extime = ?, exaddr = ?, exintro = ?, exvedio = ? WHERE id = '${req.body.id}'`
  db.query(sql, newSta, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })
})


//// 添加藏品数据
router.post('/addcollection', (req, res) => {
 let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${req.body.mname}};{藏品名称:${req.body.cname}};{藏品介绍:${req.body.cintro}};{藏品视频:${req.body.cvideo}}');`
  db.query(sql1, (err, result) => {
    if(err){
      console.log(err)
    }
    else{
      console.log(result)
    }
  })

  let sql = `INSERT INTO collection (mname,cname,cintro,cvideo) values ('${req.body.mname}','${req.body.cname}','${req.body.cintro}','${req.body.cvideo}')`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })



})

// 搜索藏品信息
router.get('/findcollection', (req, res) => {
  let name = req.query.mname //博物馆名称
  let sql = `SELECT * FROM collection WHERE collection.mname LIKE '%${name}%' or collection.cname like '%${name}%';`
  db.query({
    sql: sql
  }, (err, results, fields) => {
    console.log(results)
    res.send(results)
  })

})

// 删除collection
router.get('/removecollection', (req, res) => {
  
  let name = req.query.cname
  
 let sql0 = `select * from collection where cname = '${name}'`
  db.query(sql0, (err, result) => {
    if (err) {
      console.log(err)
    } else {
     
    let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${result[0].mname}};{藏品名称:${result[0].cname}};{藏品介绍:${result[0].cintro}};{藏品视频:${result[0].cvideo}}');`
    db.query(sql1, (err1, result1) => {
      if(err1){
        console.log(err1)
     }
      else{
        console.log(result1)
     }
      })
      }
  })

  let sql = `DELETE FROM collection WHERE cname = '${name}'`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })




})

// 根据id获取collection信息
router.get('/collection_cname', (req, res) => {
  let name = req.query.cname
  let sql = `SELECT * FROM collection WHERE cname = '${name}' `
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.send(result)
    }
  })
})

// 更新 collection 信息
router.post('/updatecollection', (req, res) => {

  let name = req.body.cname,
  id = req.body.id,
  exi = req.body,
  newSta = [exi.mname, exi.cintro, exi.cvideo]

let sql0 = `select * from collection where cname = '${name}'`
db.query(sql0, (err, result) => {
if (err) 
{
  console.log(err)
}
else
{
  let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{原博物馆名称:${result[0].mname}};{原藏品名称:${result[0].cname}};{原藏品介绍:${result[0].cintro}};{原藏品视频:${result[0].cvideo}};{新博物馆名称:${exi.mname}};{新藏品名称:${exi.cname}};{新藏品介绍:${exi.cintro}};{新藏品视频:${exi.cvideo}}');`
  db.query(sql1, (err1, result1) => {
    if(err1)
    {
      console.log(err1)
    }
    else
    {
      console.log(result1)
    }
  })

}
})

let sql = `UPDATE collection SET mname = ?, cintro = ?, cvideo = ? WHERE cname = '${req.body.cname}'`
db.query(sql, newSta, (err, result) => {
if (err) {
  console.log(err)
} else {
  res.json({
    code: 200
  })
}
})




})

//添加新闻
router.post('/addnews', (req, res) => {

  let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${req.body.mname}};{新闻标题:${req.body.nname}};{上传时间:${req.body.ntime}};{新闻简介:${req.body.nintro}};{新闻来源:${req.body.nsource}};{次级新闻网站:${req.body.nurl}};{新闻状态:${req.body.nstatus}}');`
  db.query(sql1, (err, result) => {
    if(err){
      console.log(err)
    }
    else{
      console.log(result)
    }
  })

  let sql = `INSERT INTO nnews (mname,nname,ntime,nintro,nsource,nurl,nstatus) values ('${req.body.mname}', '${req.body.nname}', '${req.body.ntime}', '${req.body.nintro}', '${req.body.nsource}', '${req.body.nurl}', '${req.body.nstatus}')`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })

  })
  
  // 搜索新闻信息
  router.get('/findnews', (req, res) => {
    let name = req.query.nname //新闻标题
    let sql = `SELECT * FROM nnews WHERE nnews.nname LIKE '%${name}%' or nnews.mname like '%${name}%';`

    db.query({
      sql: sql
    }, (err, results, fields) => {
      console.log(results)
      res.send(results)
    })
  
  })
  
  // 删除新闻
  router.get('/removenews', (req, res) => {
  let name = req.query.nname
  
 let sql0 = `select * from nnews where nname = '${name}'`
  db.query(sql0, (err, result) => {
    if (err) {
      console.log(err)
    } else {
     
    let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${result[0].mname}};{新闻标题:${result[0].nname}};{上传时间:${result[0].ntime}};{新闻简介:${result[0].nintro}};{新闻来源:${result[0].nsource}};{次级新闻网站:${result[0].nurl}};{新闻状态:${result[0].nstatus}}');`
    db.query(sql1, (err1, result1) => {
      if(err1){
        console.log(err1)
     }
      else{
        console.log(result1)
     }
      })
      }
  })

  let sql = `DELETE FROM nnews WHERE nname = '${name}'`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })
})

  // 获取新闻
  router.get('/news_nname', (req, res) => {
    let name = req.query.nname
    let sql = `SELECT * FROM nnews WHERE nnews.nname='${name}'`
    db.query(sql, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.send(result)
      }
    })
  })
  
  // 更新新闻信息
  router.post('/updatenews', (req, res) => {
    
  let name = req.body.nname,
  id = req.body.id,
  exi = req.body,
  nus = req.body,
  newSta = [nus.ntime, nus.nintro, nus.nsource, nus.nurl, nus.nstatus]

  let sql0 = `select * from nnews where nname = '${name}'`
  db.query(sql0, (err, result) => {
  if (err) 
  {
    console.log(err)
  }
  else
  {
    let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{原上传时间:${result[0].ntime}};{原新闻介绍:${result[0].nintro}};{原新闻来源:${result[0].nsource}};{原新闻链接:${result[0].nurl}};{原新闻状态：${result[0].nstatus}};{新上传时间:${exi.ntime}};{新新闻介绍:${exi.nintro}};{新新闻来源:${exi.nsource}};{新新闻链接:${exi.url}};{新新闻状态:${exi.nstatus}}');`
    db.query(sql1, (err1, result1) => {
    if(err1)
    {
      console.log(err1)
    }
    else
    {
      console.log(result1)
    }
    })
  }
})

let sql = `UPDATE nnews SET ntime = ?, nintro = ?,nsource = ?, nurl = ?, nstatus = ? WHERE nname='${req.body.nname}'`
db.query(sql, newSta, (err, result) => {
if (err) {
  console.log(err)
} else {
  res.json({
    code: 200
  })
}
})
})



  // 添加评价数据
router.post('/addscore', (req, res) => {

    let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${req.body.mname}};{用户名:${req.body.uname}};{评价分数:${req.body.evalscore}};{评价内容:${req.body.evalintro}};{展览评价分数:${req.body.evalscore_ex}};{服务评价分数:${req.body.evalscore_serv}};{评价分数:${req.body.evalscore_environ}}');`
    db.query(sql1, (err, result) => {
      if(err){
        console.log(err)
      }
      else{
        console.log(result)
      }
    })
  
    let sql = `INSERT INTO score (mname,uname,evalscore,evalintro,evalscore_ex,evalscore_serv,evalscore_environ) values ('${req.body.mname}','${req.body.uname}','${req.body.evalscore}','${req.body.evalintro}','${req.body.evalscore_ex}','${req.body.evalscore_serv}','${req.body.evalscore_environ}')`
    db.query(sql, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })

})

// 搜索评价信息
router.get('/findscore', (req, res) => {
  let name = req.query.uname, //根据用户名
  sql = `SELECT * FROM score WHERE score.uname LIKE '%${name}%' or score.mname LIKE '%${name}%';`

  db.query({
    sql: sql
  }, (err, results, fields) => {
    //console.log('d${req.query.username}',results.length)
    for(var i = 0; i < results.length; i++)
    {
      if(results[i].scorestatus == 1)
      {
        results[i].scorestatus = true
      }
      else
      {
        results[i].scorestatus = false
      }
    }
    console.log(results)
    res.send(results)
  })
})


// 删除用户评价
router.get('/removescore', (req, res) => {

  let name = req.query.uname
  let  sql0 = `select * from score where uname = '${name}'`
    db.query(sql0, (err, result) => {
      if (err) {
        console.log(err)
      } else {
       
        let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${result[0].mname}};{用户名:${result[0].uname}};{评价分数:${result[0].evalscore}};{评价内容:${result[0].evalintro}};{展览评价分数:${result[0].evalscore_ex}};{服务评价分数:${result[0].evalscore_serv}};{评价分数:${result[0].evalscore_environ}}');`
      db.query(sql1, (err1, result1) => {
        if(err1){
          console.log(err1)
       }
        else{
          console.log(result1)
       }
        })
        }
    })
  
    let sql = `DELETE FROM score WHERE uname = '${name}'`
    db.query(sql, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })

})


// mname获取评价
router.get('/score_mname', (req, res) => {
  let name = req.query.mname
  let sql = `SELECT * FROM score WHERE score.mname = '${name}' `
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.send(result)
    }
  })
})
// uname获取评价
  router.get('/score_uname', (req, res) => {
    let name = req.query.uname
    let sql = `SELECT * FROM score WHERE score.uname = '${name}' `
    db.query(sql, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.send(result)
      }
    })
  })
// 更新score信息
router.post('/updatescore', (req, res) => {

 let name = req.body.uname,
      exi = req.body,
    newSta = [exi.evalscore, exi.evalintro, exi.evalscore_ex, exi.evalscore_serv, exi.evalscore_environ]
  
    let sql0 = `select * from score where uname = '${name}'`
    db.query(sql0, (err, result) => {
      if (err) 
      {
        console.log(err)
      }
      else
      {
        let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{原博物馆名称:${result[0].mname}};{原用户名:${result[0].uname}};{原评价分数:${result[0].evalscore}};{原评价内容:${result[0].evalintro}};{原展览评价分数:${result[0].evalscore_ex}};{原服务评价分数:${result[0].evalscore_serv}};{原评价分数:${result[0].evalscore_environ}};{新博物馆名称:${req.body.mname}};{新用户名:${req.body.uname}};{新评价分数:${req.body.evalscore}};{新评价内容:${req.body.evalintro}};{新展览评价分数:${req.body.evalscore_ex}};{新服务评价分数:${req.body.evalscore_serv}};{新评价分数:${req.body.evalscore_environ}}');`
        db.query(sql1, (err1, result1) => {
          if(err1)
          {
            console.log(err1)
          }
          else
          {
            console.log(result1)
          }
        })
  
      }
    })
      
    let sql = `UPDATE score SET evalscore = ?, evalintro = ?, evalscore_ex = ?, evalscore_serv = ?, evalscore_environ = ? WHERE uname = '${req.body.uname}'`
    db.query(sql, newSta, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })


})

  // 搜索博物馆视频信息
  router.get('/findmvideo', (req, res) => {
    
      let name = req.query.mname//根据用户名
      let id = req.query.poid
      if(name && id)
        {
          sql = `SELECT * FROM mvideo WHERE mvstatus = '${id}' and (mvideo.mvname LIKE '%${name}%' or mvideo.mname LIKE '%${name}%');`
        }
        else if(id)
        {
          sql = `SELECT * FROM mvideo WHERE mvstatus = '${id}';`
        }
        else
        {
          sql = `SELECT * FROM mvideo WHERE mvideo.mname LIKE '%${name}%' or mvideo.mvname LIKE '%${name}%'`
        }

    
      db.query({
        sql: sql
      }, (err, results, fields) => {
        console.log(results)
        res.send(results)
      })
    })
  
 // 删除博物馆视频
 router.get('/removemvideo', (req, res) => {

    let id = req.query.mvid
    let sql0 = `select * from mvideo where mvid = ${id}`
    db.query(sql0, (err, result) => {
      if (err) {
        console.log(err)
      } else {
       
      let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名字:${result[0].mname}};{视频标题:${result[0].mvname}};{上传时间:${result[0].mvtime}};{视频url:${result[0].mvurl}};{审核状态:${result[0].mvstatus}}');`
      db.query(sql1, (err1, result1) => {
        if(err1){
          console.log(err1)
       }
        else{
          console.log(result1)
       }
        })
        }
    })
  
    let sql = `DELETE FROM mvideo WHERE mvid = '${id}'`
    db.query(sql, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })
})




  // 搜索展览视频
  router.get('/findevideo', (req, res) => {
    
      let name = req.query.mname//根据用户名
      let id = req.query.poid
      if(name && id)
        {
          sql = `SELECT * FROM evideo WHERE evstatus = '${id}' and (evideo.evname LIKE '%${name}%' or evideo.mname LIKE '%${name}%');`
        }
        else if(id)
        {
          sql = `SELECT * FROM evideo WHERE evstatus = '${id}';`
        }
        else
        {
          sql = `SELECT * FROM evideo WHERE evideo.mname LIKE '%${name}%' or evideo.evname LIKE '%${name}%'`
        }
    
      db.query({
        sql: sql
      }, (err, results, fields) => {
        console.log(results)
        res.send(results)
      })
    })
  
 // 删除展览视频
 router.get('/removeevideo', (req, res) => {

  let id = req.query.evid
  let sql0 = `select * from evideo where evid = ${id}`
  db.query(sql0, (err, result) => {
    if (err) {
      console.log(err)
    } else {
     
    let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名字:${result[0].mname}};{视频标题:${result[0].evname}};{上传时间:${result[0].evtime}};{视频url:${result[0].evurl}};{审核状态:${result[0].evstatus}}');`
    db.query(sql1, (err1, result1) => {
      if(err1){
        console.log(err1)
     }
      else{
        console.log(result1)
     }
      })
      }
  })

  let sql = `DELETE FROM evideo WHERE evid = '${id}'`
  db.query(sql, (err, result) => {
    if (err) {
      console.log(err)
    } else {
      res.json({
        code: 200
      })
    }
  })

  
  })




    // 搜索藏品视频
    router.get('/findcvideo', (req, res) => {
    //console.log('203',req.query)
        let name = req.query.mname//根据用户名
        let id = req.query.poid
       // console.log('dsf',id)
        if(name && id)
        {
          sql = `SELECT * FROM cvideo WHERE cvstatus = '${id}' and (cvideo.cvname LIKE '%${name}%' or cvideo.mname LIKE '%${name}%');`
        }
        else if(id)
        {
          sql = `SELECT * FROM cvideo WHERE cvstatus = '${id}';`
        }
        else
        {
          sql = `SELECT * FROM cvideo WHERE cvideo.mname LIKE '%${name}%' or cvideo.cvname LIKE '%${name}%'`
        }
      
        db.query({
          sql: sql
        }, (err, results, fields) => {
          console.log(results)
          res.send(results)
        })
      })
    
   // 删除藏品视频
   router.get('/removecvideo', (req, res) => {

    let id = req.query.cvid
    let sql0 = `select * from cvideo where cvid = ${id}`
    db.query(sql0, (err, result) => {
      if (err) {
        console.log(err)
      } else {
       
      let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名字:${result[0].mname}};{视频标题:${result[0].cvname}};{上传时间:${result[0].cvtime}};{视频url:${result[0].cvurl}};{审核状态:${result[0].cvstatus}}');`
      db.query(sql1, (err1, result1) => {
        if(err1){
          console.log(err1)
       }
        else{
          console.log(result1)
       }
        })
        }
    })
  
    let sql = `DELETE FROM cvideo WHERE cvid = '${id}'`
    db.query(sql, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })

    })
  


// 更新用户评价功能状态
router.get('/updatescorestatus', (req, res) => {

    let status = req.query.scorestatus,
        name = req.query.uname,
        sql = '',
        sql1 = ''
      console.log(status)
    if(status=='true')
    {
      sql1 += `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{原权限:不可评论};{新权限:可评论}')`
    }
    else
    {
      sql1 += `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{原权限:可评论};{新权限:不可评论}')`
    }

    db.query(sql1, (err, result) => {
      if (err) {
        console.log(err)
      }
    })

    if(status=='true')
    {
      sql += `UPDATE score SET scorestatus = 1 WHERE uname = '${req.query.uname}'`
    }
    else{
      sql += `UPDATE score SET scorestatus = 0 WHERE uname = '${req.query.uname}'`
    }
    db.query(sql, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })
  })

// 登录接口
router.post('/login', (req, res) => {
    let name = req.body.uname,
        pwd = req.body.upwd
  
    let sql1 = `insert into log (uname,url,time,src) values ('${name}', '${(req.url).split('?')[0]}', '${Date.now()}', '登录')`
    db.query(sql1, (err1, result1) => {
      if(err1)
      {
        console.log(err1)
      }
      else
      {
        console.log(result1)
      }
    })
    
    let sql = `select * from staff where uname='${name}' and upwd='${pwd}' and poid=1`
    db.query(sql, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        if(result[0]){
          //console.log('result 非空')
          res.json({
                    code: 200,
                    token:jwt.sign(Object.assign({},  result[0]), secret, {
                      expiresIn:  60 * 60 * 2 // 过期时间
                  })
                 })
        }
        else{
          //console.log('result 空')
          res.json({
                    code: 404
                 })
        }
      }
    })
  })    


  
  // 通过藏品视频审核
  router.get('/agreecvideo', (req, res) => {

    let id = req.query.cvid,
        exi = req.query,
        newSta = [exi.mname, exi.cvname, exi.cvtime, exi.cvurl, exi.cvstatus]
  
    let sql0 = `select * from cvideo, collection where cvideo.cvid = ${id} and cvideo.mname = collection.mname`
    db.query(sql0, (err, result) => {
      if (err) 
      {
        console.log(err)
      }
      else
      {
        let sql2 = `select * from cvideo where cvid = ${id}`
        db.query(sql2, (err2, result2) => {
          if(err2)
          {
            console.log(err2)
          }
          else
          {
            let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${result[0].mname}};{原视频url:${result[0].cvideo}};{新视频url:${result2[0].cvurl}};{新视频审核状态:审核通过');`
        db.query(sql1, (err1, result1) => {
          if(err1)
          {
            console.log(err1)
          }
          else
          {
            console.log(result1)
          }
        })
          }
        })

  
      }
    })
      
    let sql =  `UPDATE cvideo, collection SET collection.cvideo = cvideo.cvurl, cvideo.cvstatus = '审核通过' where cvideo.cvid = '${req.query.cvid}' and cvideo.mname = collection.mname`
    db.query(sql, newSta, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })

    })
  
   // 不通过藏品视频审核
   router.get('/disagreecvideo', (req, res) => {

    let id = req.query.cvid,
        exi = req.query,
        newSta = [exi.mname, exi.cvname, exi.cvtime, exi.cvurl, exi.cvstatus]
  
    let sql0 = `select * from cvideo where cvid = ${id}`
    db.query(sql0, (err, result) => {
      if (err) 
      {
        console.log(err)
      }
      else
      {
        let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{新视频url:${result[0].cvurl}};{新视频审核状态:审核不通过');`
        db.query(sql1, (err1, result1) => {
          if(err1)
          {
            console.log(err1)
          }
          else
          {
            console.log(result1)
          }
        })
  
      }
    })
      
   let sql =  `UPDATE cvideo SET cvideo.cvstatus = '审核不通过' where cvideo.cvid = '${req.query.cvid}'`
    db.query(sql, newSta, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })
      


    
    })

  // 通过展览视频审核
router.get('/agreeevideo', (req, res) => {

     let id = req.query.evid,
        exi = req.query,
        newSta = [exi.mname, exi.evname, exi.evtime, exi.evurl, exi.evstatus]
  
    let sql0 = `select * from evideo,exhibition where evideo.evid = ${id} and evideo.mname = exhibition.mname`
    db.query(sql0, (err, result) => {
      if (err) 
      {
        console.log(err)
      }
      else
      {

        let sql2 = `select * from evideo where evideo.evid = ${id}`
        db.query(sql2, (err2, result2) => {
          if(err2)
          {
            console.log(err2)
          }
          else
          {
            let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${result[0].mname}};{原视频url:${result[0].exvedio}};{新视频url:${result2[0].evurl}};{新视频审核状态:审核通过}');`
        db.query(sql1, (err1, result1) => {
          if(err1)
          {
            console.log(err1)
          }
          else
          {
            console.log(result1)
          }
        })
          }
        })  
      }
    })
      
    let sql =  `UPDATE evideo, exhibition SET exhibition.exvedio = evideo.evurl, evideo.evstatus = '审核通过' where evideo.evid = '${req.query.evid}' and evideo.mname = exhibition.mname`
    db.query(sql, newSta, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })

  
  })

 // 不通过展览视频审核
 router.get('/disagreeevideo', (req, res) => {

     let id = req.query.evid,
        exi = req.query,
        newSta = [exi.mname, exi.evname, exi.evtime, exi.evurl, exi.evstatus]
  
    let sql0 = `select * from evideo where evid = ${id}`
    db.query(sql0, (err, result) => {
      if (err) 
      {
        console.log(err)
      }
      else
      {
        let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${result[0].mname}};{新视频url:${result[0].evurl}};{新视频审核状态:审核不通过}');`
        db.query(sql1, (err1, result1) => {
          if(err1)
          {
            console.log(err1)
          }
          else
          {
            console.log(result1)
          }
        })
  
      }
    })
      
    let sql =  `UPDATE evideo SET evideo.evstatus = '审核不通过' where evideo.evid = '${req.query.evid}'`
    db.query(sql, newSta, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })
  })
    // 通过博物馆视频审核
router.get('/agreemvideo', (req, res) => {

    let id = req.query.mvid,
        exi = req.query,
        newSta = [exi.mname, exi.mvname, exi.mvtime, exi.mvurl, exi.mvstatus]
  
    let sql0 = `select * from museum, mvideo where mvideo.mvid = ${id} and mvideo.mname = museum.mname`
    db.query(sql0, (err, result) => {
      if (err) 
      {
        console.log(err)
      }
      else
      {
        let sql2 = `select * from mvideo where mvideo.mvid = ${id}`
        db.query(sql2, (err2, result2) => {
          if(err2)
          {
            console.log(err2)
          }
          else
          {
            let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{博物馆名称:${result[0].mname}};{原视频url:${result[0].mvurl}};{新视频url:${result2[0].mvurl}};{新视频审核状态:${result2[0].mvstatus}}');`
            db.query(sql1, (err1, result1) => {
              if(err1)
              {
                console.log(err1)
              }
              else
              {
                console.log(result1)
              }
            })
          }
        })
       
  
      }
    })
      
    let sql =  `UPDATE mvideo, museum SET museum.mvedio = mvideo.mvurl, mvideo.mvstatus = '审核通过' where mvideo.mvid = '${req.query.mvid}' and mvideo.mname = museum.mname`
    db.query(sql, newSta, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })


  })

 // 不通过博物馆视频审核
 router.get('/disagreemvideo', (req, res) => {

  let id = req.query.mvid,
        exi = req.query,
        newSta = [exi.mname, exi.mvname, exi.mvtime, exi.mvurl, exi.mvstatus]
  
    let sql0 = `select * from mvideo where mvideo.mvid = ${id}`
    db.query(sql0, (err, result) => {
      if (err) 
      {
        console.log(err)
      }
      else
      {
        let sql1 = `insert into log (uname, url, time, src) values ('${req.query.username}','${(req.url).split('?')[0]}','${Date.now()}','{新视频标题:${result[0].mvname}};{新视频url:${result[0].mvurl}};{新视频审核状态:审核不通过}');`
        db.query(sql1, (err1, result1) => {
          if(err1)
          {
            console.log(err1)
          }
          else
          {
            console.log(result1)
          }
        })
  
      }
    })
      
    let sql =  `UPDATE mvideo SET mvideo.mvstatus = '审核不通过' where mvideo.mvid = '${req.query.mvid}'`
    db.query(sql, newSta, (err, result) => {
      if (err) {
        console.log(err)
      } else {
        res.json({
          code: 200
        })
      }
    })
  })

//搜索日志
  router.get('/findlog', (req, res) => {
    
      let name = req.query.mname//根据用户名
      sql = `SELECT * FROM log WHERE log.uname LIKE '%${name}%';`
    
      db.query({
        sql: sql
      }, (err, results, fields) => {
        //console.log(results)
        res.send(results)
      })
    })
//审核下拉菜单  
  router.get('/getexamine', (req, res) => {
      let sql = `SELECT * FROM examine`
      db.query({
        sql: sql
      }, (err, results, fields) => {
        res.send(results)
      })
    
    })

//备份
  router.post('/backup', (req, res) => {
    var cmd = 'mysqldump -h localhost -u root -p142857 bilibili > d:/bilibili/bilibili--' + Date.now()+ '.sql' 
    exec(cmd, function(err, stdout, stderr){
        if(err)
        {
          console.log('err',err)
          res.json({
            code: 404
          })
        }
        else{
          res.json({
            code: 200
          })
        }
      })
    })
//恢复
 router.get('/renew', (req, res) => {
    let filename = req.query.mname
    console.log('sdf',filename)
    var cmd = 'mysql -h localhost -u root -p142857 bilibili < d:/bilibili/' + filename
     exec(cmd, function(err, stdout, stderr){
          if(err)
          {
            console.log('err',err)
            res.json({
              code: 404
            })
          }
          else{
            res.json({
              code: 200
            })
          }
        })
      })  
    
module.exports = router
