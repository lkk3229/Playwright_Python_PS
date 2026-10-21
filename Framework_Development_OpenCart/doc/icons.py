from colorama import Fore, Style, init
import logging

# Initialize Colorama
init(autoreset=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

# Sample Logs
print(Fore.CYAN + "🚀 Starting Test Execution")
print(Fore.BLUE + "🌐 Launching Browser")
print(Fore.YELLOW + "⚠️ Warning: Test data not found")
print(Fore.GREEN + "✅ Registration Successful")
print(Fore.RED + "❌ Registration Failed")

print("================================")
print(Fore.GREEN + "✅ Pass")
print(Fore.RED + "❌ Fail")
print(Fore.YELLOW + "⚠️ Warning")
print(Fore.CYAN + "🚀 Launch")
print(Fore.CYAN + "🌐 Browser")
print(Fore.BLUE + "📝 Form")
print(Fore.CYAN + "🔍 Verification")
print(Fore.BLUE + "📸 Screenshot")
print(Fore.MAGENTA + "📹 Video Recording")
print(Fore.CYAN + "🧪 Test Case")
print(Fore.CYAN + "🎯 Execution")
print(Fore.GREEN + "🎉 Success")
print(Fore.RED + "🐞 Bug")
print(Fore.YELLOW + "⏳ Waiting")
print(Fore.BLUE + "🔒 Login")
print(Fore.BLUE + "📂 File")
print(Fore.MAGENTA + "📊 Report")
print(Fore.MAGENTA + "📋 Test Data")
print(Fore.BLUE + "📥 Download")
print(Fore.BLUE + "📤 Upload")
print(Fore.CYAN + "🔗 Navigation")
print(Fore.BLUE + "🏠 Home Page")
print(Fore.BLUE + "📧 Email")
print(Fore.BLUE + "🔑 Password")
print(Fore.BLUE + "👤 User")
print(Fore.GREEN + "💾 Save")
print(Fore.RED + "🗑️ Delete")
print(Fore.YELLOW + "📌 Important")
print(Fore.GREEN + "✨ Feature")
print(Fore.CYAN + "🔄 Refresh")
print(Fore.MAGENTA + "🎭 Environment")
print(Fore.CYAN + "ℹ️ Information")
print(Fore.CYAN + "ℹ️ Test Started")
print(Fore.CYAN + "ℹ️ Opening URL")
print(Fore.CYAN + "📢 Information")
print(Fore.CYAN + "📌 Information")
print(Fore.CYAN + "💡 Information")
print(Fore.CYAN + "🔔 Information")
print(Fore.BLUE + "📎 Attaching Screenshot")
print("================================")
print(Fore.CYAN + "🚀 Starting Test Execution")
print(Fore.CYAN + "🌐 Launching Browser")
print(Fore.BLUE + "🔒 Logging into Application")
print(Fore.BLUE + "📝 Filling Registration Form")
print(Fore.CYAN + "🔍 Verifying User Details")
print(Fore.YELLOW + "⏳ Waiting for Page Load")
print(Fore.BLUE + "📸 Capturing Screenshot")
print(Fore.MAGENTA + "📹 Recording Test Execution")
print(Fore.GREEN + "✅ Test Passed")
print(Fore.RED + "❌ Test Failed")
print(Fore.RED + "🐞 Bug Found")
print(Fore.MAGENTA + "📊 Generating Report")
print(Fore.GREEN + "🎉 Test Execution Completed")
print("================================")

# Common Icons Reference
icons = """
✅ Pass
❌ Fail
⚠️ Warning
🚀 Launch
🌐 Browser
📝 Form
🔍 Verification
📸 Screenshot
📹 Video Recording
🧪 Test Case
🎯 Execution
🎉 Success
🐞 Bug
⏳ Waiting
🔒 Login
📂 File
📊 Report
📋 Test Data
📥 Download
📤 Upload
🔗 Navigation
🏠 Home Page
📧 Email
🔑 Password
👤 User
💾 Save
🗑️ Delete
📌 Important
✨ Feature
🔄 Refresh
🎭 Environment

SUCCESS = Fore.GREEN      # ✅ 🎉
ERROR = Fore.RED          # ❌ 🐞
WARNING = Fore.YELLOW     # ⚠️
INFO = Fore.CYAN          # 🚀 🌐 🔍
REPORT = Fore.MAGENTA     # 📊 📋
ACTION = Fore.BLUE        # 📝 📸 📂
"""

print(Fore.MAGENTA + icons)