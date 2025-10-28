import subprocess
import sys


def test_runs():
    # Run the script and assert expected output
    p = subprocess.run([sys.executable, 'src/main.py', '--name', 'Test'], cwd='.', capture_output=True, text=True)
    assert 'Hello, Test' in p.stdout
