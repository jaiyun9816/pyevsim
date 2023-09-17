class CoreModel(object):
    def __init__(self, _name, _type):
        # Model Type
        self._type = _type

        self._name = _name
        # Input Ports Declaration
        self._input_ports = []
        # Output Ports Declaration
        self._output_ports = []

    def set_name(self, _name):
        self._name = _name

    def get_name(self):
        return self._name

    def insert_input_port(self, port):
        setattr(self, port, port)
        self._input_ports.append(port)

    def retrieve_input_ports(self):
        return self._input_ports

    def insert_output_port(self, port):
        setattr(self, port, port)
        self._output_ports.append(port)

    def retrieve_output_ports(self):
        return self._output_ports

    def get_type(self):
        return self._type