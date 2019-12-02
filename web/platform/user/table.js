import "../../lib/bootstrap/js/bootstrap.min.js";


var table = {
    template: '<table class="table table-hover table-bordered"><thead><tr><th>项目名称</th><th>项目域名</th><th>登入地址</th><th>登出地址</th><th>授权码</th><th>状态</th><th>操作</th></tr></thead><tbody><tr v-for="data in tableDataShow"><td class="cursor-pointer">{{ data.name }}</td><td>{{ data.domain }}</td><td class="text-align-left">{{ data.login_url }}</td><td class="text-align-left">{{ data.logout_url }}</td><td>{{ data.auth_code }}</td><td>{{ data.activeShow }}</td><td><div><button @click="updateClick(data)">修改</button>&nbsp;&nbsp;<button @click="destroyClick(data)">删除</button></div></td></tr></tbody></table>',
    props: ["tableData"],
    computed: {
        tableDataShow() {
            for (let i in this.tableData) {
                this.tableData[i].activeShow = this.tableData[i].active ? "√" : "×";
            }
            return this.tableData;
        }
    },
    methods: {
        updateClick(obj) {
            this.$parent.updateUser(obj);
        },
        destroyClick(obj) {
            this.$parent.destroyUser(obj);
        }
    }
};


export { table };
