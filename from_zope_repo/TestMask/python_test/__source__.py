def ret_method():
    return context.ret_method
    

def do_callback(callback):
    callback()


res = context.actual_datetime_get_q

test = container.called_method
do_callback(test)

test2 = ret_method()
test2()

assert len(res) == 1
return '{testparam}! HELLO WORLD, {username}! It\'s {now}'.format(
    testparam=testparam,
    now=res[0].actual_datetime,
    username=res[0].username
    
)
