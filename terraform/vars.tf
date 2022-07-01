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

variable "private_subnets_cidr" {
  default = "10.5.242.0/24"
}

variable "region" {
  default = "eu-west-1"
}


variable "availability_zone" {
  default = "eu-west-1a"
}

variable "key_id" {
  default = "eng144_david_terra"
}

variable "app_ami" {
  default = "ami-0b47105e3d7fc023e"
}

variable "db_ami" {
  default = "ami-0eecf033d2b64a2cb"
}

variable "controller_ami" {
  default = "ami-0b76dbf60d4901602"
}
