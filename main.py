import tags
import api
import web
# import state_machines

from rackio import Rackio

if __name__ == '__main__':

    app = Rackio()
    app.set_log(file="app.log")

    app.run()