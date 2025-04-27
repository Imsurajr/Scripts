variable "instance_type" {
  description = "Type of EC2 instance"
  default     = "t2.micro"
}

variable "key_name" {
  description = "SSH key pair name"
}

variable "bucket_name" {
  description = "Unique name for S3 bucket"
}
