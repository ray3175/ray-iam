import { randomNumber } from "../../utils/random/random.js";


var message = {
    methods: {
        addMessage(text, type="light", time=10) {
            let id = "message-" + randomNumber();
            let html = '<div id="' + id + '"class="alert alert-' + type + ' alert-dismissible fade show" role="alert">' + text + '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
            document.getElementById(this.$el.id).innerHTML += html;
            setTimeout(function () {
                $("#" + id).alert("close");
            }, 1000 * time);
        }
    }
};


export { message };
