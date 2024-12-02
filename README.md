# Winter-Supplement-Rules-Engine

## Description

This project is aimed to communicate with the Winter Supplement web application to receive input data, processes the data to calculate eligibility and amounts, and publishes the output data to the MQTT output topic.

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

   Setting up a virtual environment ensures the dependencies are separated from the main Python setup on computer.

   - on **Windows**

   ```bash
   python -m venv venv
   ```

   - on **macOS**

   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**

   Activate the virtual environment to use the dependencies.

   - on **Windows**

   ```bash
   .\venv\Scripts\activate
   ```

   - on **macOS**

   ```bash
   source venv/bin/activate
   ```

5. **Install dependencies:**

   Install the required Python libraries.

   ```bash
   pip install -r requirements.txt
   ```

6. **Replace `mqtt_topic_id`:**

   Edit `main.py` to set the `mqtt_topic_id` variable (line 11) with the correct MQTT topic ID provided by the Winter Supplement Calculator.

7. **Run the application`**

   Start the project by running the `main.py` file.

   ```bash
   python main.py
   ```

8. **Check the Integration**

   Use the Winter Supplement Calculator to send input data to the specified MQTT topic. The application will process the data and publish the output to the designated MQTT output topic.

9. **Unit Test**  
   To validate if eligibility functionality is working properly, run the following command in your terminal.
   ```bash
   python -m unittest discover
   ```
   This command will discover and execute all unit tests.

---

By following this guide, you can set up, run, and test the Winter Supplement Rules Engine project.
