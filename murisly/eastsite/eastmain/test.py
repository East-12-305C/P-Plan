#test.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    #return ["Hello World"] # python2
    return [b"just a test"] # python3
