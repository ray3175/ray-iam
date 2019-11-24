import { postLogin } from "../../api/default/login.js"


var formLogin = {
    data() {
        return {
            login_success_url: "",
            user: null,
            password: null
        };
    },
    methods: {
        loginClick(callback=this.loginCallback) {
            postLogin(this.user, this.password, callback);
        },
        loginCallback(rsp) {
            if (rsp.data.code === 200) {
                window.location.assign(this.login_success_url);
            }
            else {
                sweetAlert(rsp.data.msg);
            }
        }
    }
};


export { formLogin };
