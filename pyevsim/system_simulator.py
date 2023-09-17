from .simulation_engine import SimEngine
from .base.definition import SingletonType, Infinite
from threading import Thread

from .base.termination_manager import TerminationManager

class SysSimulator(object):
    __metaclass__ = SingletonType
    _engine = {}

    @staticmethod
    def register_engine(sim_name, sim_mode='VIRTUAL_TIME', time_step=1) -> SimEngine:
        SysSimulator._engine[sim_name] = SimEngine(time_step, sim_name, sim_mode)
        return SysSimulator._engine[sim_name] 

    @staticmethod
    def get_engine_map():
        return SysSimulator._engine

    @staticmethod
    def get_engine(sim_name):
        return SysSimulator._engine[sim_name]

    @staticmethod
    def is_terminated(sim_name):
        return SysSimulator._engine[sim_name].is_terminated()

    @staticmethod
    def is_terminated(sim_name):
        return SysSimulator._engine[sim_name].is_terminated()
    
    def exec_non_block_simulate(self, sim_list):
        self.thread_list = []
        for sim_name in sim_list:
            sim_inst = SysSimulator._engine[sim_name]
            p = Thread(target=sim_inst.simulate, args=(Infinite, False), daemon=True)
            self.thread_list.append(p)
            p.start()
            
            #p.join()

    def block(self):
        self.tm = TerminationManager()

        for t in self.thread_list:
            while t.is_alive():
                t.join(1)
    
    def __init__(self):
        pass



