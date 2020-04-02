from flask import request

@app.errorhandler(404)
def page_not_found(e):

    app.logger.info(f"Page not found: {request.url}")

    return render_template("error_handlers/404.html"), 404