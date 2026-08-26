const express = require('express');
const authRouter = express.Router();

authRouter.post('/signup', (req, res) => {
    const { username, email, password } = req.body;

    console.log(req.body);
});

export default authRouter;
