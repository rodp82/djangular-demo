# Ubuntu 16.04/Python2.7/Django
#---------------------------------------
Vagrant.configure("2") do |config|

  config.vm.box = "bento/ubuntu-16.04"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8001

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install python -y
    apt-get install python-pip -y
    pip install virtualenv
  SHELL

end