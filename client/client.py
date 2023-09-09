import requests
import json

server_url = "http://your-server-ip:8080"  # Replace with your server's IP and port

def send_command(command):
    payload = {'command': command}
        headers = {'Content-Type': 'application/json'}
        
            response = requests.post(f"{server_url}/command", data=json.dumps(payload), headers=headers)
            
                if response.status_code == 200:
                        result = response.json()
                                return result
                                    else:
                                            return {'error': 'Command failed'}
                                            
                                            if __name__ == '__main__':
                                                command_to_send = "Example command"
                                                    response = send_command(command_to_send)
                                                        print(response)
                                                                                         ok