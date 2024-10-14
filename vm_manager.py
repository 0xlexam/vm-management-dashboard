import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod

load_dotenv()

class VmManager(ABC):

    @abstractmethod
    def start_vm(self, vm_id):
        pass

    @abstractmethod
    def stop_vm(self, vm_id):
        pass

    @abstractmethod
    def get_vm_status(self, vm_id):
        pass

class MyVmManager(VmManager):

    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.api_url = os.getenv('API_URL')

    def start_vm(self, vm_id):
        print(f"Starting VM with ID: {vm_id}")
        return True

    def stop_vm(self, vm_id):
        print(f"Stopping VM with ID: {vm_id}")
        return True

    def get_vm_status(self, vm_id):
        print(f"Getting status for VM with ID: {vm_id}")
        return "running"

if __name__ == "__main__":
    vm_manager = MyVmManager()

    vm_id = "12345"

    vm_manager.start_vm(vm_id)

    status = vm_manager.get_vm_status(vm_id)
    print(f"VM Status: {status}")

    vm_manager.stop_vm(vm_id)