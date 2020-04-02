from flask import request

@app.errorhandler(500)
def server_error(e):

    email_admin(message="Server error", url=request.url, error=e)

    app.logger.error(f"Server error: {request.url}")

    return render_template("error_handlers/500.html"), 500