from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login-code', methods=['POST'])
def login_code():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # طباعة البيانات المستلمة في التيرمنال
    print(f"\n=== محاولة تسجيل دخول ===")
    print(f"UserName is  : {username}")
    print(f"Passowrd is :{password}")
    print("==========================\n")

    return jsonify({"message": "تم استلام البيانات"}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
