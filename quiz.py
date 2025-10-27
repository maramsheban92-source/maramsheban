#!/usr/bin/env python3
"""
Simple Quiz Application
A command-line quiz game that asks multiple-choice questions.
"""

import sys


class Quiz:
    """A simple quiz application."""
    
    def __init__(self):
        """Initialize the quiz with questions."""
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
                "answer": "B"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
                "answer": "B"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Venus", "B) Jupiter", "C) Mars", "D) Saturn"],
                "answer": "C"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
                "answer": "D"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
                "answer": "B"
            }
        ]
        self.score = 0
        
    def run(self):
        """Run the quiz."""
        print("=" * 50)
        print("Welcome to the Quiz Game!")
        print("=" * 50)
        print(f"\nYou will be asked {len(self.questions)} questions.")
        print("Enter the letter of your answer (A, B, C, or D).\n")
        
        for i, q in enumerate(self.questions, 1):
            print(f"\nQuestion {i}/{len(self.questions)}:")
            print(q["question"])
            for option in q["options"]:
                print(f"  {option}")
            
            answer = self.get_answer()
            
            if answer == q["answer"]:
                print("✓ Correct!")
                self.score += 1
            else:
                print(f"✗ Incorrect. The correct answer was {q['answer']}.")
        
        self.show_results()
    
    def get_answer(self):
        """Get and validate user answer."""
        while True:
            answer = input("\nYour answer: ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                return answer
            print("Invalid input. Please enter A, B, C, or D.")
    
    def show_results(self):
        """Display final results."""
        percentage = (self.score / len(self.questions)) * 100
        
        print("\n" + "=" * 50)
        print("Quiz Complete!")
        print("=" * 50)
        print(f"\nYour Score: {self.score}/{len(self.questions)} ({percentage:.1f}%)")
        
        if percentage == 100:
            print("Perfect score! Excellent work! 🎉")
        elif percentage >= 80:
            print("Great job! 👏")
        elif percentage >= 60:
            print("Good effort! 👍")
        else:
            print("Keep practicing! 📚")


def main():
    """Main entry point for the quiz application."""
    try:
        quiz = Quiz()
        quiz.run()
    except KeyboardInterrupt:
        print("\n\nQuiz interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
