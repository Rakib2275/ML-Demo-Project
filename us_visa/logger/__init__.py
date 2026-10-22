import logging
import os
from datetime import datetime

# ১. লগ ফাইলের নাম তৈরি
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# ২. বর্তমান প্রোজেক্টের ভেতর 'logs' ফোল্ডারের পাথ নির্ধারণ
log_dir_path = os.path.join(os.getcwd(), "logs")

# ৩. 'logs' ফোল্ডারটি তৈরি করা (যদি আগে থেকে না থাকে)
os.makedirs(log_dir_path, exist_ok=True)

# ৪. লগ ফাইলের সম্পূর্ণ পাথ তৈরি
logs_path = os.path.join(log_dir_path, LOG_FILE)

# ৫. লগিং কনফিগারেশন
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)