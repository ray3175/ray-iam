const postProject = function (name, domain, logout_url, license_key, callback=null) {
    axios.post("/project", {
        name: name,
        domain: domain,
        logout_url: logout_url,
        license_key: license_key
    }).then(function (rsp) {
        if (callback) {
            callback(rsp);
        }
        else {
            return rsp;
        }
    });
};


export { postProject };

