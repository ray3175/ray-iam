import { addUser, searchUser, updateUser, destroyUser, logicDeleteOrRestoreUser } from "./user-action.js";
import { table } from "./table.js"
import { pageButtonGroup } from "../../component/page-button-group/page-button-group.js"
import { getUser } from "../../api/user/user.js";


var user = {
    template: '<div class="container"><div class="row align-items-center"><add-user></add-user><update-user ref="updateUserObj" :user="user"></update-user><logic-delete-or-restore-user ref="logicDeleteOrRestoreUserObj" :user="user"></logic-delete-or-restore-user><destroy-user ref="destroyUserObj" :user="user"></destroy-user><search-user ref="searchUserObj"></search-user></div><div class="row"><div class="table-div"><table-user :tableData="tableData"></table-user></div></div><div class="row"><div class="page-div"><page-user :page="page" :rows="rows" :pageNow="pageNow" :dataLength="data.length"></page-user></div></div></div>',
    components: {
        "search-user": searchUser,
        "add-user": addUser,
        "update-user": updateUser,
        "destroy-user": destroyUser,
        "table-user": table,
        "page-user": pageButtonGroup,
        "logic-delete-or-restore-user": logicDeleteOrRestoreUser
    },
    data() {
        return {
            page: 1,
            rows: 10,
            pageNow: 1,
            reverse: true,
            data: [],
            user: {}
        };
    },
    created() {
        this.getTableData();
    },
    computed: {
        tableData() {
            let sliceNow = this.pageNow % 10;
            if (! sliceNow) {
                sliceNow = 10
            }
            return this.data.slice((sliceNow - 1) * this.rows, sliceNow * this.rows);
        }
    },
    watch: {
        page: function () {
            this.getTableData();
        }
    },
    methods: {
        addMessage(text, type) {
            this.$parent.addMessage(text, type);
        },
        getTableData() {
            let _this = this;
            getUser((this.page - 1) * (this.rows * 10), this.rows * 10, this.reverse, this.$refs.searchUserObj && this.$refs.searchUserObj.searchValue ? "%" + this.$refs.searchUserObj.searchValue + "%" : null, true, function (rsp) {
                if (rsp.data.code === 200 || rsp.data.code === 400) {
                    _this.data = rsp.data.data;
                }
            });
        },
        updateUser(user) {
            this.user = user;
            this.$refs.updateUserObj.ejectLayout();
        },
        logicDeleteOrRestoreUser(user) {
            this.user = user;
            this.$refs.logicDeleteOrRestoreUserObj.ejectLayout();
        },
        destroyUser(user) {
            this.user = user;
            this.$refs.destroyUserObj.ejectLayout();
        }
    }
};


export { user };
