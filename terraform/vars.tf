variable "environment" {
  default = "eng114-david-terra"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  default     = "10.5.0.0/16"
}

variable "public_subnets_cidr" {
  default = "10.5.241.0/24"
}

variable "public_subnets_cidr2" {
  default = "10.5.240.0/24"
}

variable "private_subnets_cidr" {
  default = "10.5.242.0/24"
}

variable "region" {
  default = "eu-west-1"
}


variable "availability_zone" {
  default = "eu-west-1a"
}

variable "availability_zone2" {
  default = "eu-west-1b"
}

variable "key_id" {
  default = "eng144_david_terra"
}

variable "app_ami" {
  default = "ami-0fcb2ff41055e4a93"
}

variable "db_ami" {
  default = "ami-075574b4670425b76"
}

variable "controller_ami" {
  default = "ami-0b756558a3243292d"
}
