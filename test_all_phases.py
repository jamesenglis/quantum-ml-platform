#!/usr/bin/env python3
"""
Test script for all Quantum ML Platform phases
"""

import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def test_phase_2():
    """Test FastAPI schemas"""
    try:
        from schemas.models import PredictionRequest, PredictionResponse
        print("✅ Phase 2: Schemas imported successfully")
        return True
    except Exception as e:
        print(f"❌ Phase 2 failed: {e}")
        return False

def test_phase_3():
    """Test data manager"""
    try:
        from data.data_manager import DataManager
        manager = DataManager()
        print("✅ Phase 3: Data manager created successfully")
        return True
    except Exception as e:
        print(f"❌ Phase 3 failed: {e}")
        return False

def test_phase_4():
    """Test Prefect flows"""
    try:
        from orchestration.flows import training_flow
        print("✅ Phase 4: Prefect flows imported successfully")
        return True
    except Exception as e:
        print(f"❌ Phase 4 failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Testing Quantum ML Platform Phases...\n")
    
    results = [
        test_phase_2(),
        test_phase_3(), 
        test_phase_4()
    ]
    
    if all(results):
        print("\n🎉 All phases tested successfully!")
    else:
        print("\n⚠️  Some phases need attention")
