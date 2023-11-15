# Bidayat Event Planning Platform

## What is Bidayat?
Bidayat is a helpful website for people who want to throw great parties and events. It's made to connect users (people planning events) with vendors (those providing services for events). We built this website using Python-Django technology.

## Features

### 1. User Profiles
- Users can make profiles to organize their events better.
- Profiles include details like event preferences and past events.

### 2. Vendor Showcase
- Vendors can show their work by adding pictures of what they've done before.
- Users can look through these to find the right vendor for their event.

### 3. Communication
- Users and vendors can talk to each other directly on the platform.
- This helps with discussing event details, agreeing on terms, and making things clear.

### 4. Event Dashboard
- Users get a dashboard to plan and keep track of their events.
- Vendors have their dashboard to manage inquiries, bookings, and show when they're available.

### 5. Technology
- Bidayat is built using Python-Django, a strong and reliable technology.

## Trello Board
[Project Trello Board](https://trello.com/b/ApMbhrRM/event-planning)

## Wireframes
[Wireframes Link](https://i.imgur.com/nKuf0yy.jpg)

## Entity Relationship Diagram (ERD)
![ERD Diagram](https://ibb.co/cXdJnvh)

### Project Technology
- Built using Python-Django technology.

## INSTALL PROCEDURE 
# Project Name Installation Guide

## Step 1: Clone the Repository
git clone [repository_url]
cd [repository_name]

### Step 2: Create .env File
- Create a file named .env in the root of the repository and add the following configuration:


- DATABASENAME=MyBidayat
- DATABASEPASSWORD=********
- DATABASEUSER=postgres
- DATABASEHOST=localhost
- DATABASEPORT=****

- Make sure to replace placeholders (********, ****, etc.) with your actual database credentials.

# Step 3: Set Up PostgreSQL Server
- Ensure that you have PostgreSQL installed on your machine or create a server on ElephantSQL. Update the .env file with the appropriate database configurations.

# Step 4: Run Migration Commands
- Execute the following commands to apply database migrations:


python manage.py makemigrations
python manage.py migrate

# Step 5: Run the Server
Start the development server using the following command:

python manage.py runserver
The application will be accessible at http://localhost:8000/ by default.


Let's make event planning a breeze with Bidayat!
