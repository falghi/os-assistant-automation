# OS Assistant Automation

## Table of Contents
- [Requirements](#requirements)
- [Prerequisites](#prerequisites)
- [Usage](#usage)


## Requirements

Listed in requirements.txt. Another additional requirement for the selenium browser to run is the Chromium WebDriver which can be downloaded from the [official website](https://chromedriver.chromium.org/downloads).

## Prerequisites

1. Create a python virtual environment anywhere in the system using the command:
    ```bash
    python -m venv env
    ```
    It will create a virtual environment folder named `env` on the current working directory where you executed the command.

2. Activate the virtual environment:
    - For Windows systems
        ```
        env\Scripts\activate
        ```
    - For Linux / macOS systems
        ```bash
        source env/bin/activate
        ```

3. Install the required dependencies using:
    ```
    pip install -r requirements.txt
    ```

4. Download the Chromium WebDriver [here](https://chromedriver.chromium.org/downloads), place it anywhere in the system, and add the location to the system's environment variables' path).

5. Change the contents of `asdosan.txt` to the github usernames you want to check.

6. Change the `os_repo` variable to the desired repository to check and `os_week` variable to the current week in the `koreksi.py` file.

    Example:
    ```python
    os_repo = 'os211'
    os_week = 'W03'
    ```

## Usage

Before you run the program make sure that the virtual environment is activated. After that use the following command to start checking:
```bash
python koreksi.py
```
