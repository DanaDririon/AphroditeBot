class CommandFactory(object):
    
    def __init__(self, config):
        self.config = config

    def command(self, bot, commandName):
        