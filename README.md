# Web Scraping on Reed Job Portal Website
This repository contains a Scrapy project aimed at scraping data analyst job listings from the Reed job portal (https://www.reed.co.uk). The project is designed to extract various details from job listings, including the job title, salary, contract type, job type, and location.

## To run this project:
 * Clone the repository to your local machine

## Set Up a Virtual Environment (Optional but recommended)
 * Command: python3 -m venv env(*env can be changed to your desired virtual environment name)

## Activate the Virtual Environment
 * On Windows: venv\Scripts\activate
 * On MacOS/Linux : source env/bin/activate
   
## Install Required Dependencies
 * Command: pip install scrap
   
## Run the Web Scraper
 * command: scrapy crawl Bim -o output.csv
