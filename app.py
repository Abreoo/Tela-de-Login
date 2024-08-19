import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = str(os.getenv('SECRET_KEY'))

# Configuração do banco de dados (SQLite como exemplo)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de Usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')


        # Verifica se o usuário já existe
        existing_user = Usuario.query.filter_by(username=username).first()
        if existing_user:
            flash('Nome de usuário já existe. Tente outro.', 'danger')
            return redirect(url_for('register'))

        new_user = Usuario(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Usuário registrado com sucesso!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Rota para a tela de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id  # Armazena o ID do usuário na sessão
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Nome de usuário ou senha incorretos.', 'danger')

    return render_template('login.html')

# Rota para o dashboard após o login
@app.route('/dashboard')
def dashboard():
    # Verifique se o usuário está logado
    if 'user_id' not in session:
        flash('Você precisa fazer login primeiro.', 'danger')
        return redirect(url_for('login'))
    
    user = Usuario.query.get(session['user_id'])
    return render_template('dashboard.html', username=user.username)

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove o usuário da sessão
    flash('Você foi desconectado com sucesso.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Garantir que o contexto da aplicação está ativo
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    
    app.run(debug=True)
