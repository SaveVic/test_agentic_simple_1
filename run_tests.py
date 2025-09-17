import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

# Run pytest
if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "tests/"])