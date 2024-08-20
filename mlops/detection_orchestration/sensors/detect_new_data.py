import json
import os
import glob

from mage_ai.settings.repo import get_repo_path

if "sensor" not in globals():
    from mage_ai.data_preparation.decorators import sensor


@sensor
def check_for_new_data(*args, **kwargs) -> bool:
    retraining_folder = "/home/src/Data/retraining"
    path = os.path.join(get_repo_path(), ".cache", "data_tracker")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    data_tracker_prev = set()
    if os.path.exists(path):
        with open(path, "r") as f:
            data_tracker_prev = set(json.load(f))

    current_files = set(glob.glob(os.path.join(retraining_folder, "*.csv")))

    with open(path, "w") as f:
        f.write(json.dumps(list(current_files)))

    new_files = current_files - data_tracker_prev

    if new_files:
        print(f"New files found: {new_files}")
        should_train = True
    else:
        print("No new files found.")
        should_train = False

    return should_train
