import sys
from models.user import User
from models.job_listing import JobListing
from models.application import Application
from models.saved_search import SavedSearch

def main_menu():
    print("Welcome To Job Search Platform")
    print("1. User Operations")
    print("2. Job Listings")
    print("3. Applications")
    print("4. Saved Searches")
    print("5. Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        user_operations()
    elif choice == '2':
        job_listing_operations()
    elif choice == '3':
        application_operations()
    elif choice == '4':
        saved_search_operations()
    elif choice == '5':
        sys.exit()
    else:
        print("Invalid choice, try again.")
        main_menu()

def user_operations():
    print("User Operations")
    print("1. Create Account")
    print("2. Delete Account")
    print("3. Update Profile")
    print("4. View User")
    print("5. List Users")
    print("6. Back to Main Menu")

    choice = input("Enter choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        delete_account()
    elif choice == '3':
        update_profile()
    elif choice == '4':
        view_user()
    elif choice == '5':
        list_users()
    elif choice == '6':
        main_menu()
    else:
        print("Invalid choice, try again.")
        user_operations()

def create_account():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email = input("Enter email: ")
    User.create(username, password, email)
    print("Account created successfully!")
    user_operations()

def delete_account():
    username = input("Enter username to delete: ")
    User.delete(username)
    print("Account deleted successfully!")
    user_operations()

def update_profile():
    username = input("Enter username to update: ")
    password = input("Enter new password: ")
    email = input("Enter new email: ")
    User.update(username, password, email)
    print("Profile updated successfully!")
    user_operations()

def view_user():
    username = input("Enter username to view: ")
    user = User.get(username)
    if user:
        print(dict(user))
    else:
        print("User not found.")
    user_operations()

def list_users():
    users = User.list()
    for user in users:
        print(dict(user))
    user_operations()

def job_listing_operations():
    print("Job Listing Operations")
    print("1. Create Job Listing")
    print("2. Delete Job Listing")
    print("3. Update Job Listing")
    print("4. View Job Listing")
    print("5. List Job Listings")
    print("6. Back to Main Menu")

    choice = input("Enter choice: ")

    if choice == '1':
        create_job_listing()
    elif choice == '2':
        delete_job_listing()
    elif choice == '3':
        update_job_listing()
    elif choice == '4':
        view_job_listing()
    elif choice == '5':
        list_job_listings()
    elif choice == '6':
        main_menu()
    else:
        print("Invalid choice, try again.")
        job_listing_operations()

def create_job_listing():
    title = input("Enter job title: ")
    description = input("Enter job description: ")
    company = input("Enter company name: ")
    JobListing.create(title, description, company)
    print("Job listing created successfully!")
    job_listing_operations()

def delete_job_listing():
    job_id = input("Enter job ID to delete: ")
    JobListing.delete(job_id)
    print("Job listing deleted successfully!")
    job_listing_operations()

def update_job_listing():
    job_id = input("Enter job ID to update: ")
    title = input("Enter new job title: ")
    description = input("Enter new job description: ")
    company = input("Enter new company name: ")
    JobListing.update(job_id, title, description, company)
    print("Job listing updated successfully!")
    job_listing_operations()

def view_job_listing():
    job_id = input("Enter job ID to view: ")
    job = JobListing.get(job_id)
    if job:
        print(dict(job))
    else:
        print("Job listing not found.")
    job_listing_operations()

def list_job_listings():
    jobs = JobListing.list()
    for job in jobs:
        print(dict(job))
    job_listing_operations()

def application_operations():
    print("Application Operations")
    print("1. Create Application")
    print("2. Delete Application")
    print("3. Update Application")
    print("4. View Application")
    print("5. List Applications")
    print("6. Back to Main Menu")

    choice = input("Enter choice: ")

    if choice == '1':
        create_application()
    elif choice == '2':
        delete_application()
    elif choice == '3':
        update_application()
    elif choice == '4':
        view_application()
    elif choice == '5':
        list_applications()
    elif choice == '6':
        main_menu()
    else:
        print("Invalid choice, try again.")
        application_operations()

def create_application():
    user_id = input("Enter user ID: ")
    job_id = input("Enter job ID: ")
    status = input("Enter application status: ")
    Application.create(user_id, job_id, status)
    print("Application created successfully!")
    application_operations()

def delete_application():
    application_id = input("Enter application ID to delete: ")
    Application.delete(application_id)
    print("Application deleted successfully!")
    application_operations()

def update_application():
    application_id = input("Enter application ID to update: ")
    status = input("Enter new application status: ")
    Application.update(application_id, status)
    print("Application updated successfully!")
    application_operations()

def view_application():
    application_id = input("Enter application ID to view: ")
    application = Application.get(application_id)
    if application:
        print(dict(application))
    else:
        print("Application not found.")
    application_operations()

def list_applications():
    applications = Application.list()
    for application in applications:
        print(dict(application))
    application_operations()

def saved_search_operations():
    print("Saved Search Operations")
    print("1. Create Saved Search")
    print("2. Delete Saved Search")
    print("3. Update Saved Search")
    print("4. View Saved Search")
    print("5. List Saved Searches")
    print("6. Back to Main Menu")

    choice = input("Enter choice: ")

    if choice == '1':
        create_saved_search()
    elif choice == '2':
        delete_saved_search()
    elif choice == '3':
        update_saved_search()
    elif choice == '4':
        view_saved_search()
    elif choice == '5':
        list_saved_searches()
    elif choice == '6':
        main_menu()
    else:
        print("Invalid choice, try again.")
        saved_search_operations()

def create_saved_search():
    user_id = input("Enter user ID: ")
    search_query = input("Enter search query: ")
    SavedSearch.create(user_id, search_query)
    print("Saved search created successfully!")
    saved_search_operations()

def delete_saved_search():
    saved_search_id = input("Enter saved search ID to delete: ")
    SavedSearch.delete(saved_search_id)
    print("Saved search deleted successfully!")
    saved_search_operations()

def update_saved_search():
    saved_search_id = input("Enter saved search ID to update: ")
    search_query = input("Enter new search query: ")
    SavedSearch.update(saved_search_id, search_query)
    print("Saved search updated successfully!")
    saved_search_operations()

def view_saved_search():
    saved_search_id = input("Enter saved search ID to view: ")
    saved_search = SavedSearch.get(saved_search_id)
    if saved_search:
        print(dict(saved_search))
    else:
        print("Saved search not found.")
    saved_search_operations()

def list_saved_searches():
    saved_searches = SavedSearch.list()
    for saved_search in saved_searches:
        print(dict(saved_search))
    saved_search_operations()

if __name__ == '__main__':
    main_menu()

