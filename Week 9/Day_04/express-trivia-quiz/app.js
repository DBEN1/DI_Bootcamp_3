import express from 'express';
import quizRouter from './routes/quizRoutes.js';

const app = express();
const PORT = 3000;

app.use(express.json());
app.use('/', quizRouter);

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
