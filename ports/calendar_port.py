from abc import ABC, abstractmethod  # Import abstract-base-class tools so Python can express an interface-like port.

class CalendarUnavailableError(Exception):  # Define a provider-independent error that the application layer is allowed to understand.
    pass  # No extra behavior is required; the meaningful exception type is enough for this teaching example.

class CalendarPort(ABC):  # Define the contract that every calendar adapter must satisfy.
    @abstractmethod  # Mark get_availability as mandatory for concrete CalendarPort implementations.
    def get_availability(self):  # Declare the operation that returns calendar availability to the application.
        raise NotImplementedError  # Prevent the abstract port from choosing any concrete calendar technology.
