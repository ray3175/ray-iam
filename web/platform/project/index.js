import { navBar } from "../../component/navbar/navbar.js";
import { message } from "../../component/message/message.js"


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
    mixins: [ message ],
});


var main = new Vue({
    el: "#main",
    methods: {
        demo() {
            msg.addMessage('草泥马', 'success');
        }
    }
});

