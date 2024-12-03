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

## Testing with MQTT Explorer

If the provided input and output topics with mqtt topic id from winter supplement app do not work, you can use MQTT Explorer to test the application. Follow these steps:

1. **Install MQTT Explorer**

- Download and install [MQTT Explorer](https://mqtt-explorer.com/).

2. **Create Custom Topics**  
   In MQTT Explorer, enter host `test.mosquitto.org` and port number `1883`, then create custom input and output topics:

   - **Input Topic:** `hamza/test/mqtt/input`
   - **Output Topic:** `hamza/test/mqtt/output`

3. **Test the Application**

   1. **Start the Application:**  
      Run the code with these values already implemented in the code:

      ```bash
      input_topic = "hamza/test/mqtt/input"
      output_topic = "hamza/test/mqtt/output"
      ```

   2. **Publish Test Input in JSON format**  
      In MQTT Explorer, publish a message to the input topic `hamza/test/mqtt/input`:

      ```bash
      {
         "id": "59974c0c-b458-4421-875c-a37915448b0b",
         "familyComposition": "single",
         "numberOfChildren": 2,
         "familyUnitInPayForDecember": true
      }
      ```

   3. **Check Output**  
      Check the output topic for the output data:  
      **Expected Output:**

      ```bash
      {
         "id": "59974c0c-b458-4421-875c-a37915448b0b",
         "isEligible": true,
         "baseAmount": 120.0,
         "childrenAmount": 40.0,
         "supplementAmount": 160.0
      }
      ```

---

By following testing steps, you can test and verify the application's functionality when the winter supplement app topics don't work.
