const router = require('express').Router();
const { restoreUser, requireAuth, setTokenCookie } = require('../../utils/auth.js');
// const { User } = require('../../db/models');
const sessionRouter = require('./session.js');
const usersRouter = require('./users.js');

//restore user 
router.use(restoreUser);

router.use('/session', sessionRouter);

router.use('/users', usersRouter);
// //test setting the token cookie
// router.get('/set-token-cookie', async (_req, res) => {
//   const user = await User.findOne({
//     where: {
//       username: 'DemoUser',
//     },
//   });
//   setTokenCookie(res, user);
//   return res.json({ user });
// });

// // test restored user
// router.get('/restore-user', (req, res) => {
//   return res.json(req.user);
// });

// // test req auth
// router.get('/require-auth', requireAuth, (req, res) => {
//   return res.json(req.user);
// });

// Test POST route
router.post('/test', (req, res) => {
  res.json({ requestBody: req.body });
});

module.exports = router;
