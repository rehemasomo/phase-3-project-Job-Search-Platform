# Job Search Platform CLI

Welcome to the Job Search Platform CLI! This is a command-line interface (CLI) application that allows users to manage their job search activities. Users can create accounts, search for job listings, save searches,  and more.

## Features

- **User Account Management**
  - Create a new account
  - Update profile information
  - Retrieve account information using user ID
  - Delete an account

- **Job Listings**
  - create ,update,delete job listings
  - View job details

- **Saved Searches**
  - Create, update, and delete saved searches
  - List all saved searches

- **Job Applications**
  - create an application
  - update,delete and view applications
  - List all applications

- **Profile Viewing**
  - View user profiles

## Future Enhancements

- Viewing and posting reviews and ratings for job listings
- Connecting with other job seekers
- Receiving notifications for new job postings

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/rehemasomo/phase-3-project-job-search-platform.git
    ```
2. Navigate to the project directory:
    ```sh
    cd job-search-platform
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up the database:
    ```sh
    python create_tables.py
    ```

## Usage

Run the main script to start the CLI application:
```shpython main.py .

###Follow the on-screen prompts to navigate through the various features of the platform.
 
 ##Project Structure
 -main.py: Entry point for the CLI application.
 -create_tables.py: Script to create the necessary database tables.
 -check_tables.py: Utility script to check the status of the database tables.lib/: Directory containing all the modules and database files.
 -application.py: Handles job application functionality.
 -job_listing.py: Handles job listings functionality.
 -saved_search.py: Handles saved searches functionality.
 -user.py: Manages user account operations.
 -database.db: SQLite database file.

##Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas or suggestions.

##License
This project is licensed under the MIT License. See the LICENSE file for details.AcknowledgementsThank you for using the Job Search Platform CLI. If you have any questions or feedback, please feel free to contact us.
'https://github.com/rehemasomo/phase-3-project-job-search-platform.git'