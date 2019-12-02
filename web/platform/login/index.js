import { formLogin } from "../../component/form/login.js";


var login = new Vue({
    el: "#login",
    components: {
        "form-login": formLogin
    },
    data() {
        return {
            loginSuccessUrl: "../index.html"
        };
    }
});


