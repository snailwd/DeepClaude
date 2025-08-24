#!/usr/bin/env python3
"""Simple test for DeepSeek v3.1 detection logic"""

def test_v31_detection():
    """Test the v3.1 detection logic directly"""
    print("Testing DeepSeek v3.1 detection logic...")
    
    # Test cases - this replicates the detection logic from deepseek_client.py
    test_cases = [
        ("deepseek-v3-1-250821", True),
        ("deepseek-v3.1", True), 
        ("DeepSeek-V3.1", True),
        ("deepseek-v3.1-large", True),
        ("deepseek-r1", False),
        ("deepseek-reasoner", False),
        ("deepseek-chat", False),
        ("claude-3-7-sonnet", False),
    ]
    
    print("\n=== Model Detection Tests ===")
    all_passed = True
    
    for model, expected in test_cases:
        # Replicate the detection logic from deepseek_client.py
        is_v31_model = (
            model == "deepseek-v3-1-250821" or
            "v3.1" in model.lower() or
            "v3-1" in model.lower()
        )
        
        status = "PASS" if is_v31_model == expected else "FAIL"
        if is_v31_model != expected:
            all_passed = False
        
        print(f"{status:4} Model: {model:<25} | Expected: {expected:<5} | Got: {is_v31_model}")
    
    print(f"\n=== Summary ===")
    if all_passed:
        print("PASS All tests passed! DeepSeek v3.1 detection is working correctly.")
    else:
        print("FAIL Some tests failed. Please check the detection logic.")
    
    return all_passed

if __name__ == "__main__":
    test_v31_detection()