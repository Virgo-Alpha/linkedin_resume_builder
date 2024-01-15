# LinkedIn Resume Builder

This project empowers you to craft a polished resume using your LinkedIn profile. The cornerstone of this tool is the `builder.py` script, a Streamlit application. The following overview provides clear instructions on installing and utilizing the LinkedIn Resume Builder.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/LinkedIn-Resume-Builder.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd LinkedIn-Resume-Builder
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit application:**
    ```bash
    streamlit run builder.py
    ```

The application will prompt you to enter your LinkedIn credentials and profile URL. After providing the required information, click the "Generate Resume" button. The script will scrape your LinkedIn profile, create a resume in Microsoft Word format (.docx), and provide a download link.

Note: Ensure that you have the necessary dependencies installed and that the ChromeDriver executable is in your system's PATH.

Feel free to customize and enhance the project based on your specific needs. Happy resume building!