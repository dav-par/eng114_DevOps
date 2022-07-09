variable "environment" {
  default = "david"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnets_cidr" {
  default = "10.0.5.0/24"
}

variable "private_subnets_cidr" {
  default = "10.0.20.0/24"
}

variable "region" {
  default = "eu-west-1"
}

variable "availability_zone" {
  default = "eu-west-1a"
}

variable "key_id" {
  default = "david-ireland"
}