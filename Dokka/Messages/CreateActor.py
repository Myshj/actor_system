from Message import Message


class CreateActor(Message):
    def __init__(self, sender, actor_class):
        super(CreateActor, self).__init__(sender)
        self.actor_class = actor_class
