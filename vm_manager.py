import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)

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

    @abstractmethod
    def restart_vm(self, vm_id):
        pass

class MyVmManager(VmManager):

    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.api_url = os.getenv('API_URL')

    def start_vm(self, vm_id):
        logging.info(f"Starting VM with ID: {vm_id}")
        
    def stop_vm(self, vm_id):
        logging.info(f"Stopping VM with ID: {vm_id}")
        
    def get_vm_status(self, vm_id):
        logging.info(f"Getting status for VM with ID: {vm_id}")
        return "running"  

    def restart_vm(self, vm_id):
        if self.get_vm_status(vm_id) != "stopped":  
            self.stop_vm(vm_id)
        self.start_vm(vm_id)
        logging.info(f"Restarted VM with ID: {vm_id}")

if __name__ == "__main__":
    vm_manager = MyVmManager()

    vm_id = "12345"

    vm_manager.restart_vm(vm_id)

    status = vm_manager.get_vm_status(vm_id)
    logging.info(f"VM Status: {status}")

    vm_manager.stop_vm(vm_id)