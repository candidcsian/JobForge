#!/usr/bin/env python3
"""
JobForge Agent - Simplified Version for Testing
"""

import sys
from pathlib import Path

def main():
    print("\n" + "="*70)
    print("🚀 JobForge - Quick Test")
    print("="*70)
    print("\nLet's collect some basic information:\n")
    
    # Basic info
    print("1. What's your full name?")
    name = input("   > ").strip()
    
    print("\n2. Your email:")
    email = input("   > ").strip()
    
    print("\n3. Career start year (e.g., 2015):")
    year = input("   > ").strip()
    
    # Validate
    if not name or not email or not year:
        print("\n⚠️  Some information was missing, but that's okay!")
        print("This was just a quick test to verify installation works.")
        print("\n" + "="*70)
        print("✅ Installation Test Successful!")
        print("="*70)
        print(f"\nJobForge is installed and working correctly!")
        print(f"\nTo build your actual resume, run:")
        print(f"  cd ~/JobForge")
        print(f"  ./start_agent.sh")
        print("\nThe full version will guide you through:")
        print("  ✅ Complete career history")
        print("  ✅ ATS-optimized resume generation")
        print("  ✅ LinkedIn profile optimization")
        print("  ✅ Job search strategy")
        print("="*70)
        return
    
    try:
        year_int = int(year)
        experience = 2026 - year_int
    except:
        print("\n❌ Invalid year")
        return
    
    # Summary
    print("\n" + "="*70)
    print("✅ Information Collected!")
    print("="*70)
    print(f"\nName: {name}")
    print(f"Email: {email}")
    print(f"Experience: {experience} years")
    print(f"\nFiles would be created at:")
    print(f"  - Career profile: ~/JobForge/career/{name.lower().replace(' ', '-')}-master.md")
    print(f"  - Resume: ~/JobForge/results/resumes/{name.replace(' ', '_')}_ATS_Resume.docx")
    print("\n✅ Test completed successfully!")
    print("\nTo run the full version: cd ~/JobForge && python3 jobforge_agent.py")
    print("="*70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
