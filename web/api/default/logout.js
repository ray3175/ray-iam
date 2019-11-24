const postLogout = function (callback=null) {
    axios.post("/logout").then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    });
};


export { postLogout };

