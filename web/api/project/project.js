const getProject = function (offset, limit, reverse, name, condition_like, callback=null) {
    axios.get("/project/", {
        params: {
            offset: offset,
            limit: limit,
            reverse: reverse,
            name: name,
            condition_like: condition_like
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

const postProject = function (name, domain, login_url, logout_url, auth_code, callback=null) {
    axios.post("/project/", {
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

const putProject = function (id, name, domain, login_url, logout_url, auth_code, callback=null) {
    axios.put("/project/" + id, {
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

const deleteProject = function (id, callback=null) {
    axios.delete("/project/" + id).then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    });
};


export { getProject, postProject, putProject, deleteProject };

