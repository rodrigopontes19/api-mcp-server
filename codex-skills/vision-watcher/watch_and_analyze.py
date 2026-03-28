import time
import os
import subprocess

WATCH_DIR = os.path.join(os.getcwd(), "input")
PROCESSED_DIR = os.path.join(os.getcwd(), "processed")

os.makedirs(WATCH_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

print(f"👀 Watching folder: {WATCH_DIR}")

processed_files = set()

while True:
    try:
        files = os.listdir(WATCH_DIR)

        for file in files:
            full_path = os.path.join(WATCH_DIR, file)

            if file in processed_files:
                continue

            if os.path.isfile(full_path):
                print(f"🚀 Processing: {file}")

                # chama o analisador universal
                subprocess.run([
                    "python",
                    "analisador_universal.py",
                    full_path
                ])

                processed_files.add(file)

                # move para pasta processed
                os.rename(full_path, os.path.join(PROCESSED_DIR, file))

                print(f"✅ Done: {file}\n")

        time.sleep(3)

    except KeyboardInterrupt:
        print("\n🛑 Watcher stopped.")
        break
