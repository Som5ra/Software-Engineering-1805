<template>
  <div class="show">
    <!-- 头部搜索 -->
    <div class="search">
      <el-row>
        <el-col :span="20">
          <div class="grid-content bg-purple">
            <el-input v-model="input" placeholder="输入你想搜索博物馆或展览名称" clearable></el-input>
            <el-button plain @click="findexhibition">搜索</el-button>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-button type="primary" @click="adddialogVisible = true">添加展览</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    <!-- 表格 -->
    <el-table :data="exhibition_show" style="width: 100%" border stripe>
      <el-table-column align="center" type="index" label="#" width="80"></el-table-column>
      <el-table-column align="center" prop="mname" label="博物馆名称"width="150"></el-table-column>
      <el-table-column align="center" prop="exname" label="展览名称"width="100"></el-table-column>
      <el-table-column align="center" prop="extime" label="展览时间"width="100">
        <template v-slot="scope">{{ formateDate(scope.row.extime) }}</template>
      </el-table-column>
    <el-table-column align="center" prop="exaddr" label="展览地点"width="100"></el-table-column>
      <el-table-column align="center" prop="exvedio" label="视频"width="100"></el-table-column>
        <el-table-column align="center" prop="exintro" label="展览介绍" ></el-table-column>
      <el-table-column align="center" label="操作" width="130">
        <template v-slot="scope">
          <!-- 修改 -->
          <el-tooltip class="item" effect="dark" content="修改" placement="top" :enterable="false">
            <el-button type="primary" icon="el-icon-edit" circle @click="show(scope.row.id)"></el-button>
          </el-tooltip>
          <!-- 删除 -->
          <el-tooltip class="item" effect="dark" content="删除" placement="top" :enterable="false">
            <el-button
              type="danger"
              icon="el-icon-delete-solid"
              circle
              @click="remove(scope.row.id)"
            ></el-button>
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加用户弹出层 -->
    <el-dialog title="添加展览" :visible.sync="adddialogVisible" width="50%">
      <el-form
        :model="addfrom"
        :rules="addrules"
        ref="addFormref"
        label-width="100px"
        class="demo-ruleForm"
      >
        <el-form-item label="博物馆名称" prop="mname"><el-col :span="12">
          <el-input v-model="addfrom.mname"></el-input>  </el-col>
        </el-form-item>

        <el-form-item label="展览名称" prop="exname"><el-col :span="12">
          <el-input v-model="addfrom.exname"></el-input> </el-col>
        </el-form-item>

        <el-form-item label="展览时间" prop="extime">
             <el-col :span="9">
            <el-form-item prop="extime">
              <el-date-picker
                format="yyyy 年 MM 月 dd 日"
                value-format="yyyy-MM-dd"
                placeholder="选择日期"
                v-model="addfrom.extime"
                style="width: 100%;"
              ></el-date-picker>
            </el-form-item>
          </el-col>
        </el-form-item>

        <el-form-item label="展览地点" prop="exaddr">
          <el-input v-model="addfrom.exaddr"></el-input>
        </el-form-item> 
        <el-form-item label="展览介绍" prop="exintro">
          <el-input  type="textarea" :rows="3"v-model="addfrom.exintro"></el-input>
        </el-form-item> 
        <el-form-item label="视频地址" prop="exvedio">
          <el-input v-model="addfrom.exvedio"></el-input>
        </el-form-item> 
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="resetForm">清 空</el-button>
        <el-button type="primary" @click="upForm">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改员工信息弹出层 -->
    <el-dialog title="修改展览信息" :visible.sync="updateDialogVisible" width="50%">
      <el-form
        :model="updatefrom"
        :rules="updaterules"
        ref="updateFormref"
        label-width="100px"
        class="demo-ruleForm"
      >
     
        <el-form-item label="博物馆名称" prop="mname"><el-col :span="12">
          <el-input v-model="updatefrom.mname"></el-input></el-col>
        </el-form-item>

        <el-form-item label="展览名称" prop="exname"><el-col :span="12">
          <el-input v-model="updatefrom.exname"></el-input></el-col>
        </el-form-item>

        <el-form-item label="展览时间" prop="extime">
            <el-col :span="9">
            <el-form-item prop="extime">
              <el-date-picker
                format="yyyy 年 MM 月 dd 日"
                value-format="yyyy-MM-dd"
                placeholder="选择日期"
                v-model="updatefrom.extime"
                style="width: 100%;"
              ></el-date-picker>
            </el-form-item>
          </el-col>
        </el-form-item>
        <el-form-item label="展览地点" prop="exaddr">
          <el-input v-model="updatefrom.exaddr"></el-input>
        </el-form-item> 
        <el-form-item label="展览介绍" prop="exintro">
          <el-input type="textarea" :rows="3" v-model="updatefrom.exintro"></el-input>
        </el-form-item> 
        <el-form-item label="视频" prop="exvedio">
          <el-input v-model="updatefrom.exvedio"></el-input>
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
  name: "exhibition",
  data() {
    return {
       username:"",
      input: "",
      exhibition_show: [],
      adddialogVisible: false,
      addfrom: {
        mname: '',
        exname: '',
        extime: '',
        exaddr: '',
        exintro:'',
        exvedio:'',
      },
      addrules: {
        mname: [
          { required: true, message: "请输入博物馆名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }
        ],
        exname: [{ required: true, message: "请输入展览名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }],
        extime: [{
            required: true,
            message: "请选择日期",
            trigger: "change"
          }],
        exaddr: [{ required: true, message: "请输入展览地点", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        exintro: [{ required: true, message: "请输入展览介绍", trigger: "blur" },
          { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        exvedio: [{ required: true, message: "请输入视频地址", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }]
      },
      updateDialogVisible: false,
      updatefrom: {
        mname: '',
        exname: '',
        extime: '',
        exaddr: '',
       // mimg:'',
        exintro:'',
        exvedio:'',
      },
      // 修改提示框的用户规则
      updaterules: {
        mname: [
          { required: true, message: "请输入博物馆名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }
        ],
        exname: [{ required: true, message: "请输入展览名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }],
        extime: [{
            required: true,
            message: "请选择日期",
            trigger: "change"
          }],
        exaddr: [{ required: true, message: "请输入展览地点", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        exintro: [{ required: true, message: "请输入展览介绍", trigger: "blur" },
          { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        exvedio: [{ required: true, message: "请输入视频地址", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }]
      }
  }
  },
  created() {
     this.username=window.sessionStorage.getItem('uname')
    this.findexhibition()
  },
  methods: {
    upForm() {
      this.$refs.addFormref.validate(valid => {
        if (valid) {
          this.axios.post("/api/addexhibition", this.addfrom,
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
            this.findexhibition();
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
    findexhibition() {
      this.axios
        .get("/api/findexhibition", {
          params: {
            
            mname: this.input
          }
        })
        .then(response => {
          this.exhibition_show = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    async remove(id) {
      const confirmRes = await this.$confirm(
        "是否确定永久删除该展览信息?",
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
        .get("/api/removeexhibition", {
          params: {
          id:id,
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
          this.findexhibition();
        });
    },
    show(id) {
      this.axios
        .get("/api/exhibition_id", {
          params: {
        id:id,
        username: this.username
          }
        })
        .then(response => {
          this.updatefrom = response.data[0];
         this.updatefrom.extime=this.formateDate(this.updatefrom.extime); 
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
        this.updatefrom.extime= this.formateDate(this.updatefrom.extime)
        this.axios.post("/api/updateexhibition", this.updatefrom,
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
          this.findexhibition();
          this.$message.success({
            duration: 800,
            message: "修改成功"
          });
        });
      });
    },
    formateDate(datetime) {
      // let  = "2019-11-06T16:00:00.000Z"
      function addDateZero(num) {
        return num < 10 ? "0" + num : num;
      }
      let d = new Date(datetime);
      let formatdatetime =
        d.getFullYear() +
        "-" +
        addDateZero(d.getMonth() + 1) +
        "-" +
        addDateZero(d.getDate());
      return formatdatetime;
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
