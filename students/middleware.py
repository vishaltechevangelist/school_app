import time
from django.http import HttpResponse

def CustomFunctionMiddleware(get_response):
    # code will execute when the web server run
    print("This will executed once web server started")
    def middleware(request):
        print("execute beforee view")
        response = get_response(request)
        print("execute after view")
        return response
    return middleware


def simple_logger_middleware(get_response):
    '''Logs the request path'''
    def middleware(request):
        print(f"[Middleware] request path: {request.path}")
        response = get_response(request)
        return response
    return middleware

def timing_middleware(get_response):
    '''Log the request timimg'''
    def middleware(request):
        start = time.time()
        response = get_response(request)
        duration = time.time() - start
        print(f"[Middleware] {request.path} took {duration: .2f}s")
        return response
    return middleware

class CustomTimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        # print(self.get_response)
        duration = time.time() - start_time
        print(f"[Middleware] {request.path} took {duration:.2f} seconds")
        return response
    
class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("execute beforee view")
        response = self.get_response(request)
        print("__call__")
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("process_view")
        # print(view_func.__name__)
        # print(view_kwargs)
        return None
    
    def process_exception(self, request, exception):
        print('process_exception')
        print(exception)
        return None
    
    def process_template_response(self, request, response):
        print("process_template_response")
        return response