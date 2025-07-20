
# API Service Deploy Example (Docker Compose + Flask)

ตัวอย่างโปรเจค Flask API ที่รันแบบหลาย Container ด้วย Docker Compose โดยที่
- **app1** เป็น API หลัก ที่สามารถเรียก API จาก app2 ได้
- **app2** เป็น API สำหรับให้บริการข้อมูล เช่น คำคม หรือข้อมูลอื่น ๆ
- ใช้ `docker-compose.yml` เพื่อรันทั้งสอง container พร้อมกัน

## โครงสร้างโปรเจค

```
apiservice-deploy/
│
├── docker-compose.yml
│
├── app1/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── app2/
    ├── app.py
    ├── Dockerfile
    └── requirements.txt
```

---

## วิธี Deploy ระบบ

### 1. ติดตั้ง Docker และ Docker Compose

หากยังไม่มี Docker:
```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo systemctl enable docker
```

ตรวจสอบเวอร์ชัน:
```bash
docker -v
docker-compose -v
```

### 2. Clone Repo นี้

```bash
git clone https://github.com/tiggertiya2022-ctrl/Facerecogito.git
cd apiservice-deploy
```

### 3. Build และ Run ด้วย Docker Compose

```bash
docker-compose up --build -d
```

ระบบจะเปิด
- app1 ที่ `http://localhost:5000`
- app2 ที่ `http://localhost:5001`

---

## วิธีทดสอบระบบ

### ทดสอบ app1
```bash
curl http://localhost:5000/
```
ผลลัพธ์:
```text
Hello from GET API1!
```

### ทดสอบ API ที่ app1 ไปดึงข้อมูลจาก app2
```bash
curl http://localhost:5000/api/motivation
```
ผลลัพธ์ตัวอย่าง:
```json
{
    "quote": "จงเชื่อว่าคุณทำได้ แล้วคุณจะทำได้"
}
```

หรือกำหนด category:
```bash
curl "http://localhost:5000/api/motivation?category=กำลังใจ"
```

### ทดสอบ app2 โดยตรง
```bash
curl "http://localhost:5001/api/quote?category=กำลังใจ"
```

---

## วิธีหยุดระบบ

```bash
docker-compose down
```

---

## หมายเหตุเพิ่มเติม
- คุณสามารถแก้ไขคำคมหรือข้อมูลที่ `app2/app.py`
- สามารถเพิ่ม API ใหม่โดยเพิ่ม endpoint ใน `app1` และ `app2`

---

## License
MIT License
