i removed `SERVER_NAME` from the Eve settings in order to make
deployment easier. This falsifies the locators produced by Eve for
HATEOS, like Petr explains:

    <pjx> without name it's eg {self: {href: '/users/1'}}
    <pjx> with name you can get {self: {href: {'http://localhost/users/1'}}

If one day i will want to have those locators back, i would also need
to improve the Nginx configuration, like Petr explains:

    <pjx> you have to change the Host header in nginx config
    <pjx> to match your server_name config
    <pjx> so eg proxy_set_header Host "localhost:8008";

