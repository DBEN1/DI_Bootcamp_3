// routes/books.js
import express from 'express';

const router = express.Router();

// Sample in-memory database for storing books
const books = [];

// Get all books
router.get('/books', (req, res) => {
    res.json(books);
});

// Add a new book
router.post('/books', (req, res) => {
    const book = {
        id: books.length + 1,
        title: req.body.title,
        author: req.body.author
    };
    books.push(book);
    res.status(201).json(book);
});

// Get a specific book by ID
router.get('/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).send('Book not found.');
    res.json(book);
});

// Update a book by ID
router.put('/books/:id', (req, res) => {
    const book = books.find(b => b.id === parseInt(req.params.id));
    if (!book) return res.status(404).send('Book not found.');

    book.title = req.body.title;
    book.author = req.body.author;

    res.json(book);
});

// Delete a book by ID
router.delete('/books/:id', (req, res) => {
    const bookIndex = books.findIndex(b => b.id === parseInt(req.params.id));
    if (bookIndex === -1) return res.status(404).send('Book not found.');

    const deletedBook = books.splice(bookIndex, 1);
    res.json(deletedBook);
});

export default router;
