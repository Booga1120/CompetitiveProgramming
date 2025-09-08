#!/bin/bash

# Check if Solution.java exists (main development file)
if [ -f "Solution.java" ]; then
    echo "Generating Main.java from Solution.java..."
    
    # Create Main.java by removing package declaration AND changing class name
    sed -e '/^package /d' -e 's/public class Solution/public class Main/' Solution.java > Main.java
    
    echo "Main.java generated (ready for Kattis submission)"
elif [ ! -f "Main.java" ]; then
    echo "Error: Neither Solution.java nor Main.java found!"
    exit 1
fi

# Compile Main.java (the Kattis-ready version)
echo "Compiling Main.java..."
javac Main.java

if [ $? -ne 0 ]; then
    echo "Compilation failed!"
    exit 1
fi

echo "Compilation successful!"
echo

# Test all sample files
for file in samples/*.in; do
    if [ -f "$file" ]; then
        # Extract the number from filename (e.g., "1" from "1.in")
        basename=$(basename "$file" .in)
        expected_file="samples/${basename}.ans"
        
        echo "╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗"
        printf "║ %-16s %-40s %-40s %-40s ║\n" "TEST $basename" "INPUT" "YOUR OUTPUT" "EXPECTED OUTPUT"
        echo "╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣"
        
        # Read input
        input_content=$(cat "$file" 2>/dev/null | tr '\n' ' ' | sed 's/[[:space:]]*$//')
        
        # Get your output
        your_output=$(java Main < "$file" 2>/dev/null | tr '\n' ' ' | sed 's/[[:space:]]*$//')
        
        # Get expected output
        if [ -f "$expected_file" ]; then
            expected_output=$(cat "$expected_file" 2>/dev/null | tr '\n' ' ' | sed 's/[[:space:]]*$//')
        else
            expected_output="FILE NOT FOUND"
        fi
        
        # Truncate long outputs for display
        input_display=$(echo "$input_content" | cut -c1-38)
        your_display=$(echo "$your_output" | cut -c1-38)
        expected_display=$(echo "$expected_output" | cut -c1-38)
        
        # Add ellipsis if truncated
        [ ${#input_content} -gt 38 ] && input_display="${input_display}.."
        [ ${#your_output} -gt 38 ] && your_display="${your_display}.."
        [ ${#expected_output} -gt 38 ] && expected_display="${expected_display}.."
        
        # Display the row
        printf "║ %-16s %-40s %-40s %-40s ║\n" "" "$input_display" "$your_display" "$expected_display"
        
        # Show match status
        if [ "$your_output" = "$expected_output" ]; then
            printf "║ %-16s %-40s %-40s %-40s ║\n" "" "" "✓ MATCH" ""
        else
            printf "║ %-16s %-40s %-40s %-40s ║\n" "" "" "✗ NO MATCH" ""
        fi
        
        echo "╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"
        echo
    fi
done

echo "📁 Main.java is ready for Kattis submission!"

# Clean up compiled files if desired (uncomment next line)
# rm -f *.class