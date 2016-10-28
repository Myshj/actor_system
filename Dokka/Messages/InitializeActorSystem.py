from Message import Message


class InitializeActorSystem(Message):
    def __init__(self, sender, count_of_processes):
        super(InitializeActorSystem, self).__init__(sender)
        self.count_of_processes = count_of_processes
