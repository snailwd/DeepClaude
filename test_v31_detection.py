#!/usr/bin/env python3
"""Test script to verify DeepSeek v3.1 detection and thinking mode"""

import asyncio
import json
from unittest.mock import AsyncMock, patch
import sys
import os

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app.clients.deepseek_client import DeepSeekClient

async def test_v31_detection():
    """Test v3.1 model detection"""
    print("Testing DeepSeek v3.1 detection...")
    
    # Create a mock DeepSeek client
    client = DeepSeekClient("test-key", "https://api.test.com")
    
    # Test cases for v3.1 detection
    test_cases = [
        ("deepseek-v3-1-250821", True),
        ("deepseek-v3.1", True), 
        ("DeepSeek-V3.1", True),
        ("deepseek-r1", False),
        ("deepseek-reasoner", False),
        ("deepseek-chat", False),
    ]
    
    print("\n=== Model Detection Tests ===")
    for model, expected in test_cases:
        # Mock the _make_request method to capture the data parameter
        with patch.object(client, '_make_request', new_callable=AsyncMock) as mock_request:
            mock_request.return_value = []
            
            try:
                # This will trigger the detection logic
                async for _ in client.stream_chat([{"role": "user", "content": "test"}], model):
                    pass
                
                # Check if thinking parameter was added
                if mock_request.called:
                    call_args = mock_request.call_args
                    data = call_args[0][1]  # Second argument is the data dict
                    has_thinking = "thinking" in data and data["thinking"]["type"] == "enabled"
                    
                    status = "✓ PASS" if has_thinking == expected else "✗ FAIL"
                    print(f"{status} Model: {model:<20} | Expected: {expected:<5} | Got: {has_thinking}")
                else:
                    print(f"✗ FAIL Model: {model:<20} | Mock not called")
                    
            except Exception as e:
                print(f"✗ ERROR Model: {model:<20} | Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_v31_detection())