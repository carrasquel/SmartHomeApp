import json
from rackio.api import RackioResource
from rackio import Rackio

app = Rackio()


@app.define_route('/api/on')
class OnResource(RackioResource):

    pass


@app.define_route('/api/off')
class OffResource(RackioResource):

    pass


@app.define_route('/api/settings')
class OffResource(RackioResource):

    pass


@app.define_route('/api/state')
class TempResource(RackioResource):

    pass