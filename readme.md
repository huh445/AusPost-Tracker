# Package Tracker Application

## Overview

This application allows you to track packages using the 17track API. It provides a user-friendly interface to enter tracking numbers, fetch tracking details, and display the results. The application is built using Python and Tkinter for the GUI.

## Features

- Enter multiple tracking numbers (comma-separated) to track.
- Fetch tracking details from the 17track API.
- Display tracking status and carrier information.
- Handles carrier code validation and error responses.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/package-tracker.git
    cd package-tracker
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**

    You need to set the `API_KEY` environment variable with your 17track API key.

    On Linux/macOS:

    ```bash
    export API_KEY='your_api_key'
    ```

    On Windows:

    ```bash
    set API_KEY='your_api_key'
    ```

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Enter tracking numbers:**

    - Open the application.
    - Enter tracking numbers separated by commas into the input field.
    - Click the "Track" button to fetch tracking information.

3. **View results:**

    The tracking details will be displayed in the results section of the application. You can see the tracking number, carrier name, and current status.

## Contributing

Feel free to open issues or submit pull requests. If you have suggestions or improvements, please share them!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
