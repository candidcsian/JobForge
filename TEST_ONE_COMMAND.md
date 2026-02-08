# Testing the One-Command Installer

## 🧪 Test on Your Other MacBook

### **Step 1: Open Terminal**

Just open Terminal (nothing else needed!)

### **Step 2: Run One Command**

Copy and paste this:

```bash
curl -sSL https://raw.githubusercontent.com/candidcsian/JobBell/main/install.sh | bash
```

Press Enter.

### **Step 3: Watch It Work**

You should see:
```
🚀 JobBell - AI-Powered Career Assistant
==========================================

📍 Detected: Mac

🔍 Checking Python...
✅ Python 3.x found

📥 Downloading JobBell...
✅ Downloaded!

🔧 Setting up environment...
📦 Installing dependencies...
✅ Setup complete!

🎯 Starting JobBell Agent...

======================================================================
🚀 Welcome to JobBell - Your AI Career Assistant!
======================================================================
```

### **Step 4: Test with Dummy Data**

When it asks questions, use test data:
- Name: Test User
- Email: test@example.com
- Phone: +91-9999999999
- Location: Bangalore
- Career start: 2020
- Current company: TestCorp
- Role: Test Engineer

### **Step 5: Verify Output**

After completion, check:

```bash
# Check files were created
ls ~/JobBell/career/
ls ~/JobBell/results/resumes/

# View the resume
open ~/JobBell/results/resumes/Test_User_ATS_Resume.docx
```

---

## ✅ What Should Work

- [ ] One command downloads and installs everything
- [ ] No manual setup required
- [ ] Python check works
- [ ] Dependencies install automatically
- [ ] Agent starts immediately
- [ ] Can provide test data
- [ ] Resume is generated
- [ ] LinkedIn content is created
- [ ] No errors appear

---

## ❌ What Should NOT Happen

- [ ] Asks to install Python manually
- [ ] Asks to install dependencies manually
- [ ] Requires git clone
- [ ] Requires cd commands
- [ ] Shows errors
- [ ] Fails to start

---

## 🐛 If Something Breaks

### Error: "Python not found"

The script will show:
```
❌ Python 3 not found!

Please install Python 3.9 or higher:
  brew install python3
```

User just runs: `brew install python3` then tries again.

### Error: "Git not found"

The script will auto-install git (asks for password).

### Error: "Permission denied"

User might need to run:
```bash
chmod +x ~/JobBell/install.sh
```

---

## 📊 Success Criteria

**Perfect experience**:
1. User opens Terminal
2. Pastes one command
3. Presses Enter
4. Everything installs automatically
5. Agent starts asking questions
6. User provides data
7. Gets resume in 1-2 hours
8. Done!

**No technical knowledge required!**

---

## 🎯 Test Scenarios

### Scenario 1: Fresh Mac (No Python)
- Should detect missing Python
- Should guide user to install
- Should work after Python installed

### Scenario 2: Mac with Python
- Should detect Python
- Should download JobBell
- Should install dependencies
- Should start agent immediately

### Scenario 3: Already Installed
- Should detect existing installation
- Should ask to update
- Should pull latest changes if yes

### Scenario 4: No Git
- Should detect missing git
- Should install git automatically
- Should continue with download

---

## 💡 What Makes This Easy

**Before** (complicated):
```bash
# Install Python
brew install python3

# Clone repo
git clone https://github.com/candidcsian/JobBell.git

# Go to directory
cd JobBell

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install python-docx pyyaml

# Run agent
python3 jobbell_agent.py
```

**After** (simple):
```bash
curl -sSL https://raw.githubusercontent.com/candidcsian/JobBell/main/install.sh | bash
```

**That's it!** 🎉

---

## 📱 Share This Command

When sharing with friends, just say:

```
Open Terminal and run:

curl -sSL https://raw.githubusercontent.com/candidcsian/JobBell/main/install.sh | bash

That's it! It will guide you through everything.
```

---

## 🔄 To Run Again Later

After first install, users can run:

```bash
cd ~/JobBell
./start_agent.sh
```

Or just run the install command again (it will update).

---

**Test it now on your other MacBook!** 🧪

**Expected time**: 5 minutes (including download and install)

**Reply with**: "works perfectly!" or "found issue: [description]"
