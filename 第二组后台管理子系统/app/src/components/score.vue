<template>
  <div class="show">
    <!-- 头部搜索 -->
    <div class="search">
      <el-row>
        <el-col :span="20">
          <div class="grid-content bg-purple">
            <el-input v-model="input" placeholder="输入搜索的博物馆或用户名" clearable></el-input>
            <el-button plain @click="findscore">搜索</el-button>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-button type="primary" @click="adddialogVisible = true">添加评价</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    <!-- 表格 -->
    <el-table :data="score_show" style="width: 100%" border stripe>
      <el-table-column align="center" type="index" label="#" width="50"></el-table-column>
      <el-table-column align="center" prop="mname" label="博物馆名称"width="100"></el-table-column>
      <el-table-column align="center" prop="uname" label="用户名"width="100"></el-table-column>
      <el-table-column align="center" prop="evalscore" label="评价分数" width="100"></el-table-column>

    <!-- <el-table-column align="center" prop="evalimg" label="评价上传图片"></el-table-column> -->
    <el-table-column align="center" prop="evalscore_ex" label="展览评价分数"width="130"></el-table-column>
     <el-table-column align="center" prop="evalscore_serv" label="服务评价分数"width="130"></el-table-column>
      <el-table-column align="center" prop="evalscore_environ" label="环境评价分数"width="130"></el-table-column>
      <el-table-column label="发布评论权限"width="130" >
            <template slot-scope="scope">
                <!-- {{scope.row}} -->
                <el-switch
                    v-model="scope.row.scorestatus"
                    @change="userStateChanged(scope.row.scorestatus,scope.row.uname)">
                </el-switch>
            </template>
        </el-table-column>
        <el-table-column align="center" prop="evalintro" label="评价内容"></el-table-column>
      <el-table-column align="center" label="操作" width="130">
        <template v-slot="scope">
          <!-- 修改 -->
          <el-tooltip class="item" effect="dark" content="修改" placement="top" :enterable="false">
            <el-button type="primary" icon="el-icon-edit" circle @click="show(scope.row.uname)"></el-button>
          </el-tooltip>
          <!-- 删除 -->
          <el-tooltip class="item" effect="dark" content="删除" placement="top" :enterable="false">
            <el-button
              type="danger"
              icon="el-icon-delete-solid"
              circle
              @click="remove(scope.row.uname)"
            ></el-button>
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加评价弹出层 -->
    <el-dialog title="添加评价" :visible.sync="adddialogVisible" width="50%">
      <el-form
        :model="addfrom"
        :rules="addrules"
        ref="addFormref"
        label-width="110px"
        class="demo-ruleForm"
      >
        <el-form-item label="博物馆名称" prop="mname"><el-col :span="12">
          <el-input v-model="addfrom.mname"></el-input></el-col>
        </el-form-item>

        <el-form-item label="用户名" prop="uname"><el-col :span="12">
          <el-input v-model="addfrom.uname"></el-input></el-col>
        </el-form-item>

        <el-form-item label="评价分数" prop="evalscore">
          <el-select v-model="addfrom.evalscore" clearable placeholder="请选择">
          <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
          </el-select>
        </el-form-item>      
        <el-form-item label="展览评价分数" prop="evalscore_ex">
          <el-select v-model="addfrom.evalscore_ex" clearable placeholder="请选择">
          <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="服务评价分数" prop="evalscore_serv">
          <el-select v-model="addfrom.evalscore_serv" clearable placeholder="请选择">
          <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="环境评价分数" prop="evalscore_environ">
          <el-select v-model="addfrom.evalscore_environ" clearable placeholder="请选择">
          <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
          </el-select>
        </el-form-item>
 <el-form-item label="评价内容" prop="evalintro">
          <el-input type="textarea" :rows="3"v-model="addfrom.evalintro"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="resetForm">清 空</el-button>
        <el-button type="primary" @click="upForm">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改评价信息弹出层 -->
     <el-dialog title="修改评价" :visible.sync="updateDialogVisible" width="50%">
      <el-form
        :model="updatefrom"
        :rules="updaterules"
        ref="updateFormref"
        label-width="110px"
        class="demo-ruleForm"
      >
         <el-form-item label="用户名" prop="uname"><el-col :span="12">
          <el-input v-model="updatefrom.uname" disabled></el-input></el-col>
        </el-form-item>
        <el-form-item label="博物馆名称" prop="mname"><el-col :span="12">
          <el-input v-model="updatefrom.mname"></el-input></el-col>
        </el-form-item>

        <el-form-item label="评价分数" prop="evalscore">
          <el-select v-model="updatefrom.evalscore" clearable placeholder="请选择">
          <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
          </el-select>
        </el-form-item>      
        <el-form-item label="展览评价分数" prop="evalscore_ex">
          <el-select v-model="updatefrom.evalscore_ex" clearable placeholder="请选择">
          <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="服务评价分数" prop="evalscore_serv">
          <el-select v-model="updatefrom.evalscore_serv" clearable placeholder="请选择">
          <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="环境评价分数" prop="evalscore_environ">
          <el-select v-model="updatefrom.evalscore_environ" clearable placeholder="请选择">
          <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
          </el-select>
        </el-form-item>
 <el-form-item label="评价内容" prop="evalintro">
          <el-input type="textarea" :rows="3"v-model="updatefrom.evalintro"></el-input>
        </el-form-item>
      </el-form>
       <span slot="footer" class="dialog-footer">
        <el-button @click="resetForm2">清 空</el-button>
        <el-button type="primary" @click="setForm">确 定</el-button>
      </span>
    </el-dialog>
    </el-dialog>

  </div>
