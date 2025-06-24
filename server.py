from flask import Flask, render_template_string, send_file

app = Flask(__name__)
# Force push for Render redeploy
@app.route('/')
def home():
    return render_template_string('''
        <h1>Ronan Bautista</h1>
        <p><strong>Student</strong></p>

        <h3>About Me</h3>
        <p>A freshman Computer Engineering student at EARIST, passionate about continuous learning and eager to grow in programming and technology.</p>

        <p><strong>Address:</strong> 636, Sampaloc, Manila.</p>
        <p><strong>Birthdate:</strong> January 25, 2005</p>
        <p><strong>Status:</strong> Single</p>
        <p><strong>Height:</strong> 5'4</p>
        <p><strong>School:</strong> Eulogio Amang Rodriguez Institute of Science and Technology</p>
        <p><strong>Program:</strong> BS Computer Engineering</p>

        <h3>Contact</h3>
        <p>Email: bautistaronan0525@gmail.com</p>

        <br>
        <a href="/download">⬇️ Download My Profile App (.exe)</a>
    ''')

@app.route('/download')
def download():
    return send_file("ronan_pf.exe", as_attachment=True)

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000)