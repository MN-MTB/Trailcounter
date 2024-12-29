import os
from csv import file_exists

def get_disk_size_mb() -> float:
    fs_stat = os.statvfs('/')
    block_size = fs_stat[0]       # Filesystem block size
    total_blocks = fs_stat[2]     # Total number of blocks
    total_size = block_size * total_blocks
    return total_size / (1024 * 1024)  # Convert bytes to MB

def get_disk_size_kb() -> float:
    fs_stat = os.statvfs('/')
    block_size = fs_stat[0]       # Filesystem block size
    total_blocks = fs_stat[2]     # Total number of blocks
    total_size = block_size * total_blocks
    return total_size / 1024  # Convert bytes to KB

def get_file_size_mb(file_path: str) -> float:
    if file_exists(file_path):
        file_size_bytes = os.stat(file_path)[6]
        return file_size_bytes / (1024 * 1024)  # Convert bytes to MB
        
        
