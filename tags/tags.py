from rackio import TagEngine, Rackio

engine = TagEngine()

acquisition = [
    ("TEMPERATURE", "float")
    ("PRESSURE", "float")
    ("HUMIDITY", "float")
]

control = [
    ("SET_TEMP", "float")
    ("ON_1", "str")
    ("ON_2", "str")
    ("OFF_1", "str")
    ("OFF_2", "str")
]

engine.set_group("acquisition", acquisition)
engine.set_group("control", control)

engine.write_tag("SET_TEMP", 20)
engine.write_tag("ON_1", "07:30")
engine.write_tag("ON_2", "17:30")
engine.write_tag("OFF_1", "09:30")
engine.write_tag("OFF_2", "22:00")