</template>
     

<script>
export default {
  name: "news",
  data() {
    return {
  username:"",
      input: "",
      options: [{
          value: '1',
          label: '1'
        }, {
          value: '2',
          label: '2'
        }, {
          value: '3',
          label: '3'
        }, {
          value: '4',
          label: '4'
        }, {
          value: '5',
          label: '5'
        }],
      score_show: [],

      adddialogVisible: false,
  
      addfrom: {
        mname: '',
        uname:'',
        evalscore:'',
        evalintro: '',
        //evalimg:'',
        evalscore_ex: '',
        evalscore_serv: '',
        evalscore_environ:''
      },
     
      addrules: {
        mname: [
          { required: true, message: "请输入博物馆名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }
        ],
        uname: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 1, max: 10, message: "长度在 1 到 10 个字符", trigger: "blur" }
        ],
        evalintro: [{ required: true, message: "请输入评价内容", trigger: "blur" },
          { min: 1, max: 100, message: "长度在100字以内", trigger: "blur" }],
       // evalimg: [{ required: true, message: "请输入评价上传图片", trigger: "change" }],
      },
  
      updateDialogVisible: false,

      updatefrom: {
        mname: '',
        uname:'',
        evalscore:'',
        evalintro:'',
       // evalimg:'',
        evalscore_ex:'',
        evalscore_serv:'',
        evalscore_environ:''
      },
  
      updaterules:  {
         mname: [
          { required: true, message: "请输入博物馆名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }
        ],
        uname: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 1, max: 10, message: "长度在 1 到 10 个字符", trigger: "blur" }
        ],
        evalintro: [{ required: true, message: "请输入评价内容", trigger: "blur" },
          { min: 1, max: 100, message: "长度在100字以内", trigger: "blur" }],
      },
    };
  },

  created() {
  this.username=window.sessionStorage.getItem('uname')
    this.findscore()
  },
  methods: {
    
    upForm() {
      this.$refs.addFormref.validate(valid => {
        if (valid) {
          this.axios.post("/api/addscore", this.addfrom,{
          params: {
            username: this.username
          }}
          ).then(res => {
           // console.log(res.data)
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
            // 隐藏对话框
            this.adddialogVisible = false;
            // 刷新评价列表数据
            this.findscore();
            // 清空输入表单
            this.resetForm();
          });
        } else {
          console.log("表单数据有错误");
          return false;
        }
      });
    },
    // 清空添加用户表单
    resetForm() {
      this.$refs.addFormref.resetFields();
    },
    // 按照搜索内容搜索员工
    findscore() {
      this.axios
        .get("/api/findscore", {
          params: {
            uname: this.input
          }
        })
        .then(response => {
           console.log(response.data)
          this.score_show = response.data;
        console.log(this.score_show)
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 删除评价
    async remove(uname) {
      const confirmRes = await this.$confirm(
        "是否确定永久删除该条评分?",
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
        .get("/api/removescore", {
          params: {
          uname:uname,
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
          // 刷新评价列表
          this.findscore();
        });
    },
    // 展示编辑评价对话框
    show(uname) {
      // 请求数据
      console.log('111')
      this.axios
        .get("/api/score_uname", {
          params: {
        uname:uname,
        username: this.username
          }
        })
        .then(response => {
          console.log(response)
          this.updatefrom = response.data[0];
        })
        .catch(error => {
          console.log(error);
        });
      // 展示编辑对话框
      this.updateDialogVisible = true;
    },
    // 弹出框关闭事件
    resetForm2() {
      this.$refs.updateFormref.resetFields();
    },
    // 提交修改信息
    setForm() {
      this.$refs.updateFormref.validate(valid => {
        if (!valid) return;
        
        this.axios.post("/api/updatescore", this.updatefrom,
        {
          params: {
            username: this.username
          }}).then(res => {
           //console.log('ss',res)
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "修改失败"
            });
          }
          // 关闭修改对话框
          this.updateDialogVisible = false;
          this.findscore();
          this.$message.success({
            duration: 800,
            message: "修改成功"
          });
        });
      });
    },
      async userStateChanged(scorestatus,uname){
        console.log(scorestatus,uname)
        this.axios
        .get("/api/updatescorestatus", {
          params: {
          scorestatus:scorestatus,
          uname:uname,
          username: this.username
          }
        })
        .then(res => {
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "修改失败"
            });
          }
          this.$message.success({
            duration: 800,
            message: "修改成功"
          });
          // 刷新评价列表
          scorestatus=!scorestatus
          console.log(scorestatus)
          //this.findscore();
        });
    },
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
