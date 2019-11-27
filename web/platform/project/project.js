import "../../utils/sweetalert/sweetalert-dev.js";
import { postProject } from "../../api/project/project.js";


var addProject = {
    template: '<div><button type="button" class="btn btn-primary" data-toggle="modal" data-target="#eject-layout">添加项目</button><div id="eject-layout" class="modal fade" tabindex="-1" role="dialog" aria-hidden="true"><div class="modal-dialog" role="document"></div><div class="modal-content"><div class="modal-header"><h5 class="modal-title">添加项目</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body"><div class="container-fluid"><div class="row"><div class="col-sm-4"><label>项目名称：</label></div><div class="col-sm-8"><input v-model="name" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>项目域名：</label></div><div class="col-sm-8"><input v-model="domain" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>注销地址：</label></div><div class="col-sm-8"><input v-model="logout_url" type="text" class="form-control" placeholder="..."></div></div><div class="row"><div class="col-sm-4"><label>授权码：</label></div><div class="col-sm-8"><input v-model="license_key" type="text" class="form-control" placeholder="..."></div></div></div></div><div class="modal-footer"><button @click="confirmClick" type="button" class="btn btn-outline-success">确定</button><button type="button" class="btn btn-outline-danger" data-dismiss="modal">取消</button></div></div></div></div>',
    data() {
        return {
            name: null,
            domain: null,
            logout_url: null,
            license_key: null
        }
    },
    methods: {
        confirmClick() {
            if (this.name && this.domain) {
                $("#eject-layout").modal("hide");
                postProject(this.name, this.domain, this.logout_url, this.license_key, this.callback);
            }
            else {
                sweetAlert("项目名称、项目域名不允许为空！")
            }
        },
        callback(rsp) {
            if (rsp.data.code === 200) {
                this.name = null;
                this.domain = null;
                this.logout_url = null;
                this.license_key = null;
            }
            this.$parent.addMessage(rsp.data.msg, rsp.data.code === 200 ? "success" : "danger");
        }
    }
};


export { addProject };
