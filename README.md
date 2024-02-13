<p align="center">
 <img width="100px" src="https://sachinsenal0x64.github.io/picx-images-hosting/favicon512x512-vercel-typescript-express-api.58o5ubszquf4.webp" align="center" alt=":package: deploy-hifi-restapi-on-vercel" />
 <h2 align="center">:package: Host HiFi REST API ON Vercel</h2>
</p>

<div align="center">
 
  [![Docker Image CI](https://github.com/sachinsenal0x64/host-hifi-restapi-on-vercel/actions/workflows/docker-image.yml/badge.svg)](https://github.com/sachinsenal0x64/host-hifi-restapi-on-vercel/actions/workflows/docker-image.yml)
 
 </div>

<br>

# ☁️ One-Click Deploy To Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fsachinsenal0x64%2Fhost-hifi-restapi-on-vercel%2Ftree%2Fmain%2Fpython%2FHifiAPI&demo-title=HifiAPI%20%2B%20Vercel&demo-description=Use%20HifiAPI%202%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2FHifiAPI.vercel.app%2F&demo-image=https://sachinsenal0x64.github.io/picx-images-hosting/cover.5gnodmhum874.webp)

<br>

# 🏠 Running Locally
<br>

### 🐳 Docker Compose

```bash
docker-compose up
```

<br>

### 🐳 Docker File

```bash
# Build the Docker image
docker build -t host-hifi-restapi-on-vercel .

# Run the Docker contaer
docker run -p 8000:8000 host-hifi-restapi-on-vercel

```
<br>

### 🦄 Uvicorn
> 🐉 Install dependencies

```bash
pip install -r requirements.txt
```

```bash
python main.py
```
🎉 Your reverse proxy is now available at http://localhost:8000.


<br>

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/sachinsenal0x64/host-hifi-restapi-on-vercel/issues).
