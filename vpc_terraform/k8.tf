resource "aws_security_group" "k8"{
	name = "david_sg_k8"
	vpc_id = aws_vpc.vpc.id

	ingress {
		description = "HTTP from all"
		from_port = 80
		to_port = 80
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}

	ingress {
		description = "HTTPS from all"
		from_port = 443
		to_port = 443
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}

	ingress {
		description = "SSH from localhost"
		from_port = 22
		to_port = 22
		protocol = "tcp"
		cidr_blocks = ["${chomp(data.http.myip.body)}/32"]
	}

    egress {
		description = "All traffic out"
		from_port = 0
		to_port = 0
		protocol = "-1"
		cidr_blocks = ["0.0.0.0/0"]
	}

  tags = {
    Name        = "${var.environment}-sg-k8"
    Environment = "${var.environment}"
  }

}

resource "aws_instance" "k8"{
# choose your ami and instance type
	ami = "ami-07b63aa1cfd3bc3a5"
	instance_type = "t2.medium"
    subnet_id = "${aws_subnet.public_subnet.id}"
    vpc_security_group_ids = ["${aws_security_group.k8.id}"]

# enable a public ip
    associate_public_ip_address = true
   
# name the instance
    tags = {
        Name = "david-k8"
    }

# add key
    key_name = var.key_id
}