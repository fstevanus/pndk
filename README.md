# pndk
link shortener

## How to Test the URL Shortener Backend

1. **Clone the repository:**
   ```sh
   git clone https://github.com/fstevanus/pndk.git
   cd pndk
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the Swagger documentation:**
   Open your web browser and go to `http://127.0.0.1:8000/swagger/` to view the Swagger UI.

7. **Run the tests:**
   ```sh
   python manage.py test
   ```

## Setting up the Codespace Environment

1. **Open the repository in a Codespace:**
   - Go to the repository on GitHub.
   - Click on the "Code" button and select "Open with Codespaces".
   - If you don't have a Codespace created, click on "New codespace".

2. **Wait for the Codespace to initialize:**
   - The Codespace will automatically use the configuration in the `.devcontainer` directory to set up the development environment.

3. **Run the development server:**
   - Open a terminal in the Codespace.
   - Run the following command to start the development server:
     ```sh
     python manage.py runserver
     ```

4. **Access the application:**
   - Once the server is running, you can access the application by clicking on the "Ports" tab in the Codespace and opening the forwarded port.
