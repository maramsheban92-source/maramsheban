#!/usr/bin/env python3
"""
Tests for the Quiz application.
"""

import unittest
from unittest.mock import patch
from io import StringIO
import quiz


class TestQuiz(unittest.TestCase):
    """Test cases for the Quiz class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.quiz = quiz.Quiz()
    
    def test_quiz_initialization(self):
        """Test that quiz initializes correctly."""
        self.assertEqual(self.quiz.score, 0)
        self.assertIsInstance(self.quiz.questions, list)
        self.assertGreater(len(self.quiz.questions), 0)
    
    def test_questions_structure(self):
        """Test that questions have the correct structure."""
        for q in self.quiz.questions:
            self.assertIn("question", q)
            self.assertIn("options", q)
            self.assertIn("answer", q)
            self.assertIsInstance(q["question"], str)
            self.assertIsInstance(q["options"], list)
            self.assertEqual(len(q["options"]), 4)
            self.assertIn(q["answer"], ["A", "B", "C", "D"])
    
    def test_get_answer_valid(self):
        """Test get_answer with valid input."""
        with patch('builtins.input', return_value='A'):
            result = self.quiz.get_answer()
            self.assertEqual(result, 'A')
    
    def test_get_answer_lowercase(self):
        """Test get_answer converts lowercase to uppercase."""
        with patch('builtins.input', return_value='b'):
            result = self.quiz.get_answer()
            self.assertEqual(result, 'B')
    
    def test_get_answer_with_whitespace(self):
        """Test get_answer strips whitespace."""
        with patch('builtins.input', return_value='  C  '):
            result = self.quiz.get_answer()
            self.assertEqual(result, 'C')
    
    def test_show_results(self):
        """Test show_results displays correctly."""
        self.quiz.score = 3
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.quiz.show_results()
            output = fake_out.getvalue()
            self.assertIn("Quiz Complete!", output)
            self.assertIn("3/5", output)
            self.assertIn("60.0%", output)


class TestQuizIntegration(unittest.TestCase):
    """Integration tests for the quiz application."""
    
    @patch('builtins.input', side_effect=['B', 'B', 'C', 'D', 'B'])
    def test_full_quiz_perfect_score(self, mock_input):
        """Test running quiz with all correct answers."""
        test_quiz = quiz.Quiz()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            test_quiz.run()
            output = fake_out.getvalue()
            self.assertIn("5/5", output)
            self.assertIn("100.0%", output)
            self.assertIn("Perfect score!", output)
    
    @patch('builtins.input', side_effect=['A', 'A', 'A', 'A', 'A'])
    def test_full_quiz_zero_score(self, mock_input):
        """Test running quiz with all incorrect answers."""
        test_quiz = quiz.Quiz()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            test_quiz.run()
            output = fake_out.getvalue()
            self.assertIn("0/5", output)
            self.assertIn("0.0%", output)


if __name__ == '__main__':
    unittest.main()
