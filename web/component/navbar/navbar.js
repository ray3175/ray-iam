import "../../lib/bootstrap/js/bootstrap.min.js";
import "../../utils/sweetalert/sweetalert-dev.js";
import { postLogout } from "../../api/default/logout.js";


var navBar = {
    props: ["router"],
    template: '<nav class="navbar navbar-expand-lg navbar-light"><a :href="administrator.root.href" class="navbar-brand">主页</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarContent"><ul class="navbar-nav mr-auto"><li class="nav-item"><a :href="administrator.project.href" :class="{ disabled: administrator.project.disabled }" class="nav-link">项目</a></li><li class="nav-item"><a :href="administrator.user.href" :class="{ disabled: administrator.user.disabled }" class="nav-link">用户</a></li><li class="nav-item"><a :href="administrator.dashboard.href" :class="{ disabled: administrator.dashboard.disabled }" class="nav-link">看板</a></li><li class="nav-item"><a :href="administrator.auth.href" :class="{ disabled: administrator.auth.disabled }" class="nav-link disabled">权限</a></li><li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="javascript:void(0)" id="settingDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">设置</a><div class="dropdown-menu" aria-labelledby="settingDropdown"><a :href="administrator.setting.updatePassword.href" :class="{ disabled: administrator.setting.updatePassword.disabled }" class="dropdown-item">修改密码</a><div class="dropdown-divider"></div><a @click="logoutClick()" class="dropdown-item" href="javascript:void(0)">登出</a></div></li></ul></div></nav>',
    data() {
        return {
            administrator: {
                root: {
                    href: this.router + "/index.html",
                    disabled: false
                },
                project: {
                    href: this.router + "/project/index.html",
                    disabled: false
                },
                user: {
                    href: this.router + "/user/index.html",
                    disabled: false
                },
                dashboard: {
                    href: this.router + "/dashboard/index.html",
                    disabled: false
                },
                auth: {
                    href: this.router + "/auth/index.html",
                    disabled: true
                },
                setting: {
                    updatePassword: {
                        href: this.router + "/setting/update-password/index.html",
                        disabled: false
                    }
                }
            },
            logout_success_url: this.router + "/login/index.html"
        };
    },
    methods: {
        logoutClick(callback=this.logoutCallback) {
            postLogout(callback);
        },
        logoutCallback(rsp) {
            if (rsp.data.code === 200) {
                window.location.assign(this.logout_success_url);
            }
            else {
                sweetAlert(rsp.data.msg);
            }
        }
    }
};


export { navBar };
