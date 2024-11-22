'use strict';

const bcrypt = require("bcryptjs");

let options = {};
if (process.env.NODE_ENV === 'production') {
  options.schema = process.env.SCHEMA;  
}

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Users', [
      {
        email: 'demo@user.io',
        username: 'DemoUser',
        hashedPassword: bcrypt.hashSync('password'),
        firstName: 'Demo',
        lastName: 'User',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'jane.doe@example.com',
        username: 'JaneDoe',
        hashedPassword: bcrypt.hashSync('password2'),
        firstName: 'Jane',
        lastName: 'Doe',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'john.smith@example.com',
        username: 'JohnSmith',
        hashedPassword: bcrypt.hashSync('password3'),
        firstName: 'John',
        lastName: 'Smith',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'emily.brown@example.com',
        username: 'EmilyBrown',
        hashedPassword: bcrypt.hashSync('password4'),
        firstName: 'Emily',
        lastName: 'Brown',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'michael.jones@example.com',
        username: 'MichaelJones',
        hashedPassword: bcrypt.hashSync('password5'),
        firstName: 'Michael',
        lastName: 'Jones',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'sarah.johnson@example.com',
        username: 'SarahJohnson',
        hashedPassword: bcrypt.hashSync('password6'),
        firstName: 'Sarah',
        lastName: 'Johnson',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'david.williams@example.com',
        username: 'DavidWilliams',
        hashedPassword: bcrypt.hashSync('password7'),
        firstName: 'David',
        lastName: 'Williams',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'olivia.miller@example.com',
        username: 'OliviaMiller',
        hashedPassword: bcrypt.hashSync('password8'),
        firstName: 'Olivia',
        lastName: 'Miller',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'william.davis@example.com',
        username: 'WilliamDavis',
        hashedPassword: bcrypt.hashSync('password9'),
        firstName: 'William',
        lastName: 'Davis',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'sophia.moore@example.com',
        username: 'SophiaMoore',
        hashedPassword: bcrypt.hashSync('password10'),
        firstName: 'Sophia',
        lastName: 'Moore',
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        email: 'daniel.taylor@example.com',
        username: 'DanielTaylor',
        hashedPassword: bcrypt.hashSync('password11'),
        firstName: 'Daniel',
        lastName: 'Taylor',
        createdAt: new Date(),
        updatedAt: new Date()
      }
    ], {
      validate: true
    });
  },

  async down(queryInterface, Sequelize) {
    options.tableName = 'Users';
    return queryInterface.bulkDelete(options, null, {});
  }
};
