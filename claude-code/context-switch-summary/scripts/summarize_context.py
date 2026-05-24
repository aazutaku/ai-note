import os
import subprocess

def get_current_directory():
    return os.getcwd()

def get_git_branch():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
    except Exception:
        return "N/A"

def get_git_status():
    try:
        return subprocess.check_output(['git', 'status', '--short']).decode().strip()
    except Exception:
        return ""

def get_git_diff():
    try:
        return subprocess.check_output(['git', 'diff', '--stat']).decode().strip()
    except Exception:
        return ""

def get_recent_files():
    files = []
    for root, dirs, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith(('.py', '.js', '.ts', '.md')):
                path = os.path.join(root, filename)
                if os.path.getmtime(path) > (os.path.getmtime(__file__) - 60*60*24):
                    files.append(path)
    return files

def main():
    print("[Context Switch Summary]")
    print(f"- 現在のdirectory: {get_current_directory()}")
    print(f"- 現在のbranch: {get_git_branch()}")
    status = get_git_status()
    if status:
        print(f"- git status:\n{status}")
    diff = get_git_diff()
    if diff:
        print(f"- 直前のdiff:\n{diff}")
    recent = get_recent_files()
    if recent:
        print("- 最近編集したファイル:")
        for f in recent:
            print(f"    - {f}")
    print("- TODO: (手動で追記してください)")

if __name__ == "__main__":
    main()