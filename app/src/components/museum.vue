<template>
  <div class="show">
    <!-- 头部搜索 -->
    <div class="search">
      <el-row>
        <el-col :span="20">
          <div class="grid-content bg-purple">
            <el-input v-model="input" placeholder="输入你想搜索的博物馆名称" clearable></el-input>
            <el-button plain @click="findmuseum">搜索</el-button>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-button type="primary" @click="adddialogVisible = true">
              添加博物馆
              </el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    <!-- 表格 -->
    <el-table :data="museum_show" style="width: 100%" border stripe>
      <el-table-column align="center" type="index" label="#" width="80px"></el-table-column>
      <el-table-column align="center" prop="mname" label="博物馆名称"width="150px"></el-table-column>
      <el-table-column align="center" prop="mtime" label="开放时间" width="100"></el-table-column>
      <el-table-column align="center" prop="maddr" label="博物馆地址"width="100"></el-table-column>
    <!-- <el-table-column align="center" prop="mimg" label="博物馆图片"></el-table-column> -->
    <el-table-column align="center" prop="mactivity" label="文教活动"width="100"></el-table-column>
     <el-table-column align="center" prop="mresearch" label="学术研究"width="100"></el-table-column>
      <el-table-column align="center" prop="mvedio" label="视频"width="100"></el-table-column>
        <el-table-column align="center"  label="博物馆介绍" prop="mintro">
        </el-table-column>
      <el-table-column align="center" label="操作" width="130">
        <template v-slot="scope">
          <!-- 修改 -->
          <el-tooltip class="item" effect="dark" content="修改" placement="top" :enterable="false">
            <el-button type="primary" icon="el-icon-edit" circle @click="show(scope.row.mname)"></el-button>
          </el-tooltip>
          <!-- 删除 -->
          <el-tooltip class="item" effect="dark" content="删除" placement="top" :enterable="false">
            <el-button
              type="danger"
              icon="el-icon-delete-solid"
              circle
              @click="remove(scope.row.mname)"
            ></el-button>
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加用户弹出层 -->
    <el-dialog title="添加博物馆" :visible.sync="adddialogVisible" width="50%">
      <el-form
        :model="addfrom"
        :rules="addrules"
        ref="addFormref"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item label="博物馆名称" prop="mname">
           <el-col :span="12">
          <el-input v-model="addfrom.mname"></el-input>
           </el-col>
        </el-form-item>

        <el-form-item label="博物馆介绍" prop="mintro" >
          <el-input  type="textarea" :rows="3" v-model="addfrom.mintro"></el-input>
        </el-form-item>

        <el-form-item label="开放时间" prop="mtime">
            <el-input   v-model="addfrom.mtime"></el-input>
        </el-form-item>

        <el-form-item label="博物馆地址" prop="maddr">
          <el-input v-model="addfrom.maddr"></el-input>
        </el-form-item> 
        <!-- <el-form-item label="博物馆图片" prop="mimg">
          <el-input v-model="addfrom.mimg"></el-input>
        </el-form-item>  -->
        <el-form-item label="文教活动" prop="mactivity">
          <el-input v-model="addfrom.mactivity"></el-input>
        </el-form-item> 
        <el-form-item label="学术研究" prop="mresearch">
          <el-input v-model="addfrom.mresearch"></el-input>
        </el-form-item> 
        <el-form-item label="视频" prop="mvedio">
          <el-input v-model="addfrom.mvedio"></el-input>
        </el-form-item> 
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="resetForm">清 空</el-button>
        <el-button type="primary" @click="upForm">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改员工信息弹出层 -->
    <el-dialog title="修改博物馆信息" :visible.sync="updateDialogVisible" width="50%">
      <el-form
        :model="updatefrom"
        :rules="updaterules"
        ref="updateFormref"
        label-width="100px"
        class="demo-ruleForm"
      >
      <el-form-item label="博物馆名称" prop="mname" >
        <el-col :span="12">
          <el-input v-model="updatefrom.mname" disabled></el-input>
        </el-col>
        </el-form-item>

        <el-form-item label="博物馆介绍" prop="mintro">
          <el-input type="textarea" :rows="3"v-model="updatefrom.mintro"></el-input>
        </el-form-item>

        <el-form-item label="开放时间" prop="mtime">
            <el-input v-model="updatefrom.mtime"></el-input>
        </el-form-item>

        <el-form-item label="博物馆地址" prop="maddr">
          <el-input v-model="updatefrom.maddr"></el-input>
        </el-form-item> 
        <!-- <el-form-item label="博物馆图片" prop="mimg">
          <el-input v-model="updatefrom.mimg"></el-input>
        </el-form-item>  -->
        <el-form-item label="文教活动" prop="mactivity">
          <el-input v-model="updatefrom.mactivity"></el-input>
        </el-form-item> 
        <el-form-item label="学术研究" prop="mresearch">
          <el-input v-model="updatefrom.mresearch"></el-input>
        </el-form-item> 
        <el-form-item label="视频地址" prop="mvedio">
          <el-input v-model="updatefrom.mvedio"></el-input>
        </el-form-item> 
      </el-form>

      <span slot="footer" class="dialog-footer">
        <el-button @click="resetForm2">清 空</el-button>
        <el-button type="primary" @click="setForm">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
