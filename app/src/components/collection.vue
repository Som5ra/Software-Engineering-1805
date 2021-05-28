<template>
  <div class="show">
    <!-- 头部搜索 -->
    <div class="search">
      <el-row>
        <el-col :span="20">
          <div class="grid-content bg-purple">
            <el-input v-model="input" placeholder="输入你想搜索的博物馆或藏品名称" clearable></el-input>
            <el-button plain @click="findcollection">搜索</el-button>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-button type="primary" @click="adddialogVisible = true">添加藏品</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    <!-- 表格 -->
    <el-table :data="collection_show" style="width: 100%" border stripe>
      <el-table-column align="center" type="index" label="#" width="40"></el-table-column>
      <el-table-column align="center" prop="mname" label="博物馆名称"width="150"></el-table-column>
      <el-table-column align="center" prop="cname" label="藏品名称"width="150"></el-table-column>
      <el-table-column align="center" prop="cintro" label="藏品介绍"></el-table-column>
      <el-table-column align="center" prop="cvideo" label="视频"width="150"></el-table-column>
      <el-table-column align="center" label="操作" width="150">
        <template v-slot="scope">
          <!-- 修改 -->
          <el-tooltip class="item" effect="dark" content="修改" placement="top" :enterable="false">
            <el-button type="primary" icon="el-icon-edit" circle @click="show(scope.row.cname)"></el-button>
          </el-tooltip>
          <!-- 删除 -->
          <el-tooltip class="item" effect="dark" content="删除" placement="top" :enterable="false">
            <el-button
              type="danger"
              icon="el-icon-delete-solid"
              circle
              @click="remove(scope.row.cname)"
            ></el-button>
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加用户弹出层 -->
    <el-dialog title="添加藏品" :visible.sync="adddialogVisible" width="50%">
      <el-form
        :model="addfrom"
        :rules="addrules"
        ref="addFormref"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item label="博物馆名称" prop="mname"><el-col :span="12">
          <el-input v-model="addfrom.mname"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="藏品名称" prop="cname"><el-col :span="12">
          <el-input v-model="addfrom.cname"></el-input></el-col>
        </el-form-item>
        <el-form-item label="藏品介绍" prop="cintro">
          <el-input type="textarea" :rows="3" v-model="addfrom.cintro"></el-input>
        </el-form-item> 
        <el-form-item label="视频" prop="cvideo">
          <el-input v-model="addfrom.cvideo"></el-input>
        </el-form-item> 
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="resetForm">清 空</el-button>
        <el-button type="primary" @click="upForm">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改员工信息弹出层 -->
    <el-dialog title="修改藏品信息" :visible.sync="updateDialogVisible" width="50%">
      <el-form
        :model="updatefrom"
        :rules="updaterules"
        ref="updateFormref"
        label-width="100px"
        class="demo-ruleForm"
      >
     
        <el-form-item label="藏品名称" prop="cname"><el-col :span="12">
          <el-input v-model="updatefrom.cname" disabled></el-input></el-col>
        </el-form-item>

         <el-form-item label="博物馆名称" prop="mname"><el-col :span="12">
          <el-input v-model="updatefrom.mname"></el-input></el-col>
        </el-form-item>

        
        <el-form-item label="藏品介绍" prop="cintro">
          <el-input type="textarea" :rows="3"v-model="updatefrom.cintro"></el-input>
        </el-form-item> 
        <el-form-item label="视频地址" prop="cvideo">
          <el-input v-model="updatefrom.cvideo"></el-input>
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
  name: "collection",
  data() {
    return {
       username:"",
      input: "",
      collection_show: [],
      adddialogVisible: false,
      addfrom: {
        mname: '',
        cname: '',
        cintro: '',
        cvideo: '',
      },
      addrules: {
        mname: [
          { required: true, message: "请输入博物馆名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }
        ],
        cname: [{ required: true, message: "请输入藏品名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }],
        cintro: [{ required: true, message: "请输入藏品介绍", trigger: "blur" },
          { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        cvideo: [{ required: true, message: "请输入视频地址", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }]
      },
      updateDialogVisible: false,
      updatefrom: {
       mname: '',
        cname: '',
        cintro: '',
        cvideo: '',
      },
      updaterules: {
        mname: [
          { required: true, message: "请输入博物馆名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }
        ],
        cname: [{ required: true, message: "请输入藏品名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }],
        cintro: [{ required: true, message: "请输入藏品介绍", trigger: "blur" },
          { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        cvideo: [{ required: true, message: "请输入视频地址", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }]
      },
    };
  },
  created() {
    this.username=window.sessionStorage.getItem('uname')
    this.findcollection()
  },
  methods: {
    upForm() {
      this.$refs.addFormref.validate(valid => {
        if (valid) {
          this.axios.post("/api/addcollection", this.addfrom,
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
            this.findcollection();
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
    findcollection() {
      this.axios
        .get("/api/findcollection", {
          params: {
            
            mname: this.input
          }
        })
        .then(response => {

          this.collection_show = response.data;

        })
        .catch(error => {
          console.log(error);
        });
    },
    async remove(cname) {
      const confirmRes = await this.$confirm(
        "是否确定永久删除该藏品信息?",
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
        .get("/api/removecollection", {
          params: {
          cname: cname,
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
          this.findcollection();
        });
    },
 
    show(cname) {
      
      this.axios
        .get("/api/collection_cname", {
          params: {
        cname:cname,
        username: this.username
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
        console.log(this.updatefrom)
        this.axios.post("/api/updatecollection", this.updatefrom,
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
          this.findcollection();
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
    }
  }
  .el-table {
    margin-top: 40px;
  }
}
</style>
