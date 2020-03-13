from injector import singleton, Module, Injector, provider

class Api:
    def fetch_remote_data(self):
        print("Api Called")
        return 42


class BussinessLogic:
    def __init__(self, api: Api):
        self.api = api

    def do_stuff(self):
        api_result = self.api.fetch_remote_data()
        print(f"the api returned a result : {api_result}")


class AppModule(Module):
    @singleton
    @provider
    def provide_bussiness_logic(self, api: Api) -> BussinessLogic:
        return BussinessLogic(api=api)

    @singleton
    @provider
    def provide_api(self) -> Api:
        return Api()


class TestApi(Api):
    def fetch_remote_data(self):
        print('demo api called')
        return 24


class TestAppModule(Module):
    @singleton
    @provider
    def provide_app(self) -> Api:
        return TestApi()


if __name__ == '__main__':
    real_injector = Injector(AppModule())
    test_injector = Injector([AppModule(), TestAppModule()])

    real_logic = real_injector.get(BussinessLogic)
    real_logic.do_stuff()

    test_logic = test_injector.get(BussinessLogic)
    test_logic.do_stuff()
