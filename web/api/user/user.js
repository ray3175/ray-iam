const getUser = function (offset, limit, reverse, name, callback=null) {
    axios.get("/user/", {
        params: {
            offset: offset,
            limit: limit,
            reverse: reverse,
            name: name
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

const postUser = function (name, domain, login_url, logout_url, auth_code, callback=null) {
    axios.post("/user/", {
        name: name,
        domain: domain,
        login_url: login_url,
        logout_url: logout_url,
        auth_code: auth_code
    }).then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    });
};

const putUser = function (id, name, domain, login_url, logout_url, auth_code, callback=null) {
    axios.put("/user/" + id, {
        name: name,
        domain: domain,
        login_url: login_url,
        logout_url: logout_url,
        auth_code: auth_code
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


export { getUser, postUser, putUser, deleteUser };

