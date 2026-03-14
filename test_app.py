import unittest

from app import Classroom


class ClassroomTests(unittest.TestCase):
    def test_enroll_adds_unique_students(self):
        classroom = Classroom("Math")
        classroom.enroll("Ada")
        classroom.enroll("Ada")
        self.assertEqual(classroom.students, ["Ada"])

    def test_enroll_rejects_empty_name(self):
        classroom = Classroom("Science")
        with self.assertRaises(ValueError):
            classroom.enroll("   ")

    def test_remove_returns_boolean(self):
        classroom = Classroom("History", ["Ben"])
        self.assertTrue(classroom.remove("Ben"))
        self.assertFalse(classroom.remove("Ben"))

    def test_summary_contains_count(self):
        classroom = Classroom("English", ["A", "B"])
        summary = classroom.summary()
        self.assertIn("Students (2)", summary)


if __name__ == "__main__":
    unittest.main()
