import { randomNumber } from "../../utils/random/random.js";


var message = {
    components: {
        message: {
            template: '<div :id="id"></div>',
            data() {
                return {
                    id: "message-" + randomNumber()
                }
            },
            methods: {
                addMessage(text, type="light", time=10) {
                    // type： ["primary", "secondary", "success", "danger", "warning", "info", "light", "dark"]
                    let id = "temp-message-" + randomNumber();
                    let html = '<div id="' + id + '"class="alert alert-' + type + ' alert-dismissible fade show" role="alert">' + text + '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>';
                    document.getElementById(this.id).innerHTML += html;
                    setTimeout(function () {
                        $("#" + id).alert("close");
                    }, 1000 * time);
                }
            }
        }
    },
    methods: {
        addMessage(text, type="light", time=10) {
            // 组件引用 <message ref="message"></message>
            this.$refs.message.addMessage(text, type, time);
        },
        addMessageSuccess(text, time=10) {
            this.addMessage(text, "success", time);
        },
        addMessageFail(text, time=10) {
            this.addMessage(text, "danger", time);
        },
        addMessageWarning(text, time=10) {
            this.addMessage(text, "warning", time);
        },
        addMessageInfo(text, time=10) {
            this.addMessage(text, "info", time);
        }
    }
};


export { message };
