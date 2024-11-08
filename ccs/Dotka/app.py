import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

folders = {
    'folder1': 'static/folder1/text1.txt',
    'folder2': 'static/folder2/text2.txt',
    'folder3': 'static/folder3/text3.txt',
}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_text')
def get_text():
    folder = request.args.get('folder')
    
    if folder in folders:
        try:
            with open(folders[folder], 'r') as f:
                return f.read()
        except Exception as e:
            return "Error reading file."
    return "Invalid folder."

@app.route('/user', methods=['POST'])
def get_user_info():
    try:
        data = request.json
        user_id = data.get('user_id')
        file_path = data.get('file_path', None)

        users = {
            1: {"id": 1, "name": "Alice"},
            2: {"id": 2, "name": "Bob"}
        }

        if user_id in users:
            response = {
                "status": "success",
                "data": users[user_id]
            }

            if file_path:
                full_path = os.path.join(os.getcwd(), file_path)
                
                if os.path.exists(full_path):
                    with open(full_path, 'r') as f:
                        file_content = f.read()
                    response["file_content"] = file_content
                else:
                    response["file_content"] = "File not found."
        else:
            response = {
                "status": "error",
                "message": "User ID not found."
            }

        return jsonify(response)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8989)
