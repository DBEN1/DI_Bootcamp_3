import express from 'express';
import bodyParser from 'body-parser';
import todosRouter from './routes/todos.js';


const app = express();

app.use(bodyParser.json());
app.use(todosRouter);

const PORT = 3000;

app.use(express.json());
app.use('/todos', todosRouter);

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
export default router;
