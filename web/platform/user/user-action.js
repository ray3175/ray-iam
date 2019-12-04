import "../../utils/sweetalert/sweetalert-dev.js";
import { postUser, putUser, deleteUser, logicDeleteUser, logicRestoreUser } from "../../api/user/user.js";


var searchUser = {
    template: '<div class="col-sm-3 offset-7"><div class="input-group"><input v-model="searchValue" @input="searchAction()" class="form-control" type="text" placeholder="请输入要查询的账号。。。"></div></div>',
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

var addUser = {
    template: '<div class="col-sm-2"><button type="button" class="btn btn-primary" data-toggle="modal" data-target="#eject-layout">添加用户</button><div id="eject-layout" class="modal fade" tabindex="-1" role="dialog" aria-hidden="true"><div class="modal-dialog" role="document"></div><div class="modal-content"><div class="modal-header"><h5 class="modal-title">添加用户</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body"><div class="container-fluid"><div class="row"><div class="col-sm-4"><label>账号：</label></div><div class="col-sm-8"><input v-model="account" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>密码：</label></div><div class="col-sm-8"><input v-model="password" type="text" class="form-control" placeholder="..."></div></div></div></div><div class="modal-footer"><button @click="confirmClick()" type="button" class="btn btn-outline-success">确定</button><button type="button" class="btn btn-outline-danger" data-dismiss="modal">取消</button></div></div></div></div>',
    data() {
        return {
            account: null,
            password: null
        }
    },
    methods: {
        confirmClick() {
            if (this.account && this.password) {
                $("#eject-layout").modal("hide");
                let _this = this;
                postUser(this.account, this.password, function (rsp) {
                    if (rsp.data.code === 200) {
                        _this.account = null;
                        _this.password = null;
                        _this.$parent.getTableData();
                    }
                    _this.$parent.addMessage(rsp.data.msg, rsp.data.code === 200 ? "success" : "danger");
                });
            }
            else {
                sweetAlert("账号、密码不允许为空！");
            }
        }
    }
};

var updateUser = {
    template: '<div id="eject-layout-update" class="modal fade" tabindex="-1" role="dialog" aria-hidden="true"><div class="modal-dialog" role="document"></div><div class="modal-content"><div class="modal-header"><h5 class="modal-title">修改用户 - {{ user.id }}</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body"><div class="container-fluid"><div class="row"><div class="col-sm-4"><label>账号：</label></div><div class="col-sm-8"><input v-model="user.account" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>密码：</label></div><div class="col-sm-8"><input v-model="user.password" type="text" class="form-control" placeholder="..."></div></div></div></div><div class="modal-footer"><button @click="confirmClick()" type="button" class="btn btn-outline-success">确定</button><button type="button" class="btn btn-outline-danger" data-dismiss="modal">取消</button></div></div></div>',
    props: ["user"],
    methods: {
        ejectLayout() {
            $('#eject-layout-update').modal('show');
        },
        confirmClick() {
            if (this.user.account && this.user.password) {
                $("#eject-layout-update").modal("hide");
                let _this = this;
                putUser(this.user.id, this.user.account, this.user.password, function (rsp) {
                    if (rsp.data.code === 200) {
                        _this.$parent.getTableData();
                    }
                    _this.$parent.addMessage(rsp.data.msg, rsp.data.code === 200 ? "success" : "danger");
                });
            }
            else {
                sweetAlert("账号、密码不允许为空！")
            }
        }
    }
};

var destroyUser = {
    template: '<div id="eject-layout-destroy" class="modal fade" tabindex="-1" role="dialog" aria-hidden="true"><div class="modal-dialog" role="document"></div><div class="modal-content"><div class="modal-header"><h5 class="modal-title">彻底删除用户 - {{ user.id }}</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body"><div class="container-fluid"><div class="row"><div class="col-sm-4"><label>账号：</label></div><div class="col-sm-8"><input v-model="user.account" :disabled="true" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>密码：</label></div><div class="col-sm-8"><input v-model="user.password" :disabled="true" type="text" class="form-control" placeholder="..."></div></div></div></div><div class="modal-footer"><button @click="confirmClick()" type="button" class="btn btn-outline-success">确定</button><button type="button" class="btn btn-outline-danger" data-dismiss="modal">取消</button></div></div></div>',
    props: ["user"],
    methods: {
        ejectLayout() {
            $('#eject-layout-destroy').modal('show');
        },
        confirmClick() {
            $("#eject-layout-destroy").modal("hide");
            let _this = this;
            deleteUser(this.user.id, function (rsp) {
                if (rsp.data.code === 200) {
                    _this.$parent.getTableData();
                }
                _this.$parent.addMessage(rsp.data.msg, rsp.data.code === 200 ? "success" : "danger");
            });
        }
    }
};

var logicDeleteOrRestoreUser = {
    template: '<div id="eject-layout-logic-delete-or-restore" class="modal fade" tabindex="-1" role="dialog" aria-hidden="true"><div class="modal-dialog" role="document"></div><div class="modal-content"><div class="modal-header"><h5 class="modal-title">{{ title }}用户 - {{ user.id }}</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body"><div class="container-fluid"><div class="row"><div class="col-sm-4"><label>账号：</label></div><div class="col-sm-8"><input v-model="user.account" :disabled="true" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>密码：</label></div><div class="col-sm-8"><input v-model="user.password" :disabled="true" type="text" class="form-control" placeholder="..."></div></div></div></div><div class="modal-footer"><button @click="confirmClick()" type="button" class="btn btn-outline-success">确定</button><button type="button" class="btn btn-outline-danger" data-dismiss="modal">取消</button></div></div></div>',
    props: ["user"],
    computed: {
        title() {
            return this.user.xy ? "删除" : "恢复";
        }
    },
    methods: {
        ejectLayout() {
            $('#eject-layout-logic-delete-or-restore').modal('show');
        },
        confirmClick() {
            $("#eject-layout-logic-delete-or-restore").modal("hide");
            let _this = this;
            if (this.user.xy) {
                logicDeleteUser(this.user.id, function (rsp) {
                    if (rsp.data.code === 200) {
                        _this.$parent.getTableData();
                    }
                    _this.$parent.addMessage(rsp.data.msg, rsp.data.code === 200 ? "success" : "danger");
                });
            }
            else {
                logicRestoreUser(this.user.id, function (rsp) {
                    if (rsp.data.code === 200) {
                        _this.$parent.getTableData();
                    }
                    _this.$parent.addMessage(rsp.data.msg, rsp.data.code === 200 ? "success" : "danger");
                });
            }
        }
    }
};


export { searchUser, addUser, updateUser, destroyUser, logicDeleteOrRestoreUser };
