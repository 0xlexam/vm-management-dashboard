import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

class VMStatus(Enum):
    RUNNING = "running"
    STOPPED = "stopped"
    SUSPENDED = "suspended"
    DELETED = "deleted"

class VirtualMachine:
    def __init__(self, vm_id, vm_name, cpu_cores, memory_gb, storage_gb, status):
        self.id = vm_id
        self.name = vm_name
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb
        self.storage_gb = storage_gb
        self.status = VMStatus(status)

    def set_status(self, new_status):
        self.status = VMStatus(new_status)

    def __str__(self):
        return f"VM {self.id}: {self.name}, Status: {self.status.name}"

class VirtualMachineManager:
    def __init__(self):
        self.virtual_machines = {}

    def add_virtual_machine(self, vm_id, vm_name, cpu_cores, memory_gb, storage_gb, status=VMStatus.STOPPED):
        if vm_id in self.virtual_machines:
            raise ValueError(f"VM with ID {vm_id} already exists.")
        self.virtual_machines[vm_id] = VirtualMachine(vm_id, vm_name, cpu_cores, memory_gb, storage_gb, status)

    def remove_virtual_machine(self, vm_id):
        if vm_id in self.virtual_machines:
            del self.virtual_machines[vm_id]
        else:
            raise ValueError(f"No VM with ID {vm_id} found.")

    def fetch_vm_status(self, vm_id):
        if vm_id in self.virtual_machines:
            return self.virtual_machines[vm_id].status
        else:
            raise ValueError(f"No VM with ID {vm_id} found.")

    def change_vm_status(self, vm_id, new_status):
        if vm_id in self.virtual_machines:
            self.virtual_machines[vm_id].set_status(new_status)
        else:
            raise ValueError(f"No VM with ID {vm_id} found.")

    def display_vm_list(self):
        return [str(vm) for vm_id, vm in self.virtual_machines.items()]