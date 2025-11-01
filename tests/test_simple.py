def test_basic():
    """Simple test to verify pytest works"""
    assert 1 + 1 == 2

def test_imports():
    """Test basic imports"""
    import numpy as np
    import sklearn
    assert True  # If we get here, imports work

def test_path():
    """Test Python path setup"""
    import sys
    import os
    # Check that src is in path
    src_path = os.path.join(os.path.dirname(__file__), '..', 'src')
    assert os.path.exists(src_path)
