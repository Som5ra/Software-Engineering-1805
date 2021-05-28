<template>
  <el-container class="home-container">
    <!-- 导航栏 -->
    <el-header>
      <div>
        <img class="logostyle"src="../assets/logo.jpg" alt="" />
        <span>博物馆后台管理系统</span>
      </div>
      <el-button type="info" @click="logout">退出</el-button>
    </el-header>
    <el-container>
      <!-- 侧边栏 -->
      <el-aside :width="isCollapse ?'64px':'200px'">
        <div class="toggle-button" @click="toggleCollapse">|||</div>
        <el-menu
          background-color="#333744"
          text-color="#fff"
          active-text-color="#409FFF"
          :unique-opened="true"
          :collapse="isCollapse"
          :collapse-transition="false"
          :router="true"
          :default-active="activePath"
        >
        <!-- :default-active="$route.path" -->
          <el-submenu
            :index="item.id + ''"
            v-for="item in section"
            :key="item.id"
          >
            <!-- 1模板区 -->
            <template slot="title">
              <i :class="id[item.id]"></i>
              <span>{{ item.name }}</span>
            </template>
            <el-menu-item
              :index="'/'+subItem.path"
              v-for="subItem in item.children"
              :key="subItem.id"
              @click="saveNavState('/'+subItem.path)"
            >
              <!-- 2模板区 -->
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>{{ subItem.name }}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <!-- 右部主体 -->
      <el-main>    
        <!-- 路由站位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import login from "./Login.vue";

export default {
  name: "home",
  data() {
    return {
      //左侧菜单数据
      id: {
        1: "iconfont icon-user",
        2: "iconfont icon-tijikongjian",
        3: "iconfont icon-shangpin",
        4: "iconfont icon-danju",
      },
      
      section: [],
      post: [],
      //是否折叠
      isCollapse:false,
      //被激活的链接地址
      activePath:''
    };
  },
  created() {
    this.getsection();
    this.activePath=window.sessionStorage.getItem('activePath')
  },
  methods: {
    //退出
    logout() {
      //清除token
      window.sessionStorage.clear();
      this.$router.push("/login");
    },
    // 请求左侧栏内容数据
    getsection() {
      this.axios
        .get("/api/getsection")
        .then(response => {
          this.section = response.data;
         //  console.log(this.section)
        })
        .catch(error => {
          console.log(error);
        });
    },
     /*左侧栏贴入展开*/
    toggleCollapse(){
      this.isCollapse=!this.isCollapse
    },
    /*保存链接的激活状态*/
    saveNavState(activePath){
        window.sessionStorage.setItem('activePath',activePath)
        this.activePath=activePath
    }
  }
};
</script>


<style less="lang" scoped>
.home-container {
  height: 100%;
}
.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #fff;
  font-size: 20px;
}
.el-header > div {
  display: flex;
  align-items: center;
}
.el-header > div > span {
  margin-left: 15px;
}
.el-aside {
  background-color: #373d41;
}
.el-aside .el-menu {
  border-right: none;
}
.el-main {
  background-color: #eaedf1;
}
.iconfont {
  margin-right: 10px;
}
.toggle-button {
  background-color: #4a5064;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em;
  cursor:pointer;
}
.logostyle{
  width: 50px;
  height: 50px;
}
</style>