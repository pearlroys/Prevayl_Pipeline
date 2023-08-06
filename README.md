# Prevayl_Pipeline
**Project README - Scraping and Automating Prevayl Website Data**

# Project Overview

In this project, I undertook the task of scraping data from the Prevayl website, a medical fitness company that helps track the vitals of users while exercising. The data scraping process was carried out using the Scrapy web scraping framework and Beautiful Soup for parsing the web content. The primary goal was to collect valuable exercise-related data from the website, which would later be processed, transformed, and stored for further analysis.
<img width="1223" alt="Screenshot 2023-08-06 at 14 08 46" src="https://github.com/pearlroys/prevayl_pipeline/assets/103274172/e754e0b0-8f1f-41c5-ad40-446a907c5396">

# Data Scraping Process

## 1. Technologies Used

- Scrapy: A powerful Python web scraping framework that allows us to extract data from websites easily.
- Beautiful Soup: A Python library for pulling data out of HTML and XML files.
- Pandas: Used for data manipulation and transformation.
- Apache Airflow: A platform to programmatically author, schedule, and monitor workflows.
- Docker: Utilized to create a containerized environment for seamless deployment and scaling.
- AWS S3: The chosen cloud storage service for storing the scraped data.

## 2. Web Scraping Procedure

- Identified the target website's structure and relevant data points to be extracted.
- Developed custom Scrapy spiders to crawl through the website and collect the desired information efficiently.
- Utilized Beautiful Soup to parse the HTML content and extract specific data elements.
- 
- <img width="874" alt="Screenshot 2023-08-06 at 14 09 40" src="https://github.com/pearlroys/prevayl_pipeline/assets/103274172/e0b50837-f8c2-413b-9f16-1738d1b1ce92">


## 3. Handling Errors and Challenges

Throughout the data scraping process, I encountered several challenges and bugs that hindered smooth execution. However, an excellent programmer knows that encountering bugs is part of the development process and the key lies in resolving them effectively.

**Bugs Encountered:**

- **CPU Usage**: Initially, I faced issues with high CPU usage when running the Scrapy spiders. The website's large size and complexity contributed to this problem. To mitigate this, I implemented optimizations in the code, such as limiting the number of concurrent requests and adding delays between requests.

- **AWS S3 Access**: During the development of the data pipeline, I overlooked granting the necessary IAM role access to the S3 bucket. Consequently, the data upload to the S3 bucket via Airflow DAGs failed. Upon identification, I quickly rectified this by configuring the IAM role to permit the required actions, enabling smooth data transfer to the S3 bucket.
- <img width="1358" alt="Screenshot 2023-07-28 at 08 18 08" src="https://github.com/pearlroys/prevayl_pipeline/assets/103274172/eb7630b5-3792-4517-8e07-e2e163fa99d6">

<img width="1399" alt="Screenshot 2023-07-28 at 08 28 44" src="https://github.com/pearlroys/prevayl_pipeline/assets/103274172/2da23eec-7753-4bf3-aba7-f1fcf46b6cf1">
<img width="821" alt="Screenshot 2023-08-06 at 14 15 09" src="https://github.com/pearlroys/prevayl_pipeline/assets/103274172/6e7e8582-426f-4958-a1fb-3e173423784c">

# Data Pipeline and Automation

## 1. Airflow DAGs

To automate the scraping process and ensure daily updates of the data, I created Airflow DAGs (Directed Acyclic Graphs). Airflow allowed me to schedule and manage the entire data scraping and transformation workflow efficiently.

<img width="1414" alt="Screenshot 2023-07-28 at 08 30 34" src="https://github.com/pearlroys/prevayl_pipeline/assets/103274172/c6a52451-b0f5-4f50-af3b-c6e4f308ece2">
## 2. Data Conversion and Storage

- After extracting data using Scrapy and Beautiful Soup, I processed and transformed it into CSV format.
- Using Pandas, I converted the CSV data into a DataFrame, making it easier to handle and analyze the information.
- Finally, I automated the process of uploading the DataFrame to an AWS S3 bucket through the Airflow DAGs.
<img width="964" alt="Screenshot 2023-07-28 at 08 31 53" src="https://github.com/pearlroys/prevayl_pipeline/assets/103274172/011afe44-70a8-4a2e-bfd6-270337d0a6e4">
## 3. Daily Automation

The Airflow DAGs were configured to execute the entire data pipeline daily, ensuring that the latest data was scraped, processed, transformed, and uploaded to the S3 bucket regularly.

<img width="1031" alt="Screenshot 2023-08-06 at 14 16 45" src="https://github.com/pearlroys/prevayl_pipeline/assets/103274172/f1a8f4e3-fe9a-48c9-8a00-c929514cfc74">
## Improvements

- **Docker Image**: To enhance portability and ease of deployment, the project can be containerized using Docker. Creating a Docker image of the application ensures consistent behavior across different environments.

- **Additional DAGs**: As the project evolves, additional Airflow DAGs can be created to include more scraping tasks or implement other data processing and analysis steps.

- **PEP 8 Guidelines**: Throughout the development process, I adhered to PEP 8 guidelines to ensure consistent and readable code, promoting better collaboration and maintainability.

- **Virtual Environment**: To manage dependencies efficiently, I created a virtual environment to isolate project-specific packages, ensuring a clean and well-organized development environment.

- **AWS Installation Guide**: While installing Apache Airflow on the AWS free tier presented some challenges, I found a helpful guide on "Moderndataengineering" (https://moderndataengineering.substack.com/p/installing-apache-airflow-on-aws) that eased the installation process and helped set up the environment effectively.

# Conclusion

In conclusion, this project showcases the power of web scraping with Scrapy and Beautiful Soup to collect valuable data from the Prevayl website. Moreover, implementing Airflow DAGs provided seamless automation and daily updates of the data pipeline. Despite encountering various bugs and challenges, I successfully overcame them, demonstrating the skills of a seasoned programmer who is capable of identifying and resolving issues efficiently.

As the project continues to run daily, it will continuously accumulate valuable data that can be used for further analysis, insights, and decision-making in the field of medical fitness and exercise tracking. The project's improvements, such as Dockerization and additional DAGs, offer scalability and future expansion potential for enhanced data processing and utilization.
