def route(page):
    def wrap(func):
        print(f'chamar a pagina {page}')
        func()
    return wrap



@route("/index")
def index( ):
    print("This is how web pages are made in Flask")
