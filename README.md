# SDT_Project
 Software Development Tools: Project
https://car-sales-analysis.onrender.com/

## Project Description
This project analyzes a dataset of used cars and visualizes the data using a Streamlit web application. The goal is to provide insights into the used car market, including price distributions, the relationship between price and odometer readings, and the impact of car model year on price.

## Installation Instructions
To run this project locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
2. **Create and activate a virtual environment:**
    python -m venv myenv
    source myenv/bin/activate # On Windows use `myenv\Scripts\Activate`
3. Install the required packages:
    pip install -r requirements.txt
4. Run the Streamlit app:
    streamlit run app.py


## Usage
Once the app is running, you can access it in your browser at http://localhost:8501. The app provides several visualizations to explore the car sales data.

## Project Structure
app.py: The main Streamlit application.
notebooks/EDA.ipynb: The Jupyter notebook for exploratory data analysis.
requirements.txt: List of required Python packages.
vehicles_us.csv: The dataset used in the project.
.streamlit/config.toml: Configuration file for Streamlit.