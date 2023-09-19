from enum import Enum

Infinite = float("inf") # hug value

class ModelType(Enum):
    BEHAVIORAL  = 0
    STRUCTURAL  = 1
    UTILITY     = 2

class SimulationMode(Enum):
    SIMULATION_IDLE = 0         # Simulation Engine is instantiated but simulation is not running
    SIMULATION_RUNNING = 1      # Simulation Engine is instantiated, simulation is running
    SIMULATION_TERMINATED = 2   # Simulation Engine is instantiated but simulation is terminated
    SIMULATION_PAUSE = 3        # Simulation Engine is instantiated, simulation paused
    SIMULATION_UNKNOWN = -1     # Simulation Engine went to abnormal state


    #SIMATION_IDLE = 0 # 시뮬레이션 엔진이 인스턴스화되었지만 시뮬레이션이 실행되고 있지 않습니다
    #SIMATION_RUNING = 1 # 시뮬레이션 엔진이 인스턴스화되고, 시뮬레이션이 실행되고 있습니다
    #SIMATION_TERMINED = 2 # 시뮬레이션 엔진이 인스턴스화되지만 시뮬레이션이 종료됨
    #SIMATION_PAUSE = 3 # 시뮬레이션 엔진이 인스턴스화됨, 시뮬레이션이 일시 중지됨
    #SIMATION_UNKNOWN = -1 # SIMATION Engine이 비정상 상태가 되었습니다

class SingletonType(object):
    def __call__(self, cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance