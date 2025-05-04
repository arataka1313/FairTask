import streamlit as st
import os, json, glob
import shutil

DATA_DIR = "data"
TEMPLATE_USERS = os.path.join(DATA_DIR, "template_users.json")
TEMPLATE_TASKS = os.path.join(DATA_DIR, "template_tasks.json")

def restore_templates():
    shutil.copy(TEMPLATE_USERS, os.path.join(DATA_DIR, "users.json"))
    shutil.copy(TEMPLATE_TASKS, os.path.join(DATA_DIR, "tasks.json"))

def run():
    st.title("🔧 管理画面（内部用）")

    pw = st.text_input("管理パスワード", type="password")
    if pw != st.secrets.get("ADMIN_PASSWORD", "admin123"):
        st.stop()

    st.success("🔓 管理アクセスOK")

    if st.button("🧹 割り当て & 履歴データの初期化"):
        for f in glob.glob(os.path.join(DATA_DIR, "assignments_*.json")):
            os.remove(f)
        for f in ["history.json", "thanks_log.json"]:
            with open(os.path.join(DATA_DIR, f), "w", encoding="utf-8") as f_:
                json.dump([], f_)
        st.success("履歴と割り当てデータを初期化したにゃ！")

    if st.checkbox("📂 users.jsonの中身を見る"):
        with open(os.path.join(DATA_DIR, "users.json"), encoding="utf-8") as f:
            st.json(json.load(f))
