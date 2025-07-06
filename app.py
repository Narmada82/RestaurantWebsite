from flask import Flask, render_template, request, flash, redirect, url_for
from sqlalchemy import create_engine, text

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Database connection
DATABASE_URL = "postgresql+psycopg2://neondb_owner:npg_OFgDGMz0L8QE@ep-curly-glitter-a84a9h5j-pooler.eastus2.azure.neon.tech/neondb?sslmode=require&channel_binding=require"
engine = create_engine(DATABASE_URL)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    # Static sample projects (if no DB needed)
    projects_data = [
        {
            'title': 'Task Management System',
            'description': 'A web-based task manager with user authentication and real-time updates.',
            'tech_stack': ['Python', 'Flask', 'SQLite', 'HTML/CSS', 'JavaScript'],
            'github': 'https://github.com/Narmada82/task-manager',
            'demo': '#'
        },
        {
            'title': 'Weather Forecast App',
            'description': 'Real-time weather application using OpenWeatherMap API with location detection.',
            'tech_stack': ['JavaScript', 'HTML/CSS', 'REST API', 'Bootstrap'],
            'github': 'https://github.com/narmada/weather-app',
            'demo': '#'
        },
        {
            'title': 'Student Grade Calculator',
            'description': 'Desktop application for calculating CGPA and semester grades with data visualization.',
            'tech_stack': ['Python', 'Tkinter', 'Matplotlib', 'Pandas'],
            'github': 'https://github.com/narmada/grade-calculator',
            'demo': '#'
        },
        {
            'title': 'E-commerce Landing Page',
            'description': 'Responsive e-commerce template with modern design and mobile optimization.',
            'tech_stack': ['HTML', 'CSS', 'JavaScript', 'Bootstrap'],
            'github': 'https://github.com/narmada/ecommerce-template',
            'demo': '#'
        }
    ]
    return render_template('projects.html', projects=projects_data)

@app.route('/db-projects')
def db_projects():
    # Example fetching projects from a database table named 'projects'
    with engine.connect() as connection:
        result = connection.execute(text("SELECT title, description FROM projects"))
        projects = [{'title': row.title, 'description': row.description} for row in result]
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Example of inserting into a table called 'messages' (make sure it exists)
        with engine.connect() as connection:
            insert_stmt = text("INSERT INTO messages (name, email, message) VALUES (:name, :email, :message)")
            connection.execute(insert_stmt, {"name": name, "email": email, "message": message})

        flash(f'Thank you {name}! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
