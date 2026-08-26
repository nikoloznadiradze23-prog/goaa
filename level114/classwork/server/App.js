const express = require("express");
const cors = require("cors");
const { authRouter } = require("./routers/auth.router");
const app = express();

// middleware
app.use(express.json());
app.use(cors({
    origin: 'http://localhost:5173'
}));

// routers
app.use(authRouter);

app.post('/root/auth/signup', (req, res) => {
    const { username, email, password } = req.body;
    console.log(req.body);
});

app.use('/root/auth', authRouter)
app.post('/root/auth/signup', (req, res) => {
    const { username, email, password } = req.body;

    console.log(req.body);
});

app.listen(3000, () => console.log("Server running on port 3000"));
