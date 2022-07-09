resource "aws_security_group" "public"{
	name = "eng114_david_sg_public"
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
    Name        = "${var.environment}-sg-public"
    Environment = "${var.environment}"
  }

}

resource "aws_security_group" "private"{
	name = "eng114_david_sg_private"
	description = "27017 for mongoDB"
	vpc_id = aws_vpc.vpc.id


	ingress {
		description = "27017 from app instance"
		from_port = 27017
		to_port = 27017
		protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
	}

	ingress { #remove in production
		description = "SSH from localhost"
		from_port = 22
		to_port = 22
		protocol = "tcp"
		cidr_blocks = ["0.0.0.0/0"] #["${chomp(data.http.myip.body)}/32"]
	}

	egress {
		description = "All traffic out"
		from_port = 0
		to_port = 0
		protocol = "-1"
		cidr_blocks = ["0.0.0.0/0"]
	}

  tags = {
    Name        = "${var.environment}-sg-private"
    Environment = "${var.environment}"
  }

}