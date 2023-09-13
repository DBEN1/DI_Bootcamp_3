
import express from 'express';

const router = express.Router();

// Sample in-memory database for storing to-do items
const todos = [];

// Get all to-do items
router.get('/todos', (req, res) => {
    res.json(todos);
});

// Add a new to-do item
router.post('/todos', (req, res) => {
    const todo = {
        id: Date.now(),
        text: req.body.text,
        completed: false
    };
    todos.push(todo);
    res.status(201).json(todo);
});

// Update a to-do item by ID
router.put('/todos/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    const todoIndex = todos.findIndex(t => t.id === id);
    if (todoIndex === -1) {
        return res.status(404).json({ error: 'Todo not found' });
    }
    todos[todoIndex].text = req.body.text || todos[todoIndex].text;
    todos[todoIndex].completed = req.body.completed !== undefined ? req.body.completed : todos[todoIndex].completed;
    res.json(todos[todoIndex]);
});

// Delete a to-do item by ID
router.delete('/todos/:id', (req, res) => {
    const id = parseInt(req.params.id, 10);
    const todoIndex = todos.findIndex(t => t.id === id);
    if (todoIndex === -1) {
        return res.status(404).json({ error: 'Todo not found' });
    }
    todos.splice(todoIndex, 1);
    res.status(204).end();
});

export default router;
