# SoundStats

## Database Schema Design

![db-schema]

[db-schema]: ./images/DB-SCHEMA.png

## Features

1. **User Authentication**
   - Create and manage user accounts.
   - Login and logout functionality.
   - User profile management.

2. **Music Data Management**
   - Full CRUD operations on music data.
   - View and analyze music sales and streaming trends.

3. **Report Management**
   - Generate, view, edit, and delete analytical reports.
   - Query-based report generation for personalized insights.

4. **Search Feature (Bonus)**
   - Search for specific music data entries based on filters (e.g., genre, sales, artist).
   - Fetch and display results dynamically.

---

## User Stories

### 1. **User Authentication**

#### Routes:  
`/login`, `/signup`, `/logout`, `/profile`

#### Logged-Out User Capabilities:  
- **Sign Up**: Create an account to access personalized features.  
- **Log In**: Use credentials to access personalized reports and dashboards.

#### Logged-In User Capabilities:  
- **Log Out**: End the session securely.  
- **View Profile**: Access and update account details like username and email.

#### User Scenarios:
- **Sign-Up:**  
  - Navigate to `/signup`.  
  - Complete a form with a username, email, and password.  
  - Upon success, the user is redirected to the login page.  

- **Log-In:**  
  - Navigate to `/login`.  
  - Input credentials (email and password).  
  - After successful authentication, the user is redirected to their dashboard.

- **Log-Out:**  
  - Click the "Logout" button.  
  - The session is terminated, and the user is redirected to the homepage.  

- **Profile Viewing/Editing:**  
  - Navigate to `/profile`.  
  - View or update account details. Changes are saved upon form submission.

---

### 2. **Music Data Management**

#### Routes:  
`/music-data`, `/music-data/:id`, `/music-data/create`, `/music-data/edit/:id`, `/music-data/delete/:id`

#### Logged-Out User Capabilities:  
- View the list of music data entries for exploration.

#### Logged-In User Capabilities:  
- **Create** new music data entries.  
- **Edit** existing entries to ensure data accuracy.  
- **Delete** outdated or irrelevant data.

#### User Scenarios:
- **Adding New Music Data:**  
  - Navigate to `/music-data/create`.  
  - Fill out a form with attributes like title, artist, genre, region, sales, streams, and release date.  
  - On submission, the data is saved, and the user is redirected to the listing page.  

- **Viewing Music Data:**  
  - Navigate to `/music-data`.  
  - Access a list or table of all music entries.  

- **Editing Music Data:**  
  - Navigate to `/music-data/edit/:id`.  
  - Update relevant fields and save changes.  

- **Deleting Music Data:**  
  - Navigate to `/music-data/delete/:id`.  
  - Confirm the deletion, and the data entry is removed from the system.  

---

### 3. **Report Management**

#### Routes:  
`/reports`, `/reports/:id`, `/reports/create`, `/reports/edit/:id`, `/reports/delete/:id`

#### Logged-Out User Capabilities:  
- View publicly available reports if enabled.

#### Logged-In User Capabilities:  
- **Create** custom reports by filtering and querying music data.  
- **Edit** existing reports to refine or update analysis.  
- **Delete** outdated reports to maintain organization.

#### User Scenarios:
- **Generate a New Report:**  
  - Navigate to `/reports/create`.  
  - Select filters like genre, sales, or region.  
  - Generate and save a report, which is displayed for further analysis.

- **Viewing Reports:**  
  - Navigate to `/reports`.  
  - View a list of all generated reports, with details like title, description, and creation date.

- **Editing Reports:**  
  - Navigate to `/reports/edit/:id`.  
  - Modify filters or update the report description, then save changes.  

- **Deleting Reports:**  
  - Navigate to `/reports/delete/:id`.  
  - Confirm deletion, and the report is removed.

---

### 4. **Search Feature (Future Feature)**

#### Routes:  
`/search`, `/search/:query`

#### Logged-Out User Capabilities:  
- Search for music data entries based on filters like genre, artist, or sales.

#### Logged-In User Capabilities:  
- Search for music data and save the results or use them for analysis.

#### User Scenarios:
- **Search Music Data:**  
  - Navigate to `/search`.  
  - Enter a query (e.g., artist name or genre).  
  - Filtered results are dynamically fetched and displayed based on the query.  

---

## Summary of User Capabilities

| **Feature**           | **Logged-In User**                         | **Logged-Out User**                |
|------------------------|--------------------------------------------|------------------------------------|
| **Authentication**    | Log in, log out, view/edit profile         | Sign up, log in                   |
| **Music Data**         | Create, edit, delete, view data entries    | View only                         |
| **Reports**            | Create, edit, delete, view reports         | View publicly available reports   |
| **Search**             | Search and analyze data                   | Search and view data              |

---

## Getting Started

1. Clone the repository.  
2. Install dependencies: `npm install`  
3. Run the development server: `npm start`
4. Run the frontend server: `npm run dev`  

## Technologies Used
- **Frontend**: React.js  
- **Backend**: Express (Javascript)  
- **Database**: PostgreSQL  

---
