from flask import redirect, url_for


def redirect_to_endpoint(endpoint):
    return redirect(url_for(endpoint))


def redirect_to_source(source_path):
    return redirect(url_for("static", filename=source_path))

