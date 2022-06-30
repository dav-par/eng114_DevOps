# set aws as the cloud provider irland as the region
provider "aws" {
	region = "eu-west-1"
}

#resource block to configure app instance
resource "aws_instance" "app_instance"{
# choose your ami and instance type
	ami = "ami-0b47105e3d7fc023e"
	instance_type = "t2.micro"
    subnet_id = var.public_subnets_cidr

# enable a public ip
    associate_public_ip_address = true
   
# name the instance
    tags = {
        Name = "eng114_david_terraform"
    }
	
# add key
    key_name = "eng114_david_2"
}
