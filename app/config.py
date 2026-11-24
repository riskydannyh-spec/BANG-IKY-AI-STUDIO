import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
ADMIN_IDS = {int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip().isdigit()}
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "").strip()
BRAND = "VARTEX AI STUDIO"
CHIEF = "Chief : IKY VARTEX AI STUDIO"
