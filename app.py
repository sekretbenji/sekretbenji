"""Class App: a tiny CLI and model for managing classes and student rosters."""

from dataclasses import dataclass, field


@dataclass
class Classroom:
    """Represents a class with a name and enrolled students."""

    name: str
    students: list[str] = field(default_factory=list)

    def enroll(self, student_name: str) -> None:
        """Enroll a student if they are not already in the class."""
        clean_name = student_name.strip()
        if not clean_name:
            raise ValueError("Student name cannot be empty")
        if clean_name not in self.students:
            self.students.append(clean_name)

    def remove(self, student_name: str) -> bool:
        """Remove a student if present. Returns True if removed."""
        if student_name in self.students:
            self.students.remove(student_name)
            return True
        return False

    def count(self) -> int:
        """Return current number of enrolled students."""
        return len(self.students)

    def summary(self) -> str:
        """Return a printable summary of this class."""
        roster = ", ".join(self.students) if self.students else "No students yet"
        return f"Class: {self.name} | Students ({self.count()}): {roster}"


def main() -> None:
    """Simple interactive command loop for the class app."""
    classroom = Classroom("General Studies")

    print("Class App")
    print("Commands: add <name>, remove <name>, list, quit")

    while True:
        raw = input("> ").strip()
        if not raw:
            continue

        if raw == "quit":
            print("Goodbye!")
            break

        if raw == "list":
            print(classroom.summary())
            continue

        action, _, argument = raw.partition(" ")

        if action == "add":
            try:
                classroom.enroll(argument)
                print(f"Added: {argument.strip()}")
            except ValueError as err:
                print(err)
        elif action == "remove":
            removed = classroom.remove(argument.strip())
            print("Removed" if removed else "Student not found")
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
