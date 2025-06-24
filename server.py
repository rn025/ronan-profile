from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def profile():
    return render_template_string('''
    <html>
    <head>
        <title>Ronan Bautista - Profile</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f2f5;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .profile-card {
                background-color: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                max-width: 600px;
                width: 100%;
            }
            h1 {
                margin-top: 0;
                color: #2c3e50;
            }
            p {
                margin: 8px 0;
                line-height: 1.5;
            }
        </style>
    </head>
    <body>
        <div class="profile-card">
            <h1>Ronan Bautista</h1>
            <p><strong>Student</strong></p>

            <h2>About Me</h2>
            <p>A freshman Computer Engineering student at EARIST, passionate about continuous learning and eager to grow in programming and technology.</p>

            <p><strong>Address:</strong> 636, Sampaloc, Manila</p>
            <p><strong>Birthdate:</strong> January 25, 2005</p>
            <p><strong>Status:</strong> Single</p>
            <p><strong>Height:</strong> 5'4</p>

            <h2>Academic</h2>
            <p><strong>School:</strong> Eulogio Amang Rodriguez Institute of Science and Technology</p>
            <p><strong>Program:</strong> BS Computer Engineering</p>

            <h2>Contact</h2>
            <p><strong>Email:</strong> bautistaronan0525@gmail.com</p>
        </div>
    </body>
    </html>
    ''')