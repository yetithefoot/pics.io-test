FROM nginx:alpine

RUN apk add --no-cache bash

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

CMD ["/bin/bash", "-c", "nginx -g \"daemon off;\""]