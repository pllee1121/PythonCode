from wsgiref.simple_server import make_server


def pllee(req):
    f = open('PythonWeb/pllee.html', 'rb')
    data = f.read()
    return data


def lg(req):
    f = open('PythonWeb/lg.html', 'rb')
    data = f.read()
    return data


def router():
    url_patterns = [
        ('/pllee', pllee),
        ('/lg', lg),
    ]
    return url_patterns


def Application(environ, start_response):

    print('path', environ['PATH_INFO'])
    path = environ['PATH_INFO']
    start_response('200 ok', [('Content-Type', 'text/html') ])

    items = router()
    func = None
    for url in items:
        if url[0] == path:
            func = url[1]
            break
    if func:
        return [func(environ)]
    else:
        return [b'<h1>not found</h1>']


httpd = make_server('localhost', 8080, Application)
print('Serving HTTP on port 8080...')
httpd.serve_forever()
