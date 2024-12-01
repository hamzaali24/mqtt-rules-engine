# Winter-Supplement-Rules-Engine

## Description
This project is aimed to communicate with the Winter Supplement web application to receive input data, processes the data, and publishes the output data to the MQTT output topic.

## Prerequisites

Ensure you have the following installed:
- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [VS Code](https://code.visualstudio.com/download) (Recommended IDE)

## Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the repository:**
   Clone the repository to your local machine using Git.

   ```bash
   git clone https://github.com/hamzaali24/mqtt-rules-engine.git
   ```

2. **Navigate to the project folder:**
    ```bash
    cd <project-folder>
    ```

3. **Optional: Create a virtual environment:**
    - on **Windows**
    ```bash
    python -m venv venv
    ```

    - on **macOS**
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment:**
    - on **Windows**
    ```bash
    .\venv\Scripts\activate
    ```
    - on **macOS**
    ```bash
    source venv/bin/activate
    ```

5. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
