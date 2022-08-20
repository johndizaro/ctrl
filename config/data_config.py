class DataConfig:
    def __init__(self):
        self.data_config_dict = dict()
        self.data_config_dict['log_no_terminal'] = True
        self.data_config_dict['log_no_arquivo'] = True
        self.data_config_dict['log_caminho'] = ''
        self.data_config_dict['log_nome'] = 'ctrl_log.log'
        self.data_config_dict['log_format'] = '%(levelname)-10s  logger:%(name)-15s %(asctime)s   filename:%(filename)s  módulo:%(module)-20s função:%(funcName)-20s  mensagem:%(message)s'
        self.data_config_dict['log_tipo'] = 'INFO'

    def convert_to_dict(self):
        pass

    def convert_from_dict(self):
        pass

    def validate_data(self):
        pass

