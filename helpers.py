import os
import hashlib
from collections import defaultdict


def get_file_hash(file_path):
    """Generate a hash for a file based on its contents."""
    hasher = hashlib.md5()

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None


def get_file_size(file_path):
    """Get file size in human-readable format."""
    try:
        size = os.path.getsize(file_path)

        for unit in ["B", "KB", "MB", "GB"]:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0

        return f"{size:.2f} TB"

    except Exception:
        return "Unknown"


def find_duplicates(folder_path, progress_callback=None):
    """Find duplicate files and group them by hash."""
    hash_groups = defaultdict(list)
    total_files = 0
    processed_files = 0

    for root, _, files in os.walk(folder_path):
        total_files += len(files)

    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            processed_files += 1

            if progress_callback:
                progress_callback(processed_files, total_files)

            file_hash = get_file_hash(file_path)
            if file_hash:
                hash_groups[file_hash].append(file_path)

    duplicates = {
        hash_val: files for hash_val, files in hash_groups.items() if len(files) > 1
    }
    return duplicates
