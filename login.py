from tradingapi_a.mconnect import MConnect
import json
import os

# 📥 Step 1: Ask for input credentials
username = input("👤 Username: ")
password = input("🔒 Password: ")
api_key = input("🔑 API Key: ")
checksum = "L"

# 🔌 Step 2: Start login
m = MConnect()
res = m.login(username, password)
res_json = res.json()  # Convert Response object to dictionary

# 📲 Step 3: OTP verification
if res_json["status"] == "success":
    print("✅ OTP sent to your mobile number.")
    otp = input("📲 Enter OTP: ")

    # Step 4: Generate session token
    token = m.generate_session(api_key, otp, checksum)
    token_json = token.json()

    if token_json["status"] == "success":
        access_token = token_json["data"]["access_token"]
        login_time = token_json["data"]["login_time"]

        # 🧾 Step 5: Save to JSON
        os.makedirs("session_data", exist_ok=True)
        with open("session_data/token.json", "w") as f:
            json.dump({
                "access_token": access_token,
                "api_key": api_key,
                "user": username,
                "login_time": login_time
            }, f, indent=4)

        print("🔓 Token saved successfully to session_data/token.json")
    else:
        print("❌ OTP failed:", token_json.get("message", "Unknown error"))
else:
    print("❌ Login failed:", res_json.get("message", "Unknown error"))
