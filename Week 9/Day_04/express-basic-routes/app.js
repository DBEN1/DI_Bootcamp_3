// app.js
import express from 'express';
import router from './routes/index.js';

const app = express();
const PORT = 3000;

app.use('/', router);

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
