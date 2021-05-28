<template>
  <div class="show">
    <!-- 头部搜索 -->
    <div class="search">
      <el-row>
        <el-col :span="20">
          <div class="grid-content bg-purple">
            <el-select clearable v-model="option" placeholder="所有角色">
              <el-option v-for="item in post" :key="item.id" :label="item.name" :value="item.id"></el-option>
            </el-select>
            <el-input v-model="input" placeholder="输入你想搜索的用户名称" clearable></el-input>
            <el-button plain @click="findstaff">搜索</el-button>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-button type="primary" @click="adddialogVisible = true">添加用户</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    <!-- 表格 -->
    <el-table :data="staff_show" style="width: 100%" border stripe>
      <el-table-column align="center" type="index" label="#" width="120px"></el-table-column>
      <el-table-column align="center" prop="uname" label="姓名" width="170px"></el-table-column>
      <el-table-column align="center" prop="upwd" label="密码"width="220px"></el-table-column>
      <el-table-column align="center" prop="uphone" label="手机号" width="220px">
      </el-table-column>
      <el-table-column align="center" prop="poid" label="角色" width="220px"></el-table-column>
      <el-table-column align="center" label="操作" >
        <template v-slot="scope" align="center">
          <!-- 修改 -->
          <el-tooltip class="item"id="change" effect="dark" content="修改" placement="top" :enterable="false">
            <el-button type="primary" icon="el-icon-edit" circle @click="show(scope.row.id)"></el-button>
          </el-tooltip>
          <!-- 删除 -->
          <el-tooltip class="item"id="delete" effect="dark" content="删除" placement="top" :enterable="false">
            <el-button
              type="danger"
              icon="el-icon-delete-solid"
              circle
              @click="remove(scope.row.id)"
            ></el-button>
          </el-tooltip>
           </el-col>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加用户弹出层 -->
    <el-dialog title="添加用户" :visible.sync="adddialogVisible" width="50%">
      <el-form
        :model="addfrom"
        :rules="addrules"
        ref="addFormref"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item label="用户名" prop="uname">
          <el-col :span="12">
          <el-input v-model="addfrom.uname" ></el-input>
          </el-col >
        </el-form-item>

        <el-form-item label="密码" prop="upwd">
          <el-col :span="18">
          <el-input v-model="addfrom.upwd"></el-input>
          </el-col >
        </el-form-item>

        <el-form-item label="角色" prop="poid">
          <el-select v-model="addfrom.poid" placeholder="请选择角色">
            <el-option v-for="item in post" :key="item.id" :label="item.name" :value="item.id"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="手机号" prop="uphone">
          <el-col :span="18">
          <el-input v-model="addfrom.uphone"></el-input>
          </el-col >
        </el-form-item> 
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="resetForm">清 空</el-button>
        <el-button type="primary" @click="upForm">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改员工信息弹出层 -->
    <el-dialog title="修改用户" :visible.sync="updateDialogVisible" width="50%">
      <el-form
        :model="updatefrom"
        :rules="updaterules"
        ref="updateFormref"
        label-width="100px"
        class="demo-ruleForm"
      >
       <el-form-item label="用户名" prop="uname">
         <el-col :span="12">
          <el-input v-model="updatefrom.uname"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="密码" prop="upwd">
          <el-col :span="18">
          <el-input v-model="updatefrom.upwd"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="角色" prop="poid">
          <el-select v-model="updatefrom.poid" placeholder="请选择角色">
            <el-option v-for="item in post" :key="item.id" :label="item.name" :value="item.id"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="手机号" prop="uphone">
          <el-col :span="18">
          <el-input v-model="updatefrom.uphone"></el-input>
          </el-col>
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
  name: "list",
  data() {
          //验证手机号的校验规则
        var checkMolbile=(rule,value,callback)=>{
            const regMobile=/^(0|86|17951)?(13[0-9]|15[012356789]|17[678]|18[0-9]14[57])[0-9]{8}$/
            if(regMobile.test(value)){
                //合法的邮箱
                return callback()
            }
            callback(new Error('请输入合法的电话'))
        }
        var checkPassword=(rule,value,callback)=>{
            const regPassword=/^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,16}$/
            if(regPassword.test(value)){
                //合法的邮箱
                return callback()
            }
            callback(new Error('请输入同时包含数字和字母的6到16位密码'))
        }
    return {
      username:"",
       post: [],
      // 搜索选择的角色类型
      option: "",
      // 输入的搜索内容
      input: "",
      // 用户信息
      staff_show: [],
      //   添加对话框的显示隐藏
      adddialogVisible: false,
      //   添加表单的信息
      addfrom: {
        uname: '',
        upwd: '',
        uphone: '',
        poid: ''
      },
      //   添加表单的验证规则
      addrules: {
        uname: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 1, max: 8, message: "长度在 1 到 8 个字符", trigger: "blur" }
        ],
        upwd: [{ required: true, message: "请输入密码", trigger: "blur" },
         {validator:checkPassword,trigger:'blur'}],
        poid: [{ required: true, message: "请选择角色类型", trigger: "blur" }],
        uphone: [{ required: true, message: '请输入电话', trigger: 'blur' },
                     {validator:checkMolbile,trigger:'blur'}]
      },
      // 用户编辑对话框的显示与隐藏
      updateDialogVisible: false,
      // 获取的用户对象
      updatefrom: {
        uname: "",
        upwd: "",
        poid: "",
        uphone: "",
      },
      // 修改提示框的用户规则
      updaterules: {
        uname: [
          { required: true, message: "请输入用户名", trigger: "blur" },
          { min: 1, max: 8, message: "长度在 1 到 8 个字符", trigger: "blur" }
        ],
        upwd: [{ required: true, message: "请输入密码", trigger: "blur" },
         {validator:checkPassword,trigger:'blur'}],
        poid: [{ required: true, message: "请选择角色类型", trigger: "blur" }],
        uphone: [{ required: true, message: '请输入电话', trigger: 'blur' },
                     {validator:checkMolbile,trigger:'blur'}]
      },
    };
  },
  created() {
     this.username=window.sessionStorage.getItem('uname')
     this.getpost();
     this.findstaff(); 
  },
  methods: {
      getpost() {
      this.axios
        .get("/api/getpost")
        .then(response => {
          // console.log(response);
          this.post = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 提交添加用户表单
    upForm() {
      this.$refs.addFormref.validate(valid => {
        if (valid) {
          this.axios.post("/api/addstaff", 
          this.addfrom,{
          params: {
            username: this.username
          }}
          ).then(res => {
            //console.log(res.data)
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
            // 刷新用户列表数据
            this.findstaff();
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
    // 按照搜索内容搜索用户
    findstaff() {
      this.axios
        .get("/api/findstaff", {
          params: {
            poid: this.option,
            uname: this.input
          }
        })
        .then(response => {
          this.staff_show = response.data;
      //  console.log(response.data)
   
          for (let i = 0; i < this.staff_show.length; i++) {
            for (let j = 0; j < this.post.length; j++) {
              if (this.staff_show[i].poid === this.post[j].id)
               {
                this.staff_show[i].poid = this.post[j].name;
              }
            }
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 删除员工
    async remove(id) {
      const confirmRes = await this.$confirm(
        "是否确定永久删除该用户 ?",
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
        .get("/api/removestaff", {
          params: {
            id: id,
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
          // 刷新用户列表
         this.findstaff(); 
        });
    },
    // 展示编辑用户对话框
    show(id) {
      // 请求该用户的数据
      this.axios
        .get("/api/staff_id", {
          params: {
            id: id,
            username:this.username
          }
        })
        .then(response => {
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
       // console.log(this.updatefrom)
        this.axios.post("/api/update", this.updatefrom,
        {
          params: {
            username: this.username
          }}).then(res => {
          // console.log(res)
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "修改失败"
            });
          }
          // 关闭修改对话框
          this.updateDialogVisible = false;
          // 刷新数据
          this.findstaff(); ;
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
#change{
  margin-left: 0px;
}
#delete{
  margin-left: 25px ;
}
</style>
