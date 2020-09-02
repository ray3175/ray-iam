import "../../../utils/sweetalert/sweetalert-dev.js";
import { getAdministratorWithSelf, putAdministratorWithSelf } from "../../../api/administrator/administrator.js";


var updatePassword = {
    template: '<div class="layout"><div class="layout-main"><div class="self-layout"><div class="self-title">个人信息</div><div class="self-account">{{ account }}</div><div class="self-password"><input v-model="passwordOld" class="self-input" type="password" placeholder="旧密码。。。"></div><div class="self-password"><input v-model="password" class="self-input" type="password" placeholder="新密码。。。"></div><div class="self-password"><input v-model="passwordConfirm" class="self-input" type="password" placeholder="确认新密码。。。"></div><button @click="confirmClick()" class="self-confirm self-button">确认更新</button></div></div></div>',
    data() {
        return {
            account: null,
            passwordNow: null,
            passwordOld: null,
            password: null,
            passwordConfirm: null
        }
    },
    mounted() {
        this.initSelfInfo();
    },
    methods: {
        initSelfInfo() {
            getAdministratorWithSelf((rsp) => {
                if (rsp.data.code === 200) {
                    this.account = rsp.data.data.account;
                    this.passwordNow = rsp.data.data.password;
                }
            });
        },
        confirmClick() {
            if (this.passwordNow && this.password && this.passwordConfirm) {
                if (this.password === this.passwordConfirm) {
                    if (this.passwordNow === this.passwordOld) {
                        putAdministratorWithSelf(this.password, (rsp) => {
                            sweetAlert(rsp.data.msg);
                        });
                    }
                    else {
                        sweetAlert("旧密码验证失败！");
                    }
                }
                else {
                    sweetAlert("两次输入的新密码不一致！");
                }
            }
            else {
                sweetAlert("密码不能为空！");
            }
        }
    }
};


export { updatePassword };
