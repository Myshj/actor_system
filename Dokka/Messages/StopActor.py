from Message import Message


class StopActor(Message):
    def __init__(self, sender):
        super(StopActor, self).__init__(sender)
