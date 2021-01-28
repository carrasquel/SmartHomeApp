import pigpio

from datetime import datetime
from rackio import Rackio, RackioStateMachine, State, GroupBinding

app = Rackio()

@app.define_machine('SmartHome', 60)
class SmartHome(RackioStateMachine):

    # State Definitions
    starting = State('start', initial=True)
    running = State('on')
    idle = State('off')

    # Transition Definitions
    start_to_idle = starting.to(idle)
    idle_to_run = idle.to(running)
    run_to_idle = running.to(idle)

    run_to_start = running.to(starting)
    idle_to_start = idle.to(starting)

    # bindings

    acquisition = GroupBinding('acquisition')
    control = GroupBinding('control')

    def while_starting(self):

        self.pi = pigpio.pi()

        if self.check_state():
            self.switch_off_relay()

        self.start_to_idle()

    def while_running(self):

        time_check = datetime.strptime(datetime.utcnow().time().strftime('%H:%M'), '%H:%M').time()
        on_1 = self.control.ON_1
        off_1 = self.control.OFF_1
        on_2 = self.control.ON_2
        off_2 = self.control.OFF_2
        
        if (on_1 < time_check < off_1) or (on_2 < time_check < off_2):
            
            if self.acquisition.TEMPERATURE > self.control.SET_TEMP + 0.4 and self.check_state():
                self.run_to_idle()

    def while_idle(self):

        time_check = datetime.strptime(datetime.utcnow().time().strftime('%H:%M'), '%H:%M').time()
        on_1 = self.control.ON_1
        off_1 = self.control.OFF_1
        on_2 = self.control.ON_2
        off_2 = self.control.OFF_2
        
        if (on_1 < time_check < off_1) or (on_2 < time_check < off_2):
            
            if self.acquisition.TEMPERATURE < self.control.SET_TEMP - 0.4 and not self.check_state():
                self.idle_to_run()

    def on_running(self):
        self.pi.write(27, 1)

    def on_idle(self):
        self.pi.write(27, 0)

    def check_state(self):
        return self.pi.read(27)

