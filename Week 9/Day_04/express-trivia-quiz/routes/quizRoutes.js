import express from 'express';
import { triviaQuestions } from '../triviaModel.js';

const router = express.Router();

let score = 0;
let currentQuestionIndex = 0;

router.get('/quiz', (req, res) => {
  if (currentQuestionIndex < triviaQuestions.length) {
    res.send(triviaQuestions[currentQuestionIndex].question);
  } else {
    res.send("Quiz completed! Check your score at /quiz/score");
  }
});

router.post('/quiz', (req, res) => {
  const userAnswer = req.body.answer;
  if (userAnswer === triviaQuestions[currentQuestionIndex].answer) {
    score++;
    res.send("Correct!");
  } else {
    res.send("Incorrect!");
  }
  currentQuestionIndex++;
  if (currentQuestionIndex < triviaQuestions.length) {
    res.redirect('/quiz');
  } else {
    res.redirect('/quiz/score');
  }
});

router.get('/quiz/score', (req, res) => {
  res.send(`Your final score is: ${score}`);
});

export default router;