export default {
  name: "museum",
  data() {
    return {
      input: "",
      username:"",
      museum_show: [],
      adddialogVisible: false,
      addfrom: {
        mname: '',
        mintro: '',
        mtime: '',
        maddr: '',
        mactivity:'',
        mresearch:'',
        mvedio:''
      },
      addrules: {
        mintro: [{ required: true, message: "请输入博物馆介绍", trigger: "blur" },
        { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        mtime: [{ required: true, message: "请输入开放时间", trigger: "blur" },
        { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        maddr: [{ required: true, message: "请输入博物馆地址", trigger: "blur" },
        { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        mactivity: [{ required: true, message: "请输入文教活动", trigger: "blur" },
        { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        mresearch: [{ required: true, message: "请输入学术研究", trigger: "blur" },
        { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        mvedio: [{ required: true, message: "请输入视频地址", trigger: "blur" },
        { min: 1, max: 100, message: "长度在 1 到 100 个字符", trigger: "blur" }]
      },
      updateDialogVisible: false,
      updatefrom: {
        mname: '',
        mintro: '',
        mtime: '',
        maddr: '',
        mactivity:'',
        mresearch:'',
        mvedio:''
      },
      updaterules:{
        mname: [
          { required: true, message: "请输入博物馆名称", trigger: "blur" },
          { min: 1, max: 15, message: "长度在 1 到 15 个字符", trigger: "blur" }
        ],
        mintro: [{ required: true, message: "请输入博物馆介绍", trigger: "blur" },
        { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        mtime: [{ required: true, message: "请输入开放时间", trigger: "blur" },
        { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        maddr: [{ required: true, message: "请输入博物馆地址", trigger: "blur" },
        { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        mactivity: [{ required: true, message: "请输入文教活动", trigger: "blur" },
        { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        mresearch: [{ required: true, message: "请输入学术研究", trigger: "blur" },
        { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        mvedio: [{ required: true, message: "请输入视频地址", trigger: "blur" },
        { min: 1, max: 100, message: "长度在 1 到 100 个字符", trigger: "blur" }]
      }
  }
  },
  created() {
    this.username=window.sessionStorage.getItem('uname')
    this.findmuseum()
  },
  methods: {
    upForm() {
      this.$refs.addFormref.validate(valid => {
        if (valid) {
          this.axios.post("/api/addmuseum", this.addfrom,
          {
          params: {
            username: this.username
          }}).then(res => {
            if (res.data.code !== 200) {
              return this.$message.error({
                duration: 800,
                message: "添加失败"
              });
            }
            this.$message.success({
              duration: 800,
              message: "添加成功"
            });
            this.adddialogVisible = false;
            this.findmuseum();
            this.resetForm();
          });
        } else {
          console.log("表单数据有错误");
          return false;
        }
      });
    },
    resetForm() {
      this.$refs.addFormref.resetFields();
    },
    findmuseum() {
      this.axios
        .get("/api/findmuseum", {
          params: {
            mname: this.input
          }
        })
        .then(response => {
          this.museum_show = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    async remove(mname) {
      const confirmRes = await this.$confirm(
        "是否确定永久删除该博物馆信息?",
        "提示",
        {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning"
        }
      ).catch(err => err);
      // 确认删除返回的是 confirm 字符串
      // 取消删除返回的是 cancel 字符串
      if (confirmRes !== "confirm") {
        return this.$message.error({
          duration: 800,
          message: "已取消删除"
        });
      }

      this.axios
        .get("/api/removemuseum", {
          params: {
          mname:mname,
          username:this.username
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
          this.findmuseum();
        });
    },
    show(mname) {
      this.axios
        .get("/api/museum_mname", {
          params: {
        mname:mname,
          username:this.username
          }
        })
        .then(response => {
          this.updatefrom = response.data[0];
        })
        .catch(error => {
          console.log(error);
        });
      this.updateDialogVisible = true;
    },
    resetForm2() {
      this.$refs.updateFormref.resetFields();
    },
    setForm() {
      this.$refs.updateFormref.validate(valid => {
        if (!valid) return;
        
        this.axios.post("/api/updatemuseum", this.updatefrom,
        {
          params: {
            username: this.username
          }}).then(res => {
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "修改失败"
            });
          }
          this.updateDialogVisible = false;
          this.findmuseum();
          this.$message.success({
            duration: 800,
            message: "修改成功"
          });
        });
      });
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
     margin: 0 30px;
    }
  }
  .el-table {
    margin-top: 40px;
  }

}
.el-button--primary {
    color: #FFF;
    background-color: #409EFF;
    border-color: #409EFF;
    font-size: 12px;
}
</style>
