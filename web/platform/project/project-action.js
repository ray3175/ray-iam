import "../../utils/sweetalert/sweetalert-dev.js";
import { postProject } from "../../api/project/project.js";


var addProject = {
    template: '<div class="col-sm-2"><button type="button" class="btn btn-primary" data-toggle="modal" data-target="#eject-layout">添加项目</button><div id="eject-layout" class="modal fade" tabindex="-1" role="dialog" aria-hidden="true"><div class="modal-dialog" role="document"></div><div class="modal-content"><div class="modal-header"><h5 class="modal-title">添加项目</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body"><div class="container-fluid"><div class="row"><div class="col-sm-4"><label>项目名称：</label></div><div class="col-sm-8"><input v-model="name" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>项目域名：</label></div><div class="col-sm-8"><input v-model="domain" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>登入地址：</label></div><div class="col-sm-8"><input v-model="login_url" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>登出地址：</label></div><div class="col-sm-8"><input v-model="logout_url" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>授权码：</label></div><div class="col-sm-8"><input v-model="auth_code" type="text" class="form-control" placeholder="..."></div></div></div></div><div class="modal-footer"><button @click="confirmClick()" type="button" class="btn btn-outline-success">确定</button><button type="button" class="btn btn-outline-danger" data-dismiss="modal">取消</button></div></div></div></div>',
    data() {
        return {
            name: null,
            domain: null,
            login_url: null,
            logout_url: null,
            auth_code: null
        }
    },
    methods: {
        confirmClick() {
            if (this.name && this.domain) {
                $("#eject-layout").modal("hide");
                let _this = this;
                postProject(this.name, this.domain, this.login_url, this.logout_url, this.auth_code, function (rsp) {
                    if (rsp.data.code === 200) {
                        _this.name = null;
                        _this.domain = null;
                        _this.login_url = null;
                        _this.logout_url = null;
                        _this.auth_code = null;
                        _this.$parent.getTableData();
                    }
                    _this.$parent.addMessage(rsp.data.msg, rsp.data.code === 200 ? "success" : "danger");
                });
            }
            else {
                sweetAlert("项目名称、项目域名不允许为空！")
            }
        }
    }
};

var searchProject = {
    template: '<div class="col-sm-3 offset-7"><div class="input-group"><input v-model="searchValue" @input="searchAction()" class="form-control" type="text" placeholder="请输入查询内容。。。"></div></div>',
    data() {
        return {
            searchValue: null,
            searchActionTimer: null
        };
    },
    methods: {
        searchAction() {
            let _this = this;
            clearTimeout(this.searchActionTimer);
            this.searchActionTimer = setTimeout(function () {
                _this.$parent.getTableData();
            }, 1000);
        }
    }
};


export { addProject, searchProject };
