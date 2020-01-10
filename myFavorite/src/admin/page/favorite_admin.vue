<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-setting"></i> 管理</el-breadcrumb-item>
                <el-breadcrumb-item>收藏列表</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div>
            <el-table :data="data" border style="width: 90%" ref="multipleTable" >
                <el-table-column label="ID" prop="id" width="80px" ></el-table-column>
                <el-table-column label="网站名称" prop="wname" width="100px" ></el-table-column>
                <el-table-column label="网站地址" prop="wurl" width="300px" ></el-table-column>
                <el-table-column label="权限" prop="type" width="80px" ></el-table-column>
                <el-table-column label="点击次数" prop="count" width="70px" ></el-table-column>
                <el-table-column label="创建时间" prop="ctime" width="250px" ></el-table-column>
                <el-table-column label="操作" width="320px" >
                    <template slot-scope="scope" width="100px">
                        <el-button type="text" @click="gotourl(scope.row)" >进入</el-button>
                        <el-button type="text" @click="openedit(scope.row)" >修改</el-button>
                        <el-button type="text" @click="del_fav(scope.row)" >删除</el-button>
                    </template>
                </el-table-column>
            </el-table><el-button type="primary" @click="addfavorite()" align="center">添加新收藏</el-button>
        </div>
        <el-dialog
            width="30%"
            title="修改"
            :visible.sync="dialogFormVisibleed">
            <div>
                <el-form :model="form" :rules="rules" ref="form" label-width="150px">
                    <el-form-item label="网站名称" prop="wname">
                        <el-input v-model="form.wname" placeholder="请输入网站名称"></el-input>
                    </el-form-item>
                    <el-form-item label="网站地址" prop="password2">
                        <el-input v-model="form.wurl" placeholder="请输入网站地址"></el-input>
                    </el-form-item>
                    <el-form-item label="权限" prop="type">
                        <el-select v-model="form.type" placeholder="请设置权限">
                            <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item style="text-align: center" >
                        <el-button @click="dialogFormVisibleed = false" >取消</el-button>
                        <el-button type="primary" @click="submit('form')">修改</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </el-dialog>
        <el-dialog
            width="30%"
            title="添加收藏"
            :visible.sync="dialogFormVisibleed1">
            <div class="form-box">
                <el-form :model="form" :rules="rules" ref="form" label-width="150px">
                    <el-form-item label="网站名称" prop="wname">
                        <el-input v-model="form.wname" placeholder="请输入网站名称"></el-input>
                    </el-form-item>
                    <el-form-item label="网站地址" prop="wurl">
                        <el-input v-model="form.wurl" placeholder="请输入网站地址"></el-input>
                    </el-form-item>
                    <el-form-item label="权限" prop="type">
                        <el-select v-model="form.type" placeholder="请设置权限">
                            <el-option
                                v-for="item in options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item style="text-align: center" >
                        <el-button @click="dialogFormVisibleed1 = false" >取消</el-button>
                        <el-button type="primary" @click="addnew(form)">添加</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import main from "../../main";
    export default {
        data: function(){
            return {
                data:[],
                options:[{value: 0, label: "公开"},{value: 1, label: "私有"}],
                dialogFormVisibleed:false,
                dialogFormVisibleed1:false,
                form:{
                    id: '',
                    wname:'',
                    wurl:'',
                    type:''
                },
                rules:{
                    wname:[
                        {required:true,message:'请输入网站名称',trigger:'blur'}
                    ],
                    wurl:[
                        {required:true,message:'请输入网站地址',trigger:'blur'}
                    ],
                    type:[
                        {required:true,message:'请设置权限',trigger:'blur'}
                    ]
                }
            }
        },
        created(){
            if(localStorage.getItem('username')===""){
                this.$router.replace('/login')
            }else{this.init();}
        },
        methods:{
            init(){
                this.$http.post(main.url+"/favorite/list",
                    {'uid': localStorage.getItem('id')},
                    {
                        headers: {'Content-Type':'application/x-www-form-urlencoded'},
                        emulateJSON: true
                    }).then(
                    success=>{
                        this.data=success.data;
                        for(let i=0;i<this.data.length;i++){
                            if(this.data[i].type===0)
                                this.data[i].type = "公开";
                            else
                                this.data[i].type = "私有";
                        }
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
            openedit(row){ //修改收藏内容，按钮按下后
                this.dialogFormVisibleed=true;
                this.form={
                    id: row.id,
                    wname: row.wname,
                    wurl: row.wurl,
                    type: row.type==="公开"?0:1
                };
            },
            submit(form){ //修改收藏内容，提交
                this.$http.post(main.url+"/favorite/update",
                    {
                        'id': this.form.id,
                        'wname': this.form.wname,
                        'wurl': this.form.wurl,
                        'type': this.form.type
                    },
                    {
                        headers: {'Content-Type':'application/x-www-form-urlencoded'},
                        emulateJSON: true
                    }).then(
                    success=> {
                        this.$message({type: 'success', message: '修改成功'});
                        this.form={
                            id: '',
                            wname:'',
                            wurl:'',
                            type:''
                        };
                        this.dialogFormVisibleed = false;
                        this.init();
                    }
                )
            },
            addfavorite(){this.dialogFormVisibleed1=true},
            addnew(form){ //添加新收藏
                if(this.form.wname==="")
                    this.$message({type: 'error', message: '网站名称！'});
                else if(this.form.wurl==="")
                    this.$message({type: 'error', message: '网站地址不能为空！'});
                else if(this.form.type==="")
                    this.$message({type: 'error', message: '请设置权限！'});
                else{
                    this.$http.post(main.url+"/favorite/add",
                        {
                            'uid': localStorage.getItem('id'),
                            'wname': this.form.wname,
                            'wurl': this.form.wurl,
                            'type': this.form.type
                        },
                        {
                            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                            emulateJSON: true
                        }).then(
                        success => {
                            this.$message({type: 'success', message: '添加成功'});
                            this.form = {
                                id: '',
                                wname:'',
                                wurl:'',
                                type:''
                            };
                            this.init();
                        }
                    );
                    this.dialogFormVisibleed1 = false;
                }
            },
            del_fav(row){ //删除收藏记录
                this.$confirm('请确认是否要删除该收藏记录！', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.$http.post(main.url+"/favorite/del",
                        {'id': row.id,},
                        {
                            headers: {'Content-Type':'application/x-www-form-urlencoded'},
                            emulateJSON: true
                        }).then(
                        success=> {
                            this.$message({type: 'success', message: '已删除'});
                            this.init();
                        }
                    );
                }).catch(() => {
                    this.$message({type: 'info', message: '已取消'});
                });
            },
        }
    }
</script>
