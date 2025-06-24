from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

@app.route('/image/<filename>')
def image(filename):
    return send_from_directory(os.getcwd(), filename)

@app.route('/')
def profile():
    return render_template_string('''
    <html>
    <head>
        <title>Ronan Bautista - Profile</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #0b1d3a;
                color: #ffffff;
                margin: 0;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .profile-card {
                background-color: #13294b;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                max-width: 600px;
                width: 100%;
                text-align: center;
            }
            .profile-card img {
                width: 150px;
                height: 150px;
                border-radius: 10px;
                object-fit: cover;
                margin-bottom: 20px;
                border: 2px solid #ffffff;
            }
            h1, h2 {
                color: #4db8ff;
                margin-top: 0;
            }
            p {
                margin: 8px 0;
                line-height: 1.5;
            }
        </style>
    </head>
    <body>
        <div class="profile-card">
            <img src="/image/ronan.jpg" alt="Ronan Bautista">
            <h1>Ronan Bautista</h1>
            <p><strong>Student</strong></p>

            <h2>About Me</h2>
            
            <p>A freshman Computer Engineering student at EARIST, passionate about continuous learning and eager to grow in programming and technology.</p>
            
            <h2>Personal Background</2>
            
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