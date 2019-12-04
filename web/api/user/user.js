const getUser = function (offset, limit, reverse, account, callback=null) {
    axios.get("/user/", {
        params: {
            offset: offset,
            limit: limit,
            reverse: reverse,
            account: account
        }
    }).then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    })
};

const postUser = function (account, password, callback=null) {
    axios.post("/user/", {
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

const putUser = function (id, account, password, callback=null) {
    axios.put("/user/" + id, {
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

const deleteUser = function (id, callback=null) {
    axios.delete("/user/" + id).then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    });
};

const logicDeleteUser = function (id, callback=null) {
    axios.put("/user/logic/delete/" + id).then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    });
};

const logicRestoreUser = function (id, callback=null) {
    axios.put("/user/logic/restore/" + id).then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    });
};


export { getUser, postUser, putUser, deleteUser, logicDeleteUser, logicRestoreUser };

