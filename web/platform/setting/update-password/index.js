import { navBar } from "../../../component/navbar/navbar.js";


var header = new Vue({
    el: "#header",
    components: {
        "nav-bar": navBar
    },
    data () {
        return {
            router: "../.."
        };
    }
});



