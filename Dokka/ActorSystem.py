from ActorSystemModule import ActorSystemModule
from Dokka.Actors import *
from Dokka.Messages import InitializeActorSystem, CreateActor

from multiprocessing import Queue


class ActorSystem(ProcessActor):
    def __init__(self):
        super(ActorSystem, self).__init__()
        self._modules = []
        self._outboxes_of_modules = []
        self._initialized = False
        self._count_of_processes = 0

    def on_received(self, message):
        if isinstance(message, InitializeActorSystem):
            self._on_initialize(message)
        elif isinstance(message, CreateActor):
            self._on_create_actor(message)

    def _on_initialize(self, message):
        if self._initialized:
            return

        self._count_of_processes = message.count_of_processes
        self._run_modules()
        self._initialized = True

    def _on_create_actor(self, message):
        self._modules[0].tell(message)

    def _run_modules(self):
        for i in xrange(0, self._count_of_processes):
            outbox = Queue()
            self._outboxes_of_modules.append(outbox)
            module = ActorSystemModule(outbox)
            module.start()
            self._modules.append(module)
