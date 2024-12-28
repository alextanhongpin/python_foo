from python_foo import baz

def bar():
    return 'bar'

def bar_baz():
    return bar() + '_' + baz.baz()
