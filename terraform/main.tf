# set aws as the cloud provider irland as the region
provider "aws" {
	region = "eu-west-1"
}

#resource block to configure app instance
resource "aws_instance" "app_instance"{
# choose your ami and instance type
	ami = "ami-0b47105e3d7fc023e"
	instance_type = "t2.micro"
    subnet_id = "${aws_subnet.public_subnet.id}"
    vpc_security_group_ids = ["${aws_security_group.eng114_david_sg_app_terra.id}"]

# enable a public ip
    associate_public_ip_address = true
   
# name the instance
    tags = {
        Name = "eng114_david_terraform_app"
    }
	
# add key
    key_name = "eng114_david_2"
}

#resource block to configure app instance
resource "aws_instance" "db_instance"{
# choose your ami and instance type
	ami = "ami-0eecf033d2b64a2cb"
	instance_type = "t2.micro"
    subnet_id = "${aws_subnet.private_subnet.id}"
    vpc_security_group_ids = ["${aws_security_group.eng114_david_sg_db_terra.id}"]

# enable a public ip
    associate_public_ip_address = false
   
# name the instance
    tags = {
        Name = "eng114_david_terraform-db"
    }
	
# add key
    key_name = "eng114_david_2"
}

