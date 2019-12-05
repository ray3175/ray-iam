import "../../utils/sweetalert/sweetalert-dev.js";
import { postLogin } from "../../api/default/login.js";


var formLogin = {
    template: '<div class="form-login"><h1 class="form-login-title">Ray-Iam</h1><div class="form-login-input"><input v-model="account" class="form-login-input_input" type="text" autocomplete="off" placeholder="用户名。。。"></div><div class="form-login-input"><input v-model="password" @keydown.enter="loginClick()" class="form-login-input_input" type="password" autocomplete="off" placeholder="密码。。。"></div><button @click="loginClick()" class="form-login-button">登录</button></div>',
    props: {
        loginSuccessUrl: {
            type: String,
            default: ""
        }
    },
    data() {
        return {
            account: null,
            password: null
        };
    },
    methods: {
        loginClick(callback=this.loginCallback) {
            if (this.account && this.password) {
                postLogin(this.account, this.password, callback);
            }
            else {
                sweetAlert("请输入用户名密码！");
            }
        },
        loginCallback(rsp) {
            if (rsp.data.code === 200) {
                window.location.assign(this.loginSuccessUrl);
            }
            else {
                sweetAlert(rsp.data.msg);
            }
        }
    }
};


export { formLogin };
