import json  # Import json so workflow events can be stored in a readable text format.
from pathlib import Path  # Import Path so the adapter can manage its storage file safely.
from ports.memory_store import MemoryStore  # Import the memory contract that this adapter must implement.

class JsonMemoryStore(MemoryStore):  # Implement MemoryStore using one local JSON file.
    def __init__(self, filename="week5_memory.json"):  # Allow the caller to select a filename while providing a beginner-friendly default.
        self.path = Path(filename)  # Convert the filename into a Path object and keep it as adapter state.
    def load(self):  # Implement the load operation required by MemoryStore.
        if not self.path.exists():  # Check whether any memory has been stored by an earlier run.
            return []  # Return an empty history when the storage file does not exist yet.
        return json.loads(self.path.read_text(encoding="utf-8"))  # Read the JSON text and convert it back into a Python list.
    def append(self, event):  # Implement the append operation required by MemoryStore.
        events = self.load()  # Load the current persistent event history.
        events.append(event)  # Add the supplied event to the in-memory history.
        self.path.write_text(json.dumps(events, indent=2), encoding="utf-8")  # Serialize and save the updated history to disk.
