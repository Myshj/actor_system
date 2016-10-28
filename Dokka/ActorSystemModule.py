from Dokka.Actors import *

from Dokka.Messages import CreateActor


class ActorSystemModule(ProcessActor):
    def __init__(self, outbox):
        super(ActorSystemModule, self).__init__()
        self._outbox = outbox

    def on_received(self, message):
        if isinstance(message, CreateActor):
            print('CreateActor received!')
            print(message.actor_class)
