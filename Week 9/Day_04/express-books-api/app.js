import express from 'express';
import booksRouter from './routes/books.js';

const app = express();

app.use(express.json()); // This middleware is required to parse JSON request bodies
app.use(booksRouter);

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
