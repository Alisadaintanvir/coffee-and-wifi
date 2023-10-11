# Cafe Information App

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview

The Cafe Information App is a Flask-based web application that allows users to submit and view cafe information, including the cafe name, location, opening and closing times, ratings, WiFi strength, and power socket availability. Users can add new cafes, and the information is stored in a CSV file for easy access.

## Prerequisites

Before you get started, ensure you have the following dependencies installed:

- Python 3
- Flask
- Flask-WTF
- Flask-Bootstrap

## Installation

1. Clone the repository to your local machine:

   `git clone https://github.com/yourusername/yourproject.git`
   
2. Change into the project directory:
     `cd coffee-and-wifi`

3. Create a virtual environment (recommended):
    `python -m venv venv`

4. Activate the virtual environment:
     -On Windows:
       `venv\Scripts\activate`
     - On macOS and Linux:
       `source venv/bin/activate`

5. Install the required packages:
    `pip install -r requirements.txt`

6. Run the Flask application:
     `flask run`

## Usage

1. Access the web application by navigating to http://localhost:5000/ in your web browser.

2. On the homepage, you can view the list of cafes submitted by users.

3. Click on the "Add a Cafe" link to submit cafe information. Fill in the required fields and click the "Submit" button.

4. Your cafe information will be added to the list of cafes and saved in a CSV file.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize this README to include additional information or details about your project.


