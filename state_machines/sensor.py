import json
import requests

from rackio import Rackio, RackioStateMachine, State, GroupBinding

app = Rackio()

@app.define_machine('SmartHome', 20)
class Sensor(RackioStateMachine):

    # State Definitions
    reading = State('read', initial=True)

    # bindings

    acquisition = GroupBinding('acquisition', direction="write")

    def while_reading(self):

        req = requests.get('http://192.168.1.88/')
        data = json.loads(req.text)

        self.acquisition.TEMPERATURE = float(data['temperature'])
        self.acquisition.PRESSURE = float(data['pressure'])
        self.acquisition.HUMIDITY = float(data["humidity"])
        