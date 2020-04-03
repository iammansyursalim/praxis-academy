from flask.views import View

class MyRequest(View):
    def dispatch_request(self):
        name = request.args.get('name', 'Damyan')
        return 'Hello, %s!' % name

app.add_url_rule(
    '/say-hi', view_func=MyRequest.as_view('my_request')
)

#==================================

from flask.views import View


class MyRequest(View):
    methods = ['POST']

    def dispatch_request(self):
        # request.method == 'POST'
        name = request.form.get('name', 'Damyan')
        return 'Hello, %s!' % name


app.add_url_rule(
    '/say-hi', view_func=MyRequest.as_view('my_request')
)

#=================================

from flask.views import MethodView

class GenericRequest(MethodView):
    def get(self):
        name = request.args.get('name', 'Damyan')
        return 'Hello GET from %s!' % name

    def post(self):
        name = request.form.get('name', 'Damyan')
        return 'Hello POST from %s' % name

app.add_url_rule(
    '/generic_request',
    view_func=GenericRequest.as_view('generic_request')
)