from bottle import get, route, request, response, run, post
import Robot

robot = Robot.Robot(0,0)

def handle_padded(handler):
    def decorator(**kwargs):
        r = handler
        try:
            callback = request.query.get('callback')
        except Exception, e:
            callback = None
        if callback is None:
            return r(kwargs)
        else:
            response.content_type = 'text/javascript'
            return "%s(%r);" % (callback, r)
    return decorator


@get('/Robot___init__/<addr>/<left_id>/<right_id>/<left_trim>/<right_trim>/<stop_at_exit>')
@handle_padded
def Robot___init__(kargs):
    r = {'return_value': robot.__init__(int(kargs['addr']), int(kargs['left_id']), int(kargs['right_id']), int(kargs['left_trim']), int(kargs['right_trim']), int(kargs['stop_at_exit']))}
    return r


@get('/Robot__left_speed/<speed>')
@handle_padded
def Robot__left_speed(kargs):
    r = {'return_value': robot._left_speed(int(kargs['speed']))}
    return r


@get('/Robot__right_speed/<speed>')
@handle_padded
def Robot__right_speed(kargs):
    r = {'return_value': robot._right_speed(int(kargs['speed']))}
    return r


@get('/Robot_stop')
@handle_padded
def Robot_stop(kargs):
    r = {'return_value': robot.stop()}
    return r


@get('/Robot_forward/<speed>/<seconds>')
@handle_padded
def Robot_forward(kargs):
    r = {'return_value': robot.forward(int(kargs['speed']), int(kargs['seconds']))}
    return r


@get('/Robot_backward/<speed>/<seconds>')
@handle_padded
def Robot_backward(kargs):
    r = {'return_value': robot.backward(int(kargs['speed']), int(kargs['seconds']))}
    return r


@get('/Robot_right/<speed>/<seconds>')
@handle_padded
def Robot_right(kargs):
    r = {'return_value': robot.right(int(kargs['speed']), int(kargs['seconds']))}
    return r


@get('/Robot_left/<speed>/<seconds>')
@handle_padded
def Robot_left(kargs):
    r = {'return_value': robot.left(int(kargs['speed']), int(kargs['seconds']))}
    return r


@get('/Robot_left_glide/<speed>/<seconds>')
@handle_padded
def Robot_left_glide(kargs):
    r = {'return_value': robot.left_glide(int(kargs['speed']), int(kargs['seconds']))}
    return r


@get('/Robot_right_glide/<speed>/<seconds>')
@handle_padded
def Robot_right_glide(kargs):
    r = {'return_value': robot.right_glide(int(kargs['speed']), int(kargs['seconds']))}
    return r


run(host='0.0.0.0', port=8080, debug=True)
