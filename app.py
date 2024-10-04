from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'abnerck9@gmail.com'  # Cambia esto por tu correo
app.config['MAIL_PASSWORD'] = 'viig xfjk xomv thzt'  # Cambia esto por tu contraseña
app.config['MAIL_DEFAULT_SENDER'] = 'abnerck9@gmail.com'  # Cambia esto por tu correo
mail = Mail(app)

@app.route('/')
def layout():
    return render_template('layout.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ubicacion')
def located():
    return render_template('ubicacion.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/reuniones')
def meetings():
    return render_template('meetings.html')

@app.route('/totlip')  # Ruta para la página de reuniones
def nos_reunimos():
    return render_template('totlip.html')  # Cambia el nombre si es diferente

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        subject = request.form.get('subject')

        # Crear el mensaje
        msg = Message('Nuevo Contacto', recipients=['abnerck9@gmail.com'])  # Cambia por el destinatario deseado
        msg.body = f'Nombre: {name}\nTeléfono: {phone}\nAsunto: {subject}'
        
        # Enviar el correo
        mail.send(msg)

        return render_template('contact.html', success=True)  # Página de éxito después de enviar el correo
    
    return render_template('contact.html')  # Página de formulario

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
