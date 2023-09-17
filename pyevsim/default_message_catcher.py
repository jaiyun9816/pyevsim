from .behavior_model import BehaviorModel
from .system_message import SysMessage
from .base.definition import *

class DefaultMessageCatcher(BehaviorModel):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModel.__init__(self, instance_time, destruct_time, name, engine_name)

        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)

        self.insert_input_port("uncaught")

    def ext_trans(self, port, msg):
        data = msg.retrieve()

    def time_advance(self):
        return Infinite
