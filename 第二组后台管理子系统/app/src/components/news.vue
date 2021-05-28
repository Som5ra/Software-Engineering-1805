<template>
  <div class="show">
    <!-- 头部搜索 -->
    <div class="search">
      <el-row>
        <el-col :span="20">
          <div class="grid-content bg-purple">
            <el-input v-model="input" placeholder="输入搜索的博物馆名称或新闻标题" clearable></el-input>
            <el-button plain @click="findnews">搜索</el-button>
          </div>
        </el-col>
        <el-col :span="4">
          <div class="grid-content bg-purple-light">
            <el-button type="primary" @click="adddialogVisible = true">添加新闻</el-button>
          </div>
        </el-col>
      </el-row>
    </div>
    <!-- 表格 -->
    <el-table :data="news_show" style="width: 100%" border stripe>
      <el-table-column align="center" type="index" label="#" width="50"></el-table-column>
      <el-table-column align="center" prop="mname" label="博物馆名称" width="100"></el-table-column>
      <el-table-column align="center" prop="nname" label="新闻标题" width="100"></el-table-column>
      <el-table-column align="center" prop="ntime" label="发布时间" width="100">
          <template v-slot="scope">{{ formateDate(scope.row.ntime) }}</template>
      </el-table-column>
    <!-- <el-table-column align="center" prop="nimg" label="新闻图片"></el-table-column> -->
    <el-table-column align="center" prop="nsource" label="新闻来源" width="100"></el-table-column>
     <el-table-column align="center" prop="nurl" label="次级新闻网站" width="100"></el-table-column>
      <el-table-column align="center" prop="nstatus" label="新闻状态" width="100"></el-table-column>
      <el-table-column align="center" prop="nintro" label="新闻介绍"></el-table-column>
      <el-table-column align="center" label="操作" width="130">
        <template v-slot="scope">
          <!-- 修改 -->
          <el-tooltip class="item" effect="dark" content="修改" placement="top" :enterable="false">
            <el-button type="primary" icon="el-icon-edit" circle @click="show(scope.row.nname)"></el-button>
          </el-tooltip>
          <!-- 删除 -->
          <el-tooltip class="item" effect="dark" content="删除" placement="top" :enterable="false">
            <el-button
              type="danger"
              icon="el-icon-delete-solid"
              circle
              @click="remove(scope.row.nname)"
            ></el-button>
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加用户弹出层 -->
    <el-dialog title="添加新闻" :visible.sync="adddialogVisible" width="50%">
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

        <el-form-item label="新闻标题" prop="nname"><el-col :span="12">
          <el-input v-model="addfrom.nname" ></el-input></el-col>
        </el-form-item>

        <el-form-item label="发布时间" prop="ntime">
          <el-col :span="9">
            <el-form-item prop="ntime">
              <el-date-picker
                format="yyyy 年 MM 月 dd 日"
                value-format="yyyy-MM-dd"
                placeholder="选择日期"
                v-model="addfrom.ntime"
                style="width: 100%;"
              ></el-date-picker>
            </el-form-item>
          </el-col>
        </el-form-item>

        <!-- <el-form-item label="新闻图片" prop="uphone">
          <el-input v-model="addfrom.nimg"></el-input>
        </el-form-item>  -->

        <el-form-item label="新闻介绍" prop="nintro">
          <el-input type="textarea" :rows="3" v-model="addfrom.nintro"></el-input>
        </el-form-item>
        
        <el-form-item label="新闻来源" prop="nsource">
          <el-input v-model="addfrom.nsource"></el-input>
        </el-form-item>

        <el-form-item label="次级新闻网站" prop="nurl">
          <el-input v-model="addfrom.nurl"></el-input>
        </el-form-item>

        <el-form-item label="新闻状态" prop="nstatus">
          <el-input v-model="addfrom.nstatus"></el-input>
        </el-form-item>

      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="resetForm">清 空</el-button>
        <el-button type="primary" @click="upForm">确 定</el-button>
      </span>
    </el-dialog>

    <!-- 修改新闻信息弹出层 -->
    <el-dialog title="修改新闻内容" :visible.sync="updateDialogVisible" width="50%">
      <el-form
        :model="updatefrom"
        :rules="updaterules"
        ref="updateFormref"
        label-width="110px"
        class="demo-ruleForm"
      >

       <el-form-item label="新闻标题" prop="nname"><el-col :span="12"
          <el-input v-model="updatefrom.nname" disabled></el-input></el-col>
        </el-form-item>

        <el-form-item label="博物馆名称" prop="mname"><el-col :span="12"
          <el-input v-model="updatefrom.mname"></el-input></el-col>
        </el-form-item>

       

        <el-form-item label="发布时间" prop="ntime">
          <el-col :span="9">
            <el-form-item prop="ntime">
              <el-date-picker
                format="yyyy 年 MM 月 dd 日"
                value-format="yyyy-MM-dd"
                placeholder="选择日期"
                v-model="updatefrom.ntime"
                style="width: 100%;"
              ></el-date-picker>
            </el-form-item>
          </el-col>
        </el-form-item>

        <!-- <el-form-item label="新闻图片" prop="uphone">
          <el-input v-model="addfrom.nimg"></el-input>
        </el-form-item>  -->

        <el-form-item label="新闻介绍" prop="nintro">
          <el-input type="textarea" :rows="3"v-model="updatefrom.nintro"></el-input>
        </el-form-item>
        
        <el-form-item label="新闻来源" prop="nsource">
          <el-input v-model="updatefrom.nsource"></el-input>
        </el-form-item>

        <el-form-item label="次级新闻网站" prop="nurl">
          <el-input v-model="updatefrom.nurl"></el-input>
        </el-form-item>

        <el-form-item label="新闻状态" prop="nstatus">
          <el-input v-model="updatefrom.nstatus"></el-input>
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
import App from '../App.vue';
export default {
  components: { App },
  name: "news",
  data() {
    return {
      username:"",
      input: "",
      news_show: [],
      adddialogVisible: false,
      addfrom: {
        mname: '',
        nname:'',
        ntime:'',
        //nimg:'',
        nintro: '',
        nsource: '',
        nurl: '',
        nstatus:''
      },
      addrules: {
        mname: [
          { required: true, message: "请输入博物馆名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }
        ],
        nname: [
          { required: true, message: "请输入新闻标题", trigger: "blur" },
          { min: 1, max: 30, message: "长度在 1 到 30 个字符", trigger: "blur" }
        ],
        ntime: [{
            required: true,
            message: "请选择日期",
            trigger: "change"
          }],
        nintro: [{ required: true, message: "请输入新闻介绍", trigger: "blur" },
          { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        nsource: [{ required: true, message: "请输入新闻来源", trigger: "blur" },
          { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        nurl: [{ required: true, message: "请输入次级新闻网站", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        nstatus: [{ required: true, message: "请选择新闻状态", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
      },
      updateDialogVisible: false,
      updatefrom: {
        mname: '',
        nname:'',
        ntime:'',
       // nimg:'',
       nintro:'',
       nsource:'',
       nurl:'',
       nstatus:''
      },
  
      updaterules: {
        mname:[
          { required: true, message: "请输入博物馆名称", trigger: "blur" },
          { min: 1, max: 20, message: "长度在 1 到 20 个字符", trigger: "blur" }
        ],
        nname: [
          { required: true, message: "请输入新闻标题", trigger: "blur" },
          { min: 1, max: 30, message: "长度在 1 到 30 个字符", trigger: "blur" }
        ],
        ntime: [{
            required: true,
            message: "请选择日期",
            trigger: "change"
          }],
        nintro: [{ required: true, message: "请输入新闻介绍", trigger: "blur" },
          { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        nsource: [{ required: true, message: "请输入新闻来源", trigger: "blur" },
          { min: 1, max: 100, message: "长度100字以内", trigger: "blur" }],
        nurl: [{ required: true, message: "请输入次级新闻网站", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
        nstatus: [{ required: true, message: "请选择新闻状态", trigger: "blur" },
          { min: 1, max: 50, message: "长度在 1 到 50 个字符", trigger: "blur" }],
      },
    };
  },
  created() {
     this.username=window.sessionStorage.getItem('uname')
    this.findnews()
  },
  methods: {
    upForm() {
      this.$refs.addFormref.validate(valid => {
        if (valid) {
          this.axios.post("/api/addnews", this.addfrom,
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
            this.findnews();
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
 
    findnews() {
      this.axios
        .get("/api/findnews", {
          params: {
            nname: this.input
          }
        })
        .then(response => {
          this.news_show = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    async remove(nname) {
      const confirmRes = await this.$confirm(
        "是否确定永久删除该条新闻?",
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
        .get("/api/removenews", {
          params: {
          nname:nname,
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
          })
          this.findnews();
        });
    },
    show(nname) {

      this.axios
        .get("/api/news_nname", {
          params: {
        nname:nname,
        username: this.username
          }
        })
        .then(response => {
        
          this.updatefrom = response.data[0];
          this.updatefrom.ntime=this.formateDate(this.updatefrom.ntime); 
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

        this.updatefrom.ntime= this.formateDate(this.updatefrom.ntime)

        this.axios.post("/api/updatenews", this.updatefrom,
        {
          params: {
            username: this.username
          }}).then(res => {
    
           console.log(this.updatefrom)
          if (res.data.code !== 200) {
            return this.$message.error({
              duration: 800,
              message: "修改失败"
            });
          }

          this.updateDialogVisible = false;
          this.findnews();
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
  },

  
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
.el-form-item__label{
    font-size: 13px!important;
}



</style>
