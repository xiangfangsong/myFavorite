<template>
    <div class="header">
        <div class="logo">管理</div>
        <div class="user-info">
            <el-dropdown trigger="click" @command="handleCommand">
                <span class="el-dropdown-link">
                    <img class="user-logo" src="../../../static/img/img.jpg">
                    {{username}}
                </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item command="change_pass">修改密码</el-dropdown-item>
                    <el-dropdown-item command="loginout">退出</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>
        <el-dialog
            width="30%"
            title="修改密码"
            :visible.sync="dialogFormVisibleed1">
            <div class="form-box">
                <el-form :model="form1" :rules="rules1" ref="form1" label-width="150px">
                    <el-form-item label="新密码" prop="name">
                        <el-input v-model="password1" type="password" placeholder="请输入新密码"></el-input>
                    </el-form-item>
                    <el-form-item label="确认密码" prop="name">
                        <el-input v-model="password2" type="password" placeholder="请输入确认密码"></el-input>
                    </el-form-item>
                    <el-form-item style="text-align: center" >
                        <el-button @click="dialogFormVisibleed1 = false">取消</el-button>
                        <el-button type="primary" @click="submit()">确认</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </el-dialog>
    </div>
</template>
<script>
    import main from "../../main";
    export default {
        data() {
            return {
                name: '用户名',
                dialogFormVisibleed1:false,
                password1:'',
                password2:'',
                form1:{},
            }
        },
        computed:{
            username(){
                let username = localStorage.getItem('username');
                return username ? username : this.name;
            }
        },
        methods:{
            handleCommand(command) {
                if(command == 'loginout'){
                    localStorage.removeItem('username');
                    localStorage.removeItem('role');
                    localStorage.removeItem('id');
                    this.$router.push('/');
                }
                else if(command == 'change_pass'){this.dialogFormVisibleed1 = true}
            },
            submit(){
                if(this.password1==="")
                    this.$message({type: 'info', message: '密码不能为空！'});
                else if(this.password1!==this.password2)
                    this.$message({type: 'info', message: '确认密码与新密码不一致！'});
                else{
                    let crypto = require('crypto');
                    const md5 = crypto.createHash('md5');
                    md5.update(this.password1);
                    let md5password = md5.digest('hex');
                    this.$http.post(main.url+"/login/update",
                        {
                            'id': localStorage.getItem('id'),
                            'password': md5password,
                        },
                        {
                            headers: {'Content-Type':'application/x-www-form-urlencoded'},
                            emulateJSON: true
                        }).then(
                        success=>{this.$message({type: 'success', message: '密码修改成功！'})}
                    );
                    this.dialogFormVisibleed1 = false;
                }
            }
        }
    }
</script>
<style scoped>
    .header {
        position: relative;
        box-sizing: border-box;
        width: 100%;
        height: 70px;
        font-size: 22px;
        line-height: 70px;
        color: #fff;
    }
    .header .logo{
        float: left;
        width:250px;
        text-align: center;
    }
    .user-info {
        float: right;
        padding-right: 50px;
        font-size: 16px;
        color: #fff;
    }
    .user-info .el-dropdown-link{
        position: relative;
        display: inline-block;
        padding-left: 50px;
        color: #fff;
        cursor: pointer;
        vertical-align: middle;
    }
    .user-info .user-logo{
        position: absolute;
        left:0;
        top:15px;
        width:40px;
        height:40px;
        border-radius: 50%;
    }
    .el-dropdown-menu__item{
        text-align: center;
    }
</style>
