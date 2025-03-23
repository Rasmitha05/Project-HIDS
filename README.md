# Project-HIDS

**Project-HIDS** is a Hybrid Intrusion Detection System that enhances security by combining multiple detection techniques, specifically anomaly-based and signature-based methods. This hybrid approach aims to improve the effectiveness of intrusion detection systems (IDS) by addressing the limitations inherent in individual methods, such as high false-positive rates and the inability to detect new attacks.

## 🌟 Features

- **Hybrid Detection Approach:** Integrates both signature-based and anomaly-based detection methods to provide comprehensive security coverage.
- **Machine Learning Integration:** Utilizes machine learning algorithms to enhance the detection of known and unknown threats.
- **Data Preprocessing:** Implements robust data preprocessing techniques to prepare datasets for effective model training and evaluation.
- **User-Friendly Interface:** Provides a web-based interface for easy interaction and monitoring of intrusion detection activities.

## 🛠️ Tech Stack

- **Programming Languages:** Python
- **Web Framework:** Flask
- **Machine Learning Libraries:** scikit-learn, pandas, numpy
- **Frontend:** HTML, CSS, JavaScript (via Flask templates)
- **Others:** Jupyter Notebook for data preprocessing and model training

## 🚀 Installation

To set up and run Project-HIDS locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rasmitha05/Project-HIDS.git
2. Navigate to the project directory:
   cd Project-HIDS
3. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
4. Install the required packages:
   pip install -r requirements.txt
5. Run the application:
   python app.py
The application should now be accessible at http://localhost:5000.

📌 Usage
Access the Web Interface: Open your web browser and navigate to http://localhost:5000.

Monitor Intrusions: Use the dashboard to monitor intrusion detection activities, view logs, and analyze alerts.

Data Analysis: Utilize the provided tools to analyze intrusion data and refine detection models.
