FROM nginx:alpine

# Reconfigure nginx to listen on 3000 (Coolify's default exposed port)
RUN sed -i 's/listen       80;/listen       3000;/' /etc/nginx/conf.d/default.conf && \
    sed -i 's/listen  \[::\]:80;/listen  [::]:3000;/' /etc/nginx/conf.d/default.conf

# One host gets its own root (see the file). Every other host is unchanged.
COPY nginx-stephens.conf /etc/nginx/conf.d/stephens.conf

COPY . /usr/share/nginx/html/
EXPOSE 3000
