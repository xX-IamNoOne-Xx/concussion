from flask import Flask, request

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def receive_command():
    data = request.get_json()
        # Process the command and return a response
            return {'response': 'Command received and processed'}

            if __name__ == '__main__':
                app.run(host='0.0.0.0', port=8080)
                l