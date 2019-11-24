import { formLogin } from "../../component/form/login.js";


var login = new Vue({
    el: "#login",
    mixins: [ formLogin ],
    data() {
        return {
            login_success_url: "../index.html"
        }
    }
});


