import "../../lib/bootstrap/js/bootstrap.min.js";
import "../../utils/sweetalert/sweetalert-dev.js";


var table = {
    template: '<table class="table table-hover table-bordered"><thead><tr><th>ID</th><th>账号</th><th>密码</th><th>身份证</th><th>姓名</th><th>性别</th><th>出生日期</th><th>出生地</th><th>籍贯</th><th>名族</th><th>其他</th><th>注册时间</th><th>操作</th></tr></thead><tbody><tr v-for="data in tableDataShow"><td class="cursor-pointer">{{ data.id }}</td><td>{{ data.account }}</td><td>{{ data.password }}</td><td>{{ data.person.id_card }}</td><td>{{ data.person.name }}</td><td>{{ data.person.sex }}</td><td>{{ data.person.birth_date }}</td><td class="text-align-left">{{ data.person.birth_place }}</td><td>{{ data.person.native_place }}</td><td>{{ data.person.nationality }}</td><td><div><button @click="phoneClick(data)">手机号</button>&nbsp;&nbsp;<button @click="mailClick(data)">邮箱</button></div></td><td>{{ data.register_time }}</td><td><div><button @click="updateClick(data)">修改</button>&nbsp;&nbsp;<button @click="deleteOrRestoreClick(data)">{{ data.deleteOrRestore }}</button>&nbsp;&nbsp;<button @click="destroyClick(data)">彻底删除</button></div></td></tr></tbody></table>',
    props: ["tableData"],
    computed: {
        tableDataShow() {
            for (let i in this.tableData) {
                if (! this.tableData[i].person) {
                    this.tableData[i].person = {};
                }
                this.tableData[i].deleteOrRestore = this.tableData[i].xy ? "删除" : "恢复";
            }
            return this.tableData;
        }
    },
    methods: {
        phoneClick(obj) {
            if (obj.person.phone && obj.person.phone.length) {
                sweetAlert("该功能暂未开放！");
            }
            else {
                sweetAlert("该账号未绑定手机号！");
            }
        },
        mailClick(obj) {
            if (obj.person.mail && obj.person.mail.length) {
                sweetAlert("该功能暂未开放！");
            }
            else {
                sweetAlert("该账号未绑定邮箱！");
            }
        },
        updateClick(obj) {
            this.$parent.updateUser(obj);
        },
        deleteOrRestoreClick(obj) {
            this.$parent.logicDeleteOrRestoreUser(obj);
        },
        destroyClick(obj) {
            this.$parent.destroyUser(obj);
        }
    }
};


export { table };
