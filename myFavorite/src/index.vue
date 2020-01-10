<template>
    <div class="login-wrap">
        <div class="ms-title" style="font-size: 30px">我的收藏夹<span style="font-size: 10px; margin-left: 73px;">
            <u></u></span>
        </div>
        <div class="tab">
            <el-table :data="data" border ref="multipleTable" >
                <el-table-column label="网站名称" prop="wname" width="100px" ></el-table-column>
                <el-table-column label="网站地址" prop="wurl" width="300px" ></el-table-column>
                <el-table-column label="点击次数" prop="count" width="70px" ></el-table-column>
                <el-table-column label="创建时间" prop="ctime" width="250px" ></el-table-column>
                <el-table-column label="操作" width="80px" >
                    <template slot-scope="scope" width="100px">
                        <el-button type="text" @click="gotourl(scope.row)" >进入</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
        <el-button type="primary" @click="submit()" >登录</el-button>
    </div>
</template>

<script>
    import main from './main';
    export default {
        data: function(){
            return {
                dialogVisible:false,
                data:[]
            }
        },
        created(){
            this.init();
        },
        methods: {
            init(){
                this.$http.post(main.url+"/favorite/list",
                    {'uid': 0},
                    {
                        headers: {'Content-Type':'application/x-www-form-urlencoded'},
                        emulateJSON: true
                    }).then(
                    success=>{
                        this.data=success.data;
                    }
                );
            },
            gotourl(row){ //进入指定的网站
                this.$http.post(main.url+"/favorite/count",
                    {'id': row.id},
                    {
                        headers: {'Content-Type':'application/x-www-form-urlencoded'},
                        emulateJSON: true
                    }).then(
                    success=> {
                        window.open(row.wurl, "_blank");
                        this.init();
                    }
                )
            },
            submit(){
                this.$router.push({ path: '/login' });
            }
        }
    }
</script>

<style scoped>
    .tab{
        position: absolute;
        top: 20%;
        left: 25%;
        width: 805px;
        height: 100%;
    }
    .login-wrap{
        position: relative;
        background: url("/static/img/bg.jpg") no-repeat center;
        width:100%;
        height:100%;
    }
    .ms-title{
        position: absolute;
        top: 40%;
        width: 100%;
        margin-top: -230px;
        text-align: center;
        font-size: 14px;
        color: #fff;
        font-weight: bold;
    }
    .login-btn button{
        position: absolute;
        width: 40%;
        height: 35px;
        right: 10%;
        top: 10%;
    }
</style>
