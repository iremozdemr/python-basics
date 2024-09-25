#virtual environment (sanal ortam):
#-izole çalışma ortamları oluşturmak için kullanılan araçlardır
#-farklı projeler için oluşabilecek farklı kütüphane ve versiyon ihtiyaçlarını
#projeler birbirini etkilemeyecek şekilde oluşturma imkanı sunar

#virtual environment araçları:

#-venv:
#paket yönetimi için pip kullanır

#-virtualenv:
#paket yönetimi için pip kullanır

#-pipenv:
#virtual environment aracıdır
#package management aracıdır

#-conda:
#virtual environment aracıdır
#package management aracıdır


#package + dependency management araçları:
#-pip (requirements.txt):
#-pipenv (Pipfile)
#-conda (environment.yaml)


#conda:

#sanal ortamların listelenmesi:
#conda env list

#sanal ortam oluşturma:
#conda create -n myenv

#oluşturulan sanal ortamı aktif etme:
#conda activate myenv

#oluşturulan sanal ortamı deaktif etme:
#conda deactivate

#yüklenmiş paketlerin listelenmesi:
#conda list

#paket yükleme:
#conda install numpy

#belirli bir versiyona göre paket yükleme:
#conda install numpy=1.20.1

#aynı anda birden fazla paket yükleme
#conda install numpy pandas

#paket silme:
#conda remove numpy

#paket versiyonunu güncelleme:
#conda upgrade numpy

#tüm paketlerin versiyonlarını güncelleme:
#conda upgrade -all

#environment.yaml dosyası oluşturma:
#yaml ve yml uzantılı olabilir
#conda env export > environment.yaml

#environment.yaml kullanarak environment oluşturma:
#conda env create -f environment.yaml


#pip = pypi = python package index:

#paket yükleme:
#pip install numpy

#belirli bir versiyona göre paket yükleme:
#pip install numpy==1.20.1


#class içindeyse: method
#class içinde değilse: function

print(9)
print(9.2)
print(2j + 1)
#sayılar:
#-int
#-float
#-complex

int_methods = dir(int)
str_methods = dir(str)
print(int_methods)
print(str_methods)
#dir: methodları listeler

type("a")
#değişkenin type'ını verir

len("a")
#değişkenin uzunluğunu verir
#stringleri parametre olarak alır
#dizileri parametre olarak alır
#intleri parametre olarak almaz
#floatları parametre olarak almaz

print(True and True)
print(True or False)
print(not True)