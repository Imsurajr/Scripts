provider "aws" {
  region = "ap-south-1" # Mumbai Region
}

resource "aws_instance" "suraj_ec2" {
  ami                    = "ami-0f5ee92e2d63afc18" # Amazon Linux 2 AMI (ap-south-1)
  instance_type          = var.instance_type
  key_name               = var.key_name

  tags = {
    Name = "SurajEC2Instance"
  }
}

resource "aws_s3_bucket" "suraj_bucket" {
  bucket = var.bucket_name

  tags = {
    Name = "SurajS3Bucket"
  }
}
