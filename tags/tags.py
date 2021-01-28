from rackio import TagEngine, Rackio

engine = TagEngine()

acquisition = [
    "TEMPERATURE",
    "PRESSURE",
    "HUMIDITY"
]

control = [
    "SET_TEMP",
    "ON_1",
    "ON_2",
    "OFF_1",
    "OFF_2"
]

engine.set_group("acquisition", acquisition)
engine.set_group("control", control)
