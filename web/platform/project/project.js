import { addProject, searchProject, updateProject, destroyProject } from "./project-action.js";
import { table } from "./table.js";
import { pageButtonGroup } from "../../component/page-button-group/page-button-group.js";
import { getProject } from "../../api/project/project.js";


var project = {
    template: '<div class="container"><div class="row align-items-center"><add-project></add-project><update-project ref="updateProjectObj" :project="project"></update-project><destroy-project ref="destroyProjectObj" :project="project"></destroy-project><search-project ref="searchProjectObj"></search-project></div><div class="row"><div class="table-div"><table-project :tableData="tableData"></table-project></div></div><div class="row"><div class="page-div"><page-project :page="page" :rows="rows" :pageNow="pageNow" :dataLength="data.length"></page-project></div></div></div>',
    components: {
        "search-project": searchProject,
        "add-project": addProject,
        "update-project": updateProject,
        "destroy-project": destroyProject,
        "table-project": table,
        "page-project": pageButtonGroup
    },
    data() {
        return {
            page: 1,
            rows: 10,
            pageNow: 1,
            reverse: true,
            data: [],
            project: {}
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
            getProject((this.page - 1) * (this.rows * 10), this.rows * 10, this.reverse, this.$refs.searchProjectObj && this.$refs.searchProjectObj.searchValue ? "%" + this.$refs.searchProjectObj.searchValue + "%" : null, true, function (rsp) {
                if (rsp.data.code === 200) {
                    _this.data = rsp.data.data;
                }
            });
        },
        updateProject(project) {
            this.project = project;
            this.$refs.updateProjectObj.ejectLayout();
        },
        destroyProject(project) {
            this.project = project;
            this.$refs.destroyProjectObj.ejectLayout();
        }
    }
};


export { project };
