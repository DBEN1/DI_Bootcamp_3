const express = require('express');
const app = express();
const PORT = 3000;

let posts = [
    { id: 1, title: 'First Post', content: 'This is the first post' },
    // ... other posts
];

app.use(express.json());

app.get('/posts', (req, res) => {
    res.json(posts);
});

app.get('/posts/:id', (req, res) => {
    const post = posts.find(p => p.id === parseInt(req.params.id));
    if (!post) return res.status(404).send('Post not found');
    res.json(post);
});

app.post('/posts', (req, res) => {
    const post = {
        id: posts.length + 1,
        title: req.body.title,
        content: req.body.content
    };
    posts.push(post);
    res.status(201).json(post);
});

app.put('/posts/:id', (req, res) => {
    const post = posts.find(p => p.id === parseInt(req.params.id));
    if (!post) return res.status(404).send('Post not found');
    post.title = req.body.title;
    post.content = req.body.content;
    res.json(post);
});

app.delete('/posts/:id', (req, res) => {
    const postIndex = posts.findIndex(p => p.id === parseInt(req.params.id));
    if (postIndex === -1) return res.status(404).send('Post not found');
    posts.splice(postIndex, 1);
    res.status(204).send();
});

app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`);
});
