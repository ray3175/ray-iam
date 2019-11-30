const getProject = function (offset, limit, reverse, name, callback=null) {
    axios.get("/project/", {
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


export { getProject, postProject };

