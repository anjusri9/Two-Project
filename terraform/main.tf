provider "aws" {
  region = var.region
}

resource "aws_instance" "iris_api" {
  ami           = var.ami
  instance_type = var.instance_type

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install docker.io -y",
      "docker run -d -p 5000:5000 anjusri9/iris_api:1.0.0"
    ]
  }
}
