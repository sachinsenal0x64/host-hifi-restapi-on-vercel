<p align="center">
 <img width="100px" src="https://sachinsenal0x64.github.io/picx-images-hosting/favicon512x512-vercel-typescript-express-api.58o5ubszquf4.webp" align="center" alt=":package: deploy-hifi-restapi-on-vercel" />
 <h2 align="center">:package: Host HiFi REST API ON Vercel</h2>
</p>

<div align="center">
 
   #### This is [Hifi Tui](https://github.com/sachinsenal0x64/hifi-tui) core it base on this API and you can selfhost :)
 
   [![Docker Image CI](https://github.com/sachinsenal0x64/host-hifi-restapi-on-vercel/actions/workflows/docker-image.yml/badge.svg)](https://github.com/sachinsenal0x64/host-hifi-restapi-on-vercel/actions/workflows/docker-image.yml)
 
 </div>

<br><br>

# :two_hearts: Community

> :beers: Join the community:  <a href="https://discord.gg/EbfftZ5Dd4">Discord</a>
> [![](https://cdn.statically.io/gh/sachinsenal0x64/picx-images-hosting@master/discord.72y8nlaw5mdc.webp)](https://discord.gg/EbfftZ5Dd4)
 
<br>

# ❓ Requirements

- Tidal Subscription

- Fill the [.env](https://github.com/sachinsenal0x64/host-hifi-restapi-on-vercel/blob/main/src/.env-example)

- Redis (its free)

- Grab Tokens / Ids Using [tidal_auth.py](https://github.com/sachinsenal0x64/hifi-tui/blob/main/tidal_auth/)

<br>

# ☁️ One-Click Deploy To Vercel
> 🧗 THIS WILL BYPASS TIDAL GEO RESTRICT CONTENT 

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fsachinsenal0x64%2Fhost-hifi-restapi-on-vercel%2Ftree%2Fmain%2Fpython%2FHifiAPI&demo-title=HifiAPI%20%2B%20Vercel&demo-description=Use%20HifiAPI%202%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2FHifiAPI.vercel.app%2F&demo-image=https://sachinsenal0x64.github.io/picx-images-hosting/cover.5gnodmhum874.webp)

<br>

# 📄 Documentation

- [API-DOCS](https://github.com/sachinsenal0x64/hifi-tui?tab=readme-ov-file#-api-documentation)
- https://hifitui.401658.xyz
- https://hifitui.pages.dev (Backup Url)

<br>

# 🏠 Running Locally

### 🐳 Docker Compose

```bash
docker-compose up
```

### 🐳 Docker File

```bash
# Build the Docker image
docker build -t host-hifi-restapi-on-vercel .

# Run the Docker contaer
docker run -p 8000:8000 host-hifi-restapi-on-vercel

```

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
