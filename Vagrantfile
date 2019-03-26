# virtualbox guest additions aren't in the current centos box
# see https://blog.centos.org/2019/03/updated-centos-vagrant-images-available-v1902-01/
# so we make sure we have the plugin we need. if we install he need to make ourselves
# into a fresh process to have the plugin loaded
plugin = "vagrant-vbguest"
unless Vagrant.has_plugin? plugin
  system "vagrant plugin install #{plugin}"
  exec "vagrant #{ARGV.join ' '}"
end

Vagrant.configure("2") do |config|
  config.vm.define :systemd_demos
  config.vm.box = "centos/7"

  # again, we need to be explicit because of the lack of guest additions
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"

  config.vm.post_up_message = "insert instructions here"
  config.vm.provision "shell", inline: <<-SHELL
  yum install -y gcc time
  cd /vagrant/src/primes
  make
  make install
  cd -
  install /vagrant/src/memkill/memkill.py /usr/local/bin/memkill
  install /vagrant/src/logger/logger.py /usr/local/bin/logger
  SHELL
end
