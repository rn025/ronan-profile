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
            }
            .section-title {
                border-left: 5px solid #4db8ff;
                padding-left: 10px;
                margin-top: 25px;
                font-size: 20px;
                color: #4db8ff;
            }
            h1.name {
                border-left: 8px solid #4db8ff;
                padding-left: 12px;
                color: #4db8ff;
            }
            p {
                margin: 8px 0;
                line-height: 1.5;
            }
        </style>
    </head>
    <body>
        <div class="profile-card">
            <h1 class="name">Ronan Bautista</h1>
            <p><strong>Student</strong></p>

            <div class="section-title">About Me</div>
            
            <p>A freshman Computer Engineering student at EARIST, passionate about continuous learning and eager to grow in programming and technology.</p>

            <div class="section-title">Personal Background</div>
            
            <p><strong>Address:</strong> 636, Sampaloc, Manila</p>
            <p><strong>Birthdate:</strong> January 25, 2005</p>
            <p><strong>Status:</strong> Single</p>
            <p><strong>Height:</strong> 5'4</p>

            <div class="section-title">Academic</div>
            
            <p><strong>School:</strong> Eulogio Amang Rodriguez Institute of Science and Technology</p>
            <p><strong>Program:</strong> BS Computer Engineering</p>

            <div class="section-title">Contact</div>
            
            <p><strong>Email:</strong> bautistaronan0525@gmail.com</p>
        </div>
    </body>
    </html>
    ''')