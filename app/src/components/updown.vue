<template>
  <div class="show">
    <!-- 头部搜索 -->
    <div class="search">
      <el-row>
        <el-col :span="10">
          <div class="grid-content bg-purple">
            <el-input v-model="input" placeholder="输入你想搜索的管理员用户名" clearable></el-input>
            <el-button plain @click="findlog">搜索</el-button>
          </div>
        </el-col>
        <el-col :span="10">
          <div class="grid-content bg-purple">
            <el-input v-model="rnewpath" placeholder="输入你用来恢复数据库的文件名" clearable></el-input>
             <el-button type="primary" @click="renew">数据恢复</el-button>
          </div>
        </el-col>
        <el-col :span="4">
           <div class="grid-content bg-purple-light">
            <el-button type="primary" @click="backup">数据备份</el-button>
          </div>
         </el-col> 
      </el-row>
    </div>
    <!-- 表格 -->
    <el-table :data="log_show" style="width: 100%" border stripe>
      <el-table-column align="center" type="index" label="#" width="50px"></el-table-column>
      <el-table-column align="center" prop="uname" label="管理员名称" width="100px"></el-table-column>
      <el-table-column align="center" prop="url" label="请求地址"width="150px"></el-table-column>
        <el-table-column align="center" prop="time" label="时间" width="150px">
            <template v-slot="scope">{{ getLocalTime(scope.row.time) }}</template>
        </el-table-column>
        <el-table-column align="center" prop="src" label="参数"></el-table-column>
    </el-table>
  </div>
</template>
<script>
export default {
  name: "log",
  data() {
    return {
      input: "",
      log_show: [],
      rnewpath:""
      }
  },
  created() {
    this.findlog()
  },
  methods: {
    findlog() {
      this.axios
        .get("/api/findlog", {
          params: {
            mname: this.input
          }
        })
        .then(response => {
          this.log_show = response.data;
        console.log(this.log_show)
        })
        .catch(error => {
          console.log(error);
        });
    },
     getLocalTime(nS) {     
   return new Date(parseInt(nS) ).toLocaleString().replace(/:\d{1,2}$/,' ');     
    },
    backup(){
      this.axios.post("/api/backup").then(res => {
          // console.log(res)
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "备份失败"
            });
          }
          return this.$message.success({
              duration: 800,
              message: "备份成功，备份文件位于D盘bilibili目录文件夹"
            });
    })},
    renew(){
      this.axios
      .get("/api/renew", {
          params: {
            mname: this.rnewpath
          }
        })
       .then(res => {
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "恢复失败"
            });
          }
          this.$message.success({
            duration: 800,
            message: "恢复成功"
          });
        });
    }
  }
}
</script>


<style lang="less" scoped>
.show {
  .search {
    margin-top: 15px;
    .el-input {
      width: 300px;
      margin: 0 30px;
    }
    .el-button {
      width: 100px;
    }
  }
  .el-table {
    margin-top: 40px;
  }
}
</style>
