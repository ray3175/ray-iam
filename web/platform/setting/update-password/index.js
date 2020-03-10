import { navBar } from "../../../component/navbar/navbar.js";
import { updatePassword } from "./update-password.js";


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

var main = new Vue({
    el: "#main",
    components: {
        "update-password": updatePassword
    }
});


