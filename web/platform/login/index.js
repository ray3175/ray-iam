import { normal } from "../../component/form/login.js";


var login = new Vue({
    el: "#login",
    components: {
        "Login": {
            props: ["user", "password"],
            template: normal
        }
    },
    data() {
        return {
            user: null,
            password: null
        };
    }
});


