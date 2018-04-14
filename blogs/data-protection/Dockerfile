FROM wordpress
ADD 000-default.conf /etc/apache2/sites-enabled/000-default.conf
ADD ports.conf /etc/apache2/ports.conf
RUN chgrp 0 /var/run/apache2 && \
    chmod g+w /var/run/apache2
