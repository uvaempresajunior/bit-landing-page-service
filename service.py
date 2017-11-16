#!/usr/bin/env python3

import json
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask('bit_service_subscriptions')
CORS(app)

@app.route('/api/subscriptions', methods=['POST'])
def subscription():
    nome = request.form.get('nome')
    curso = request.form.get('curso')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    matricula = request.form.get('matricula')

    server  = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('email@email.com', 'senha')

    msg = MIMEMultipart()
    msg['from'] = 'email@email.com'
    msg['to'] = email
    msg['subject'] = 'Inscrição no BIT'

    body = '''
            <html>
                <body>
                    Olá %s,
                    <br/>
                    <p>
                        Inscrição para o BIT confirmada ;)
                    </p>
                </body>
            </html>
            ''' % nome
    msg.attach(MIMEText(body, 'html'))
    
    text = msg.as_string()
    server.sendmail('email@email.com', email, text)
    server.quit()

    retorno = [{'msg': 'ok'}]
    return jsonify(retorno=retorno, total=len(retorno))

app.run(debug=True, use_reloader=True)