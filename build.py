import os
import shutil

def main():
    try:
        if os.path.exists('.next'):
            shutil.rmtree('.next')
    except:
        print('Failed to remove .next folder')
        return None
    
    try:
        os.system('yarn build')
    except:
        print('Failed to execute build process')
        return None
    
    try:
        if os.path.exists('.next.zip'):
            os.remove('.next.zip')
    except:
        print('Failed to remove .next.zip')
    
    try:
        shutil.make_archive('.next', 'zip', '.next')
    except:
        print('Failed to create .next.zip')
        return None

main()
