# 🔔 Rename GitHub Repository: JobForge → JobBell

## Steps to Rename on GitHub:

1. **Go to GitHub:**
   https://github.com/candidcsian/JobForge

2. **Click "Settings"** (top right of repo page)

3. **Scroll down to "Repository name"**

4. **Change from:** `JobForge`
   **Change to:** `JobBell`

5. **Click "Rename"**

6. **Update local remote:**
   ```bash
   cd ~/JobForge
   git remote set-url origin https://github.com/candidcsian/JobBell.git
   ```

7. **Rename local directory (optional):**
   ```bash
   cd ~
   mv JobForge JobBell
   cd JobBell
   ```

8. **Test:**
   ```bash
   git push
   ```

## New URLs After Rename:

- **Repo:** https://github.com/candidcsian/JobBell
- **Install:** `bash <(curl -sSL https://raw.githubusercontent.com/candidcsian/JobBell/main/jobbell_onecommand.sh)`

## Share Message (Updated):

```
🔔 Try JobBell - finds jobs that match YOUR skills!

✅ Fetches 100+ jobs
✅ Matches to your profile
✅ Finds LinkedIn contacts for referrals
✅ 100% free & private

One command:
bash <(curl -sSL https://raw.githubusercontent.com/candidcsian/JobBell/main/jobbell_onecommand.sh)

GitHub: https://github.com/candidcsian/JobBell

Let me know what you think! 🙏
```

---

**Do this now, then JobBell is ready to share! 🔔**
