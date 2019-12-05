const postLogin = function (account, password, callback=null) {
    axios.post("/login", {
        account: account,
        password: password
    }).then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    });
};


export { postLogin };

