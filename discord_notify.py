import os
import requests

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
print("🐾 Webhook URL 読み込み:", "✅ OK" if WEBHOOK_URL else "❌ 失敗")

def send_notification(message):
    if not WEBHOOK_URL:
        print("⚠️ Discord Webhook URL が設定されていません")
        return
    data = {"content": message}
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code != 204:
            print(f"❌ 通知失敗: {response.status_code}, {response.text}")
        else:
            print("✅ 通知成功")
    except Exception as e:
        print(f"🔥 通知中にエラー: {e}")
