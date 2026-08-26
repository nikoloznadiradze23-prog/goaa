const handleRegister = (req, res) => {
    const { username, email, password } = req.body;
    console.log(req.body);
};

module.exports = { handleRegister };
