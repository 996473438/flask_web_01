from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return "<h1>test</h1>"


@main.route('/test', methods=['GET', 'POST'])
def test():
    return "test, this is my test"
