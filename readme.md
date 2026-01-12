#DB_HOST=127.0.0.1      # if using SQL Auth Proxy
#DB_NAME=appdb
#DB_USER=postgres
#DB_PASSWORD=example123


4️⃣ Instance Template Configuration (Important)

Set environment variables via VM metadata:

DB_HOST=127.0.0.1      # if using SQL Auth Proxy
DB_NAME=appdb
DB_USER=postgres
DB_PASSWORD=example123


In production:

Use Secret Manager

Inject secrets at runtime

5️⃣ Cloud SQL Auth Proxy (Recommended)

Run SQL Auth Proxy as a system service:

wget https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.7.0/cloud-sql-proxy.linux.amd64 -O /usr/local/bin/cloud-sql-proxy
chmod +x /usr/local/bin/cloud-sql-proxy


Example service:

cloud-sql-proxy \
  --private-ip \
  my-project:us-central1:app-db

6️⃣ Deployment Flow (End to End)
GitHub
  ↓
VM Startup Script
  ↓
App Installed & Running
  ↓
LB → MIG → App
  ↓
Cloud SQL
