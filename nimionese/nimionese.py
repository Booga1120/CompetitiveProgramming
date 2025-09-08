#!/usr/bin/env python3
import subprocess
import sys
import os

def main():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to parent directory for proper package structure
    parent_dir = os.path.dirname(script_dir)
    os.chdir(parent_dir)
    
    # Compile Java file
    try:
        subprocess.run(['javac', 'nimionese/Main.java'], check=True)
        print("Compiled successfully!")
    except subprocess.CalledProcessError:
        print("Compilation failed!")
        return
    
    # Run all sample inputs
    for i in range(1, 5):
        print(f"\nRunning sample {i}:")
        try:
            with open(f'nimionese/samples/{i}.in', 'r') as input_file:
                result = subprocess.run(
                    ['java', 'nimionese.Main'], 
                    stdin=input_file, 
                    capture_output=True, 
                    text=True
                )
                print(result.stdout.strip())
        except FileNotFoundError:
            print(f"Sample {i} not found")
        print("---")

if __name__ == "__main__":
    main()