#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

def run_tests():
    # Check if solution.py exists
    if not os.path.exists('solution.py'):
        print("❌ solution.py not found")
        return
    
    # Check if samples directory exists
    samples_dir = Path('samples')
    if not samples_dir.exists():
        print("❌ samples directory not found")
        return
    
    # Find all input files
    input_files = sorted(samples_dir.glob('*.in'), key=lambda x: int(x.stem))
    
    if not input_files:
        print("❌ No input files found in samples/")
        return
    
    passed = 0
    total = len(input_files)
    
    print(f"Running {total} test(s)...")
    
    for input_file in input_files:
        test_num = input_file.stem
        ans_file = samples_dir / f"{test_num}.ans"
        
        if not ans_file.exists():
            print(f"⚠️  Test {test_num}: No answer file found")
            continue
        
        try:
            # Run solution.py with input file
            with open(input_file, 'r') as f:
                result = subprocess.run(
                    [sys.executable, 'solution.py'],
                    stdin=f,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
            
            if result.returncode != 0:
                print(f"❌ Test {test_num}: Runtime error")
                if result.stderr:
                    print(f"   Error: {result.stderr.strip()}")
                continue
            
            # Read expected answer
            with open(ans_file, 'r') as f:
                expected = f.read().strip()
            
            actual = result.stdout.strip()
            
            # Read input for debugging
            with open(input_file, 'r') as f:
                input_content = f.read().strip()
            
            def format_multiline(content, label):
                lines = content.split('\n')
                if len(lines) == 1:
                    return f"   {label}: {content}"
                else:
                    result = f"   {label}:\n"
                    for line in lines:
                        result += f"     {line}\n"
                    return result.rstrip()
            
            if actual == expected:
                print(f"✅ Test {test_num}: Passed")
                print(format_multiline(input_content, "Input"))
                print(format_multiline(actual, "Output"))
                passed += 1
            else:
                print(f"❌ Test {test_num}: Failed")
                print(format_multiline(input_content, "Input"))
                print(format_multiline(expected, "Expected"))
                print(format_multiline(actual, "Got"))
                
        except subprocess.TimeoutExpired:
            print(f"❌ Test {test_num}: Timeout")
        except Exception as e:
            print(f"❌ Test {test_num}: Error - {e}")
    
    print(f"\nResult: {passed}/{total} tests passed")
    if passed == total:
        print("🎉 All tests passed!")

if __name__ == "__main__":
    run_tests()