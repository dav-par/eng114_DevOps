# set aws as the cloud provider irland as the region
provider "aws" {
	region = "eu-west-1"
}

#resource block to configure app instance###########################################################
resource "aws_instance" "app_instance"{
# choose your ami and instance type
	ami = "ami-07b63aa1cfd3bc3a5"
	instance_type = "t2.micro"
    subnet_id = "subnet-0e9792ee5dc08fbbd"
    vpc_security_group_ids = "vpc-0dace77b8ccb63bb8"

# enable a public ip
    associate_public_ip_address = true
   
# name the instance
    tags = {
        Name = "eng114_david_terra_made_by_jenkins"
    }
	
# add key
    key_name = "eng144_david_terra"
}

#resource block to configure db instance###########################################################
resource "aws_instance" "db_instance"{
# choose your ami and instance type
	ami = "ami-07b63aa1cfd3bc3a5"
	instance_type = "t2.micro"
    subnet_id = "subnet-0b8a442c13307badf"
    vpc_security_group_ids = "sg-03c002f966f328233"
    private_ip = "10.5.242.225"
    

# enable a public ip
    associate_public_ip_address = false
   
# name the instance
    tags = {
        Name = "eng114_david_terraform-db"
    }
	
# add key
    key_name = "eng144_david_terra"
}