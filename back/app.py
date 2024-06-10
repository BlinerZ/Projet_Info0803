from typing import List, Dict
from flask import Flask, request, jsonify
import mysql.connector

CONFIG = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'mysql_db'
}
CONNECTION = mysql.connector.connect(**CONFIG)
CURSOR = CONNECTION.cursor()
print('Connexion DB OK')

app = Flask(__name__)

def get_contacts() -> List[Dict]:
    filters = request.args
    sql = 'SELECT * FROM contacts'
    conditions = []

    if 'prenom' in filters:
        conditions.append(f"firstname LIKE '%{filters['prenom']}%'")
    if 'nom' in filters:
        conditions.append(f"lastname LIKE '%{filters['nom']}%'")
    if 'email' in filters:
        conditions.append(f"email LIKE '%{filters['email']}%'")
    if 'entreprise' in filters:
        conditions.append(f"company LIKE '%{filters['entreprise']}%'")
    if 'region' in filters:
        conditions.append(f"region LIKE '%{filters['region']}%'")
    if 'tel' in filters:
        conditions.append(f"phone LIKE '%{filters['tel']}%'")
    if 'age_min' in filters:
        conditions.append(f"age >= {filters['age_min']}")
    if 'age_max' in filters:
        conditions.append(f"age <= {filters['age_max']}")
    if 'sexe' in filters:
        conditions.append(f"sex = '{filters['sexe']}'")

    if conditions:
        sql += ' WHERE ' + ' AND '.join(conditions)
        sql += ';'

    CURSOR.execute(sql)
    results = [{"id": id, "prenom": prenom, "nom": nom, "age": age, "sexe": sex, "email": email, "n tel": tel, 'entreprise': company, 'region': region} for (id, prenom, nom, age, sex, email, tel, company, region) in CURSOR.fetchall()]
    return results


@app.route('/api/contacts', methods=['GET', 'POST'])
def contacts():
    if request.method == 'GET':
        return jsonify(get_contacts())
    elif request.method == 'POST':
        contact_id = request.form.get('id')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        sex = request.form.get('sex')
        age = request.form.get('age')
        email = request.form.get('email')
        phone = request.form.get('phone')
        company = request.form.get('company')
        region = request.form.get('region')

        if contact_id == '0':
            CURSOR.execute(
                'INSERT INTO contacts (firstname, lastname, age, sex, email, phone, company, region) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (firstname, lastname, age, sex, email, phone, company, region)
            )
        else:
            CURSOR.execute(
                'UPDATE contacts SET firstname = %s, lastname = %s, age = %s, sex = %s, email = %s, phone = %s, company = %s, region = %s WHERE id = %s',
                (firstname, lastname, age, sex, email, phone, company, region, contact_id)
            )

        CONNECTION.commit()
        return jsonify({'message': 'Contact saved'})


@app.route('/api/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    CURSOR.execute('DELETE FROM contacts WHERE id = %s', (id,))
    CONNECTION.commit()
    return jsonify({'message': 'Contact deleted'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
