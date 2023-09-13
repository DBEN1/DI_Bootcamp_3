import { Router } from 'express';
import bcrypt from 'bcrypt';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';


const router = Router();
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const usersFilePath = path.join(__dirname, '..', 'users.json');

async function readUsers() {
    const data = await fs.readFile(usersFilePath, 'utf-8');
    return JSON.parse(data);
}

async function writeUsers(users) {
    await fs.writeFile(usersFilePath, JSON.stringify(users, null, 2));
}

// POST /register
router.post('/register', async (req, res) => {
    const { name, lastName, email, username, password } = req.body;

    const users = await readUsers();
    const existingUser = users.find(user => user.username === username);

    if (existingUser) {
        return res.status(400).send('Username already exists');
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = { name, lastName, email, username, password: hashedPassword };
    users.push(newUser);

    await writeUsers(users);

    res.send('Hello! Your account is now created!');
});

// POST /login
router.post('/login', async (req, res) => {
    const { username, password } = req.body;

    const users = await readUsers();
    const user = users.find(u => u.username === username);

    if (!user) {
        return res.status(400).send('Username is not registered');
    }

    const isPasswordCorrect = await bcrypt.compare(password, user.password);
    if (!isPasswordCorrect) {
        return res.status(400).send('Incorrect password');
    }

    res.send(`Hi ${user.name}, welcome back!`);
});

// ... (Other routes can be added similarly)

export default router;
