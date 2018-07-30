# Mesele Nedir?

Öncelikle Python 3.x bilgisayarımıza kuruyoruz.
Daha sonra komut satırına "pip install Django" diyerek djangoyu kuruyoruz
*istiyorsanız env'ye kurulum yapabilirsiniz*

Google Cloud'a üyelik ve ardından consol'a giriş.
Burada bir sanal makina oluşturmalıyız.
Ubuntu 17.10 kullandım ben 10GB + 3.075GB aylık 31$
VPC ağında Güvenlik duvarı kurllarında 8000. portu açmalısınız. (Dışardan girişe)
Burada önemli olan Harici IP'yi settings.py > Allowed'ın içine koymak.
*ALLOWED_HOSTS = ['http://35.230.140.10'] *
Tabiki windowsta yazdığınız code'u response edip, sanal sunucunuza SSH'tan bağlanıyorsunuz.
*sudo apt-get update*
*sudo apt-get install nginx*
*sudo systemctl start nginx*
Artdından buradada pythonu kuruyorsunuz.
*sudo apt-get update*
*sudo apt-get install python3-pip*
*pwd*
git clone ediyorsunuz
*mkdir djangoBeginnerApp*
sanal ortam kurlım
*python3 -m venv myvenv*
*source myvenv/bin/activate*
sanal ortamımıza django kuralım
*pip install django*
*./python manage.py runserver 0.0.0.0:8000*

