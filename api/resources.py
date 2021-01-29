import json
from rackio.api import RackioResource
from rackio import Rackio

machine_name = "SmartHome"
app = Rackio()


@app.define_route('/api/on')
class OnResource(RackioResource):

    def on_post(self, request, response):

        machine = app.get_machine(machine_name)
        machine.idle_to_run()


@app.define_route('/api/off')
class OffResource(RackioResource):

    def on_post(self, request, response):

        machine = app.get_machine(machine_name)
        machine.run_to_idle()


@app.define_route('/api/settings')
class OffResource(RackioResource):

    def on_get(self, request, response):

        engine = self.tag_engine

        doc = {
            'desired_temp': engine.read_tag("SET_TEMP"),
            'on_1': engine.read_tag("ON_1"),
            'off_1': engine.read_tag("OFF_1"),
            'on_2': engine.read_tag("ON_2"),
            'off_2': engine.read_tag("OFF_2")
        }

        response.body = json.dumps(doc)

    def on_post(self, request, response):

        desired_temp = request.media.get('desired_temp')
        on_1 = request.media.get('on_1')
        off_1 = request.media.get('off_1')
        on_2 = request.media.get('on_2')
        off_2 = request.media.get('off_2')

        engine = self.tag_engine

        engine.write_tag("SET_TEMP", desired_temp)
        engine.write_tag("ON_1", on_1)
        engine.write_tag("OFF_1", off_1)
        engine.write_tag("ON_2", on_2)
        engine.write_tag("OFF_2", off_2)


@app.define_route('/api/state')
class TempResource(RackioResource):

    def on_get(self, request, response):

        machine = app.get_machine(machine_name)
        engine = self.tag_engine

        doc = {
            'temp': engine.read_tag("TEMPERATURE"),
            'desired_temp': engine.read_tag("SET_TEMP"),
            'on': machine.check_state()
            }

        print(doc)

        response.body = json.dumps(doc)
    