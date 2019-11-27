import { navBar } from "../../component/navbar/navbar.js";
import { message } from "../../component/message/message.js";
import { addProject } from "./project.js";


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
        "add-project": addProject
    },
    methods: {
        addMessage(text, type) {
            msg.addMessage(text, type);
        }
    }
});

