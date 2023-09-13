import express from 'express';
import bcrypt from 'bcrypt';
import fs from 'fs/promises';
import path from 'path';
import userRoutes from './routes/users.js';

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(userRoutes);

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
