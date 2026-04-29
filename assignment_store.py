import json
from pathlib import Path

class AssignmentStore:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.assignments = self.load_assignments()

    def load_assignments(self):
        if self.file_path.exists():
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return []

    def save_assignments(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.assignments, f, indent=4)

    def add_assignment(self, assignment):
        self.assignments.append(assignment)
        self.save_assignments()

    def get_assignments(self):
        return self.assignments