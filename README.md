# Controlling resources with systemd services

This will be:

+ an overview of strategies for controlling the resources used by systemd services
+ a collection of example service definitions demonstrating the strategies
+ an environment to run the examples in that includes executables that naively mimic heavy or steady loads.


Right now it contains a base for the demo environment, `vagrant up` will get you a CentOS 7 box with a few dummy executables added to /usr/local/bin for use by example services.
