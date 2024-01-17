## NGINX and Docker Compose

While running a FastAPI application with NGINX and Docker Compose, we need to make sure that the NGINX server is able to communicate with the FastAPI application. For this we need to have `root_path` configured in the FastAPI application, or else configure NGINX properly so that you don't need to set the `root_path` explicitly.

This really helped me, as I didn't want to scaffold root_path in the application itself, since I was using `nginx` as a reverse proxy in production with docker-compose.

For people using `nginx` as a reverse proxy, and stuck on how to forward the traffic to the right container, this is my current configuration:

```nginx title="sample-application.conf" hl_lines="11 12 13" linenums="1"
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        # For my react frontend served by an nginx container
        proxy_pass http://localhost:7000;
    }
    location /api/{
       # For FastAPI app running in docker container
       # where the endpoint should be /api/
    	proxy_pass http://localhost:8100/;
  }
}
```

Notice the trailing slash at the end in line `13`, it is important,so that it performs stripping properly.
