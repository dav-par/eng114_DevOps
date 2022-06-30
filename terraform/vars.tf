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


variable "my_ip" {
    default = "94.4.90.120/32"

}