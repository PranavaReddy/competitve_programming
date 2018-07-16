import os
import sys
import hashlib


def file_hash(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for i in iter(lambda: f.read(128 * 1024), b''):
            h.update(i)
    return h.hexdigest()


def dup_files(main_folder):
    hashes = {}
    directory = [main_folder]
    dup = []

    while directory:
        current_path = directory.pop()
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                directory.append(full_path)
        
        else:
            file_hash = file_hash(current_path)
            last_time = os.path.getmtime(current_path)
            if file_hash in hashes:
                temp, ep = hashes[file_hash]
                if last_time > temp:
                    dup.append((current_path, ep))
                else:
                    dup.append((ep, current_path))
                    hashes[file_hash] = (last_time, current_path)
            else:
                hashes[file_hash] = (last_time, current_path)
    return dup