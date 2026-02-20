import os
import shutil
import tempfile
import winshell

def temp_files_cleanup():
    ## path to temp directory
    folder = tempfile.gettempdir()
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
    ## removing temp files and folders
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
            

def recycle_bin_cleanup():
    try:
        ## winshell library to properly empty the recycle bin
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        print("Recycle bin has been emptied.")
    except Exception as e:
        print(f"Failed to empty recycle bin. Reason: {e}")

## executing script
def main():
    print("Starting system cleanup...")
    temp_files_cleanup()
    recycle_bin_cleanup()
    print("System cleanup completed.")
    
if __name__ == "__main__":
    main()



