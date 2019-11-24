const postLogin = function (user, password, callback=null) {
    axios.post("/login", {
        user: user,
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

