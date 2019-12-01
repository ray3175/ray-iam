import "../../lib/bootstrap/js/bootstrap.min.js";


var pageButtonGroup = {
    template: '<div class="btn-toolbar" role="toolbar"><div class="btn-group" role="group"><button @click="prePageClick()" :disabled="prePageDisabled" type="button" class="btn btn-secondary"><</button></div><div class="btn-group" role="group"><button v-for="pageNumber in pageRange" @click="numberPageClick(pageNumber)" :disabled="pageNumberDisabled(pageNumber)" type="button" class="btn btn-secondary">{{ pageNumber }}</button></div><div class="btn-group" role="group"><button @click="nextPageClick()" :disabled="nextPageDisabled" type="button" class="btn btn-secondary">></button></div><div class="input-group"><input v-model="pageNowShow" @input="pageGoTo()" class="page-goto form-control text-center" type="text" autocomplete="off" placeholder="..."></div></div>',
    props: ["page", "rows", "pageNow", "dataLength"],
    data() {
        return {
            pageNowShow: 1,
            pageGoToTimer: null
        };
    },
    computed: {
        pageRange() {
            let rangList = [];
            let dataLength = Math.ceil(this.dataLength / this.rows);
            for (let i=1; i <= dataLength; i++) {
                rangList.push((this.page - 1) * this.rows + i);
            }
            return rangList;
        },
        prePageDisabled() {
            return this.page <= 1;
        },
        nextPageDisabled() {
            return this.dataLength < 10 * this.rows;
        }
    },
    methods: {
        pageNumberDisabled(pageNumber) {
            return pageNumber === this.pageNow;
        },
        prePageClick() {
            if (! this.prePageDisabled) {
                this.$parent.page--;
                this.pageNowShow = this.$parent.pageNow = this.$parent.pageNow - 10;
            }
        },
        nextPageClick() {
            this.$parent.page++;
            this.pageNowShow = this.$parent.pageNow = this.$parent.pageNow + 10;
        },
        numberPageClick(pageNumber) {
            this.pageNowShow = this.$parent.pageNow = pageNumber;
        },
        pageGoTo() {
            let _this = this;
            clearTimeout(this.pageGoToTimer);
            this.pageGoToTimer = setTimeout(function () {
                _this.$parent.pageNow = _this.pageNowShow = Number(_this.pageNowShow);
                _this.$parent.page = Math.ceil(_this.pageNowShow / 10);
            }, 500);
        }
    }
};


export { pageButtonGroup };
