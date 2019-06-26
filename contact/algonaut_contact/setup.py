from .api.v1.routes import routes
from .tasks import send

config = {
    'providers' :{},
    'api' : [{
        'routes' : routes,
        'version' : 'v1',
    }],
    'tasks' : [send],
}
