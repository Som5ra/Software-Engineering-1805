<template>

<div>
    <img class="image" src="../assets/background.jpg" alt="">
    <div id="Box">
        <div id="bigBox">
			<h1>LOGIN</h1>
			<div class="inputBox">
                <!--登录表单区域-->
                <el-form ref="loginFormRef" :model="loginForm">
                <!--用户名-->
				<div class="inputText">
					<input v-model="loginForm.uname"  placeholder="Username">
				</div> 
                <!--密码-->
				<div class="inputText">
					<input v-model="loginForm.upwd" type="password" placeholder="Password">
				</div>
                
                <!--动态登录按钮-->
                <div id="wrap" @click="login">
			        <a href="#" class="btn-slide">
			            <span class="circle"><i class="fa fa-download" @click="login"></i></span>
			            <span class="title">登录</span> 
			            <span class="title-hover">点击登录</span>
			        </a>
	    	    </div>
                </el-form>
			</div>
		</div>
    </div>
</div>

</template>

<script>
export default {
    data()
    {
        return{
            //登录表单数据绑定对象
            loginForm:{
                uname:"",
                upwd:""
            },
        }
    },
    methods:{
        login(){
        this.$refs.loginFormRef.validate(valid => {
        if (valid) {
          this.axios.post("/api/login", this.loginForm).then(res => {
           // console.log(res.data)
            if (res.data.code !== 200) {
              return this.$message.error({
                duration: 800,
                message: "登录失败"
              });
            }
            this.$message.success({
              duration: 800,
              message: "登录成功"
            });
            console.log(res)
            window.sessionStorage.setItem('token',res.data.token)
            window.sessionStorage.setItem('uname',this.loginForm.uname)
            this.$router.push('/list')
          });
        } else {
          console.log("登录失败");
          return false;
        }
      });
        }
    }
}
</script>

<style  lang="less" scoped>
.image
{
    width:100%;
    height:100%;
    position:absolute;
}
#bigBox
{
	margin:0 auto;
	margin-top: 200px;
	padding: 20px 50px;
	background-color: #00000090;
	width: 400px;
	height: 300px;
	border-radius: 10px;
	text-align: center;
    left:50%;
    transform: translate(-50%);
    position:absolute; 
}

#bigBox h1
{
	color: white;
	font-family:Verdana, Geneva, Tahoma, sans-serif;
	font-size: 40px;

}

#bigBox .inputBox
{
	margin-top: 30px;

}

#bigBox .inputBox .inputText
{
	margin-top: 20px;

}

#bigBox .inputBox .inputText input
{
	border: 0;
	padding: 10px 10px;
	border-bottom: 1px solid white;
	background-color: #00000000;
	color: white;

}

.inputText
{
    padding:0;
    margin-left:30%;
    margin-right:30%;

}

#wrap {
    margin: 20px auto;
    text-align: center;
}
 
#wrap br {
    display: none;
}
 
.btn-slide{
    position: relative;
    display: inline-block;
    height: 30px;
    width: 150px;
    line-height: 30px;
    padding: 0;
    border-radius: 30px;
    background: #fdfdfd;
    border: 2px solid #0099cc;
    margin: 15px;
    transition: .5s;
}

.btn-slide:hover {
    background-color: #0099cc;
}
 

.btn-slide:hover span.circle{
    right: 100%;
    margin-right: -40px;
    background-color: #fdfdfd;
    color: #0099cc;
}

.btn-slide:hover span.title{
    right: 35px;
    opacity: 0;
}
 
.btn-slide:hover span.title-hover {
    opacity: 1;
    right: 30px;
}
 
.btn-slide span.circle{
    display: block;
    background-color: #0099cc;
    color: #fff;
    position: absolute;
    margin: 1px;
    height: 28px;
    width: 28px;
    top: 0;
    right: 10px;
    transition: .5s;
    border-radius: 50%;
}
.btn-slide span.title, .btn-slide span.title-hover{
    position: absolute;
    right: 70px;
    text-align: center;
    margin: 0 auto;
    font-size: 16px;
    font-weight: bolder;
    color: #30abd5;
    transition: .5s;
}
.btn-slide span.title-hover{
    right: 0;
    opacity: 0;
}
 
.btn-slide span.title-hover{
    color: #fff;
}
</style>
