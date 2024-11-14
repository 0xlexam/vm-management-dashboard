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
    def __init__(self, id, name, cpu_cores, memory_gb, disk_gb, status):
        self.id = id
        self.name = name
        self.cpu_cores = cpu_cores
        self.memory_gb = memory_gb
        self.disk_gb = disk_gb
        self.status = VMStatus(status)

    def update_status(self, new_status):
        self.status = VMStatus(new_status)

    def __str__(self):
        return f"VM {self.id}: {self.name}, Status: {self.status.name}"

class VMManager:
    def __init__(self):
        self.vms = {}

    def create_vm(self, id, name, cpu_cores, memory_gb, disk_gb, status=VMStatus.STOPPED):
        if id in self.vms:
            raise ValueError(f"VM with ID {id} already exists.")
        self.vms[id] = VirtualMachine(id, name, cpu_cores, memory_gb, disk_gb, status)

    def delete_vm(self, id):
        if id in self.vms:
            del self.vms[id]
        else:
            raise ValueError(f"No VM with ID {id} found.")

    def get_vm_status(self, id):
        if id in self.vms:
            return self.vms[id].status
        else:
            raise ValueError(f"No VM with ID {id} found.")

    def update_vm_status(self, id, new_status):
        if id in self.vms:
            self.vms[id].update_status(new_status)
        else:
            raise ValueError(f"No VM with ID {id} found.")

    def list_vms(self):
        return [str(vm) for id, vm in self.vms.items()]