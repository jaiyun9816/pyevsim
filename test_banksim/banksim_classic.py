from pyevsim.base.definition import *
from pyevsim.system_simulator import SysSimulator

from .model_acoountant import BankAccountant
from .model_queue import BankQueue
from .model_user_gen import BankUserGenerator

def execute_simulation(engine_name = "test_case", t_resol=1, execution_mode="REAL_TIME"):
    ss = SysSimulator()
    ss.register_engine(engine_name, execution_mode, t_resol)
        
    gen_num = 3             #Number of BankUserGenerators 
    queue_size = 10         #BankQueue size
    proc_num = 5            #Number of BankAccountant
    
    user_process_time = 3   #BankUser's processing speed
    gen_cycle = 2           #BankUser Generattion cycle
    max_user = 50000        #Total number of users generated
    
    
    instance_time = 0
    destruct_time = Infinite
    
    ## model set & register entity
    gen_list = []
    user = int(max_user / gen_num)
    for i in range(gen_num) :
        if i == gen_num-1:
            user += max_user % gen_num
        gen = BankUserGenerator(instance_time, destruct_time, engine_name, f'gen{i}', gen_cycle, user, user_process_time)
        gen_list.append(gen)    
        ss.get_engine(engine_name).register_entity(gen)    
        
    que = BankQueue(instance_time, destruct_time, engine_name, 'Queue', queue_size, proc_num)
    ss.get_engine(engine_name).register_entity(que)
    
    account_list = []
    for i in range(proc_num) :
        account = BankAccountant(instance_time, destruct_time, engine_name, 'BankAccountant', i)
        account_list.append(account)
        ss.get_engine(engine_name).register_entity(account)
        
    ## Model Relation
    ss.get_engine(engine_name).insert_input_port('start')

    for gen in gen_list : 
        ss.get_engine(engine_name).coupling_relation(None, 'start', gen, 'start')
        ss.get_engine(engine_name).coupling_relation(gen, 'user_out', que, 'user_in')
    for i in range(proc_num) : 
        ss.get_engine(engine_name).coupling_relation(que, f'proc{i}', account_list[i], 'in')
        ss.get_engine(engine_name).coupling_relation(account_list[i], 'next', que, 'proc_checked')
        
    ss.get_engine(engine_name).insert_external_event('start', None)

    ## simulation run    
    for i in range(100000):
        print()
        ss.get_engine(engine_name).simulate(1)
        
def test_casual_order1(capsys):
    execute_simulation("engine", 1, "VIRTUAL_TIME")
    print(capsys)
    