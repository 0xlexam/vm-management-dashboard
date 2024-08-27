from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.before_request
def before_request_func():
    print("This is executed before each request.")

@app.route('/vms', methods=['GET'])
def list_vms():
    return jsonify({"message": "List of VMs", "vms": []})

@app.route('/vms', methods=['POST'])
def create_vm():
    vm_data = request.json
    return jsonify({"message": "VM created", "data": vm_data}), 201

@app.route('/vms/<string:vm_id>', methods=['GET'])
def get_vm(vm_id):
    return jsonify({"message": "VM details", "vm_id": vm_id})

@app.route('/vms/<string:vm_id>', methods=['PUT'])
def update_vm(vm_id):
    update_data = request.json
    return jsonify({"message": "VM updated", "vm_id": vm_id, "update_data": update_data})

@app.route('/vms/<string:vm_id>', methods=['DELETE'])
def delete_vm(vm_id):
    return jsonify({"message": "VM deleted", "vm_id": vm_id})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("PORT", 5000))