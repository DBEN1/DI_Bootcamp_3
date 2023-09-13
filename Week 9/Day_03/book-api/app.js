const express = require('express');
const app = express();
const PORT = 5000;

let books = [
    { id: 1, title: 'First Book', author: 'John Doe', publishedYear: 2020 },
    // ... other books
];

app.use(express.json());

app.get('/api/books', (req, res) => {
    res.json(books);
});

app.get('/api/books/:bookId', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.bookId));
    if (!book) return res.status(404).send('Book not found');
    res.json(book);
});

app.post('/api/books', (req, res) => {
    const book = {
        id: books.length + 1,
        title: req.body.title,
        author: req.body.author,
        publishedYear: req.body.publishedYear
    };
    books.push(book);
    res.status(201).json(book);
});

app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`);
});
