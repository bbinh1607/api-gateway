# ⚡ API Gateway - Microservices Powerhouse

🚀 **api-gateway** là trái tim của hệ thống microservices — nơi tất cả các request đều được dẫn dắt qua một cổng trung tâm thông minh, an toàn, có kiểm soát và mở rộng linh hoạt.

---

## 🧠 Kiến trúc tổng quan

[Client] ───▶ [API Gateway] ──▶ [User Service]
└──▶ [Device Service]
└──▶ [Camera Service]
└──▶ [Auth Service]

yaml
Sao chép
Chỉnh sửa

- ✅ **Routing thông minh** theo đường dẫn
- ✅ **Forward token** bảo toàn xác thực
- ✅ **Middleware phân quyền**
- ✅ **Dễ dàng tích hợp thêm service mới**

---

## 🔥 Tính năng nổi bật

- ✨ Giao tiếp thống nhất giữa frontend và microservices
- 🔐 Tích hợp JWT & phân quyền theo `role` / `rank`
- 🧱 Xử lý lỗi tập trung (retry, timeout, fallback)
- 📦 Gọn nhẹ, thuần `Flask + Requests`, không rối rắm

---

## 📁 Cấu trúc thư mục

api_gateway/
├── api/ # Route chính (forward request)
├── middlewares/ # Middleware xác thực, phân quyền
├── services/ # BaseService + từng microservice
├── utils/ # Helper (token decode, response format)
├── config.py # Config hệ thống
└── app.py # App chính để chạy Flask

yaml
Sao chép
Chỉnh sửa

---

## ⚙️ Cách chạy

```bash
# Cài package
pip install -r requirements.txt

# Chạy Flask Gateway
python app.py
Mặc định chạy ở http://localhost:8000

📡 Ví dụ gọi API
bash
Sao chép
Chỉnh sửa
curl -X GET http://localhost:8000/api/device/get-all \
  -H "Authorization: Bearer <your-jwt-token>"
💪 Dành cho Dev siêu nhân
😎 Bạn có thể mở rộng thêm route chỉ bằng 1 dòng

⚔️ Bạn có thể phân quyền từng route dễ dàng

🔁 Retry + timeout tự động

🪄 Không cần đụng tới từng service — mọi thứ đi qua Gateway

📜 License
MIT © bbinh1607
