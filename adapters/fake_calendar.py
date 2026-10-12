from ports.calendar_port import CalendarPort, CalendarUnavailableError  # Import the calendar contract and its provider-independent failure type.

class FakeCalendarAdapter(CalendarPort):  # Implement CalendarPort with deterministic local data instead of a real external service.
    def __init__(self, should_fail=False):  # Allow the demonstration to switch between success and simulated failure.
        self.should_fail = should_fail  # Store whether this adapter should fail when the application calls it.
    def get_availability(self):  # Implement the operation required by CalendarPort.
        print("FakeCalendarAdapter: get_availability() called")  # Show which concrete adapter is performing the external-style action.
        if self.should_fail:  # Check whether the selected scenario asks for a simulated provider failure.
            raise CalendarUnavailableError("Calendar service unavailable")  # Raise the port-level error instead of leaking provider-specific details.
        return ["Monday 14:00-16:00", "Tuesday 10:00-12:00"]  # Return stable fake slots so the lab needs no account, API key, or network access.
