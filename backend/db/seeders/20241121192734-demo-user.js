'use strict';

const { User } = require('../models');
const bcrypt = require("bcryptjs");

let options = {};
if (process.env.NODE_ENV === 'production') {
  options.schema = process.env.SCHEMA;  
}

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await User.bulkCreate([
      {
        email: 'demo@user.io',
        username: 'DemoUser',
        hashedPassword: bcrypt.hashSync('password')
      },
      {
        email: 'jane.doe@example.com',
        username: 'JaneDoe',
        hashedPassword: bcrypt.hashSync('password2')
      },
      {
        email: 'john.smith@example.com',
        username: 'JohnSmith',
        hashedPassword: bcrypt.hashSync('password3')
      },
      {
        email: 'emily.brown@example.com',
        username: 'EmilyBrown',
        hashedPassword: bcrypt.hashSync('password4')
      },
      {
        email: 'michael.jones@example.com',
        username: 'MichaelJones',
        hashedPassword: bcrypt.hashSync('password5')
      },
      {
        email: 'sarah.johnson@example.com',
        username: 'SarahJohnson',
        hashedPassword: bcrypt.hashSync('password6')
      },
      {
        email: 'david.williams@example.com',
        username: 'DavidWilliams',
        hashedPassword: bcrypt.hashSync('password7')
      },
      {
        email: 'olivia.miller@example.com',
        username: 'OliviaMiller',
        hashedPassword: bcrypt.hashSync('password8')
      },
      {
        email: 'william.davis@example.com',
        username: 'WilliamDavis',
        hashedPassword: bcrypt.hashSync('password9')
      },
      {
        email: 'sophia.moore@example.com',
        username: 'SophiaMoore',
        hashedPassword: bcrypt.hashSync('password10')
      },
      {
        email: 'daniel.taylor@example.com',
        username: 'DanielTaylor',
        hashedPassword: bcrypt.hashSync('password11')
      }
    ], {
      validate: true
    });
  },

  async down(queryInterface, Sequelize) {
    const options = { tableName: 'Users' };
    return queryInterface.bulkDelete(options, {}, {}); 
  }
};
