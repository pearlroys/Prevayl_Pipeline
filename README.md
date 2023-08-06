# Prevayl_Pipeline
**Project README - Scraping and Automating Prevayl Website Data**

# Project Overview

In this project, I undertook the task of scraping data from the Prevayl website, a medical fitness company that helps track the vitals of users while exercising. The data scraping process was carried out using the Scrapy web scraping framework and Beautiful Soup for parsing the web content. The primary goal was to collect valuable exercise-related data from the website, which would later be processed, transformed, and stored for further analysis.

# Data Scraping Process

## 1. Technologies Used

- Scrapy: A powerful Python web scraping framework that allows us to extract data from websites easily.
- Beautiful Soup: A Python library for pulling data out of HTML and XML files.
- Pandas: Used for data manipulation and transformation.
- AWS S3: The chosen cloud storage service for storing the scraped data.

## 2. Web Scraping Procedure

- Identified the target website's structure and relevant data points to be extracted.
- Developed custom Scrapy spiders to crawl through the website and collect the desired information efficiently.
- Utilized Beautiful Soup to parse the HTML content and extract specific data elements.

## 3. Handling Errors and Challenges

Throughout the data scraping process, I encountered several challenges and bugs that hindered smooth execution. However, an excellent programmer knows that encountering bugs is part of the development process and the key lies in resolving them effectively.

**Bugs Encountered:**

- **CPU Usage**: Initially, I faced issues with high CPU usage when running the Scrapy spiders. The website's large size and complexity contributed to this problem. To mitigate this, I implemented optimizations in the code, such as limiting the number of concurrent requests and adding delays between requests.

- **AWS S3 Access**: During the development of the data pipeline, I overlooked granting the necessary IAM role access to the S3 bucket. Consequently, the data upload to the S3 bucket via Airflow DAGs failed. Upon identification, I quickly rectified this by configuring the IAM role to permit the required actions, enabling smooth data transfer to the S3 bucket.

# Data Pipeline and Automation

## 1. Airflow DAGs

To automate the scraping process and ensure daily updates of the data, I created Airflow DAGs (Directed Acyclic Graphs). Airflow allowed me to schedule and manage the entire data scraping and transformation workflow efficiently.

## 2. Data Conversion and Storage

- After extracting data using Scrapy and Beautiful Soup, I processed and transformed it into CSV format.
- Using Pandas, I converted the CSV data into a DataFrame, making it easier to handle and analyze the information.
- Finally, I automated the process of uploading the DataFrame to an AWS S3 bucket through the Airflow DAGs.

## 3. Daily Automation

The Airflow DAGs were configured to execute the entire data pipeline daily, ensuring that the latest data was scraped, processed, transformed, and uploaded to the S3 bucket regularly.

# Conclusion

In conclusion, this project showcases the power of web scraping with Scrapy and Beautiful Soup to collect valuable data from the Prevayl website. Moreover, implementing Airflow DAGs provided seamless automation and daily updates of the data pipeline. Despite encountering various bugs and challenges, I successfully overcame them, demonstrating the skills of a seasoned programmer who is capable of identifying and resolving issues efficiently.

As the project continues to run daily, it will continuously accumulate valuable data that can be used for further analysis, insights, and decision-making in the field of medical fitness and exercise tracking.
