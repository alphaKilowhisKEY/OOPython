# Quiz App

## Description
This Python script implements a simple quiz application where users can answer True/False questions. It utilizes classes to represent questions and the quiz itself, and it keeps track of the user's score.

## Features
- **Question Representation**: Each question is represented by a `Question` object containing the question text and the correct answer.
- **Quiz Management**: The `QuizBrain` class manages the quiz by presenting questions to the user, checking their answers, and keeping track of the score.
- **Question Bank**: The script retrieves question data from an external source (`question_data`) and constructs a list of `Question` objects to form the question bank.
- **User Interaction**: The user interacts with the quiz by inputting their answers as True or False.

## Usage
1. Run the script to start the quiz.
2. Answer each question by typing "True" or "False" when prompted.
3. Receive immediate feedback on your answer.
4. Once all questions have been answered, see your final score.

## Requirements
- Python 3.x

## Files
- **question_model.py**: Defines the `Question` class, which represents individual questions.
- **quiz_brain.py**: Defines the `QuizBrain` class, which manages the quiz and user interaction.
- **data.py**: Contains the question data used to create the question bank.
- **main.py**: The main script that initializes the quiz and controls the flow of the quiz.