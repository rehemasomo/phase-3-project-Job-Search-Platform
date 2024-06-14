from faker import Faker
import random

fake = Faker()

# List of industries
industries = ['Technology', 'Finance', 'Healthcare', 'Education', 'Marketing', 'Hospitality', 'Retail', 'Manufacturing']

# List of job types
job_types = ['Full-time', 'Part-time', 'Contract', 'Freelance']

# Generate fake job listings
def generate_job_listings(num_listings):
    job_listings = []
    for _ in range(num_listings):
        title = fake.job()
        location = fake.city()
        industry = random.choice(industries)
        job_type = random.choice(job_types)
        job_listings.append((title, location, industry, job_type))
    return job_listings

# Function to search for job listings based on criteria
def search_job_listings(job_listings, location=None, industry=None, job_type=None):
    filtered_listings = []
    for job_listing in job_listings:
        if (not location or job_listing[1] == location) and \
           (not industry or job_listing[2] == industry) and \
           (not job_type or job_listing[3] == job_type):
            filtered_listings.append(job_listing)
    return filtered_listings

def main():
    # Generate fake job listings
    num_listings = 100
    job_listings = generate_job_listings(num_listings)

    # Prompt the user to enter search criteria
    location = input("Enter location (leave blank to skip): ")
    industry = input("Enter industry (leave blank to skip): ")
    job_type = input("Enter job type (leave blank to skip): ")

    # Filter job listings based on user input
    filtered_listings = search_job_listings(job_listings, location=location, industry=industry, job_type=job_type)

    # Print the filtered job listings
    print("Filtered Job Listings:")
    if filtered_listings:
        for job in filtered_listings:
            print(job)
    else:
        print("No job listings found matching the criteria.")

if __name__ == "__main__":
    main()
