import { navBar } from "../../component/navbar/navbar.js";
import { message } from "../../component/message/message.js";
import { project } from "./project.js";


var header = new Vue({
    el: "#header",
    components: {
        "nav-bar": navBar
    },
    data () {
        return {
            router: ".."
        };
    }
});


var msg = new Vue({
    el: "#msg",
    mixins: [ message ]
});


var main = new Vue({
    el: "#main",
    components: {
        "project": project
    },
    computed: {
        tableData: function () {
            return this.getTableData;
        }
    },
    methods: {
        addMessage(text, type) {
            msg.addMessage(text, type);
        }
    }
});

