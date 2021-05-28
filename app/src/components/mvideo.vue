<template>
  <div class="show">
    <!-- 头部搜索 -->
    <div class="search">
      <el-row>
        <el-col :span="20">
          <div class="grid-content bg-purple">
            <el-select clearable v-model="option" placeholder="审核状态">
              <el-option v-for="item in examine" :key="item.id" :label="item.name" :value="item.name"></el-option>
            </el-select>
            <el-input v-model="input" placeholder="输入你想搜索的博物馆名称或视频标题" clearable></el-input>
            <el-button plain @click="findmvideo">搜索</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    <!-- 表格 -->
    <el-table :data="mvideo_show" style="width: 100%" border stripe>
      <el-table-column align="center" type="index" label="#" width="50px"></el-table-column>
      <el-table-column align="center" prop="mname" label="博物馆名称" width="150px"></el-table-column>
      <el-table-column align="center" prop="mvname" label="视频标题" width="150px"></el-table-column>
        <el-table-column align="center" prop="mvurl" label="视频链接" width="150px"></el-table-column>
        <el-table-column align="center" prop="mvtime" label="上传时间"width="250px">
           <template v-slot="scope">{{ renderTime(scope.row.mvtime) }}</template>
        </el-table-column>
       <el-table-column align="center" prop="mvstatus" label="审核状态" width="180px"></el-table-column>
      <el-table-column align="center" label="操作" >
        <template v-slot="scope">
            <!-- 审核通过 -->
            <el-tooltip class="item" effect="dark" content="审核通过" placement="top" :enterable="false">
            <el-button
              type="success"
              icon="el-icon-check"
              circle
              @click="agree(scope.row.mvid)"
            ></el-button>
          </el-tooltip>
          <!-- 审核不通过 -->
          <el-tooltip class="item" effect="dark" content="审核不通过" placement="top" :enterable="false">
            <el-button
              type="primary"
              icon="el-icon-close"
              circle
              @click="disagree(scope.row.mvid)"
            ></el-button>
          </el-tooltip>
          <!-- 删除 -->
          <el-tooltip class="item" effect="dark" content="删除" placement="top" :enterable="false">
            <el-button
              type="danger"
              icon="el-icon-delete-solid"
              circle
              @click="remove(scope.row.mvid)"
            ></el-button>
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
export default {
  name: "mvideo",
  data() {
    return {
       username:"",
      examine: [],
      option: "",
      input: "",
      mvideo_show: [],
      }
  },
  created() {
    this.username=window.sessionStorage.getItem('uname')
    this.getexamine();
    this.findmvideo()
  },
  methods: {
    getexamine() {
      this.axios
        .get("/api/getexamine")
        .then(response => {
          this.examine = response.data;
          console.log(this.examine)
        })
        .catch(error => {
          console.log(error);
        });
    },
    findmvideo() {
      this.axios
        .get("/api/findmvideo", {
          params: {
            poid: this.option,
            mname: this.input
          }
        })
        .then(response => {
          this.mvideo_show = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    async remove(mvid) {
      const confirmRes = await this.$confirm(
        "是否确定永久删除该视频信息?",
        "提示",
        {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning"
        }
      ).catch(err => err);
      if (confirmRes !== "confirm") {
        return this.$message.error({
          duration: 800,
          message: "已取消删除"
        });
      }

      this.axios
        .get("/api/removemvideo", {
          params: {
          mvid:mvid,
          username: this.username 
          }
        })
        .then(res => {
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "删除失败"
            });
          }
          this.$message.success({
            duration: 800,
            message: "删除成功"
          });
          this.findmvideo();
        });
    },
    async agree(mvid) {
      const confirmRes = await this.$confirm(
        "是否确定通过该视频信息?",
        "提示",
        {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "success"
        }
      ).catch(err => err);
      if (confirmRes !== "confirm") {
        return this.$message.error({
          duration: 800,
          message: "已取消审核"
        });
      }

      this.axios
        .get("/api/agreemvideo", {
          params: {
          mvid:mvid,
           username: this.username
          }
        })
        .then(res => {
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "操作失败"
            });
          }
          this.$message.success({
            duration: 800,
            message: "操作成功"
          });
          this.findmvideo();
        });
    },
     async disagree(mvid) {
      const confirmRes = await this.$confirm(
        "是否确定不同意该视频信息?",
        "提示",
        {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning"
        }
      ).catch(err => err);
      if (confirmRes !== "confirm") {
        return this.$message.error({
          duration: 800,
          message: "已取消审核"
        });
      }

      this.axios
        .get("/api/disagreemvideo", {
          params: {
          mvid:mvid,
           username: this.username
          }
        })
        .then(res => {
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "操作失败"
            });
          }
          this.$message.success({
            duration: 800,
            message: "操作成功"
          });
          this.findmvideo();
        });
    },
    renderTime(date) {
  var dateee = new Date(date).toJSON();
  return new Date(+new Date(dateee) + 8 * 3600 * 1000).toISOString().replace(/T/g, ' ').replace(/\.[\d]{3}Z/, '') 
}
  }
};
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
