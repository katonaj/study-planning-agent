from abc import ABC, abstractmethod  # Import abstract-base-class tools so Python can express a memory-storage contract.

class MemoryStore(ABC):  # Define the contract that every persistent-memory adapter must satisfy.
    @abstractmethod  # Mark load as mandatory for concrete memory-store implementations.
    def load(self):  # Declare the operation that retrieves previously stored workflow events.
        raise NotImplementedError  # Prevent the abstract port from choosing a storage technology.
    @abstractmethod  # Mark append as mandatory for concrete memory-store implementations.
    def append(self, event):  # Declare the operation that stores one new workflow event.
        raise NotImplementedError  # Prevent the abstract port from implementing persistence itself.
