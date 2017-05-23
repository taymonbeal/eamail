Vagrant.configure(2) do |config|
  config.vm.box = 'ubuntu/xenial64'
  config.vm.network :forwarded_port, guest: 1080, host: 1080
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.provision :shell, path: 'vagrant-scripts/provision.sh', privileged: false
  config.vm.provision :shell, path: 'vagrant-scripts/startup.sh', privileged: false, run: :always
end
