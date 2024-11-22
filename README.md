# Azurro-task

Installation process:

1. Clone the repository using `git clone <repository-url>` and navigate to the project directory using `cd azurro-task`.  
2. Create a virtual environment with `python -m venv venv`.  
3. Activate the virtual environment using `source venv/bin/activate` for macOS/Linux or `venv\Scripts\activate` for Windows.  
4. Install the dependencies with `pip install -r requirements.txt`.  
5. Apply database migrations using `python manage.py makemigrations` and then `python manage.py migrate`.  
6. Start the development server with `python manage.py runserver`.  
7. Open your browser and navigate to `http://127.0.0.1:8000/` to access the application.  
