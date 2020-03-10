const getAdministratorWithSelf = function (callback=null) {
    axios.get("/administrator/update_password_with_self").then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    })
};

const putAdministratorWithSelf = function (password, callback=null) {
    axios.put("/administrator/update_password_with_self", {
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


export { getAdministratorWithSelf, putAdministratorWithSelf };
