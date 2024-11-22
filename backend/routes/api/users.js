const express = require('express')
const router = express.Router();
const bcrypt = require('bcryptjs');
const { setTokenCookie, requireAuth } = require('../../utils/auth');
const { User } = require('../../db/models');

// Sign up
router.post(
  '/',
  // validateSignup, // Use existing validation logic
  async (req, res) => {
    const { firstName, lastName, email, password, username } = req.body;
    const hashedPassword = bcrypt.hashSync(password);

    try {
      const existingEmail = await User.findOne({ where: { email } });
      const existingUsername = await User.findOne({ where: { username } });

      if (existingEmail || existingUsername)   
 {
        const errors = {};
        if (existingEmail) errors.email = "User with that email already exists";
        if (existingUsername) errors.username = "User with that username already exists";
        return res.status(500).json({ message: "User already exists", errors });
      }

      const user = await User.create({ firstName, lastName, email, username, hashedPassword });

      const safeUser = {
        id: user.id,
        firstName:   
 user.firstName,
        lastName: user.lastName,
        email: user.email,
        username: user.username,
      };

      await setTokenCookie(res, safeUser);

      return res.status(201).json({
        user: safeUser   

      });
    } catch (error) {
      console.error(error); 
      return res.status(500).json({ message: 'An error occurred' }); 
    }
  }
);


module.exports = router;
