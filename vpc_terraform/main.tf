# set aws as the cloud provider irland as the region
provider "aws" {
	region = "eu-west-1"
}

/*
#resource block to configure test in
resource "aws_instance" "test_-instance"{
# choose your ami and instance type
	ami = "ami-07b63aa1cfd3bc3a5"
	instance_type = "t2.micro"
    subnet_id = "${aws_subnet.public_subnet.id}"
    vpc_security_group_ids = ["${aws_security_group.public.id}"]

# enable a public ip
    associate_public_ip_address = true
   
# name the instance
    tags = {
        Name = "eng114_david_terraform_network_test"
    }

# add key
    key_name = var.key_id
}
*/
