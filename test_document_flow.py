#!/usr/bin/env python3
"""
Test the document collection flow
"""

from pathlib import Path

def test_file_validation():
    """Test file path validation"""
    
    print("Testing file validation logic:\n")
    
    test_cases = [
        ("/Users/rajamas/Downloads/Utkarsh_Resume (1).pdf", "Valid file path"),
        ("2", "Invalid - just a number"),
        ("4", "Invalid - just a number"),
        ("/nonexistent/file.pdf", "Invalid - file doesn't exist"),
        ("done", "Valid - exit command"),
    ]
    
    for file_path, description in test_cases:
        print(f"Input: '{file_path}'")
        print(f"Description: {description}")
        
        # Clean the path
        cleaned = file_path.replace('\\', '').strip('\'"')
        
        # Check if it's the exit command
        if cleaned.lower() == 'done':
            print("✅ Exit command recognized\n")
            continue
        
        # Check if file exists
        if Path(cleaned).exists():
            print(f"✅ File exists: {cleaned}\n")
        else:
            print(f"❌ File not found: {cleaned}\n")

if __name__ == "__main__":
    test_file_validation()
    
    print("\n" + "="*70)
    print("EXPECTED BEHAVIOR:")
    print("="*70)
    print("""
Option 4 selected:
  → Should immediately go to manual entry
  → Should NOT ask for file paths

Option 1/2/3 selected:
  → Should ask for file paths
  → Should validate each path
  → If invalid path: show error, ask again
  → If 'done': proceed
  → If no files collected: offer manual entry

Invalid option (5, abc, etc.):
  → Show error
  → Ask to choose again
""")
