#loadbalancer#######################################################
resource "aws_elb" "eng114_david_loadbalancer" {
  name               = "${var.environment}-app-lb"
  internal           = false
  security_groups    = ["${aws_security_group.eng114_david_sg_app_terra.id}"]
  subnets            = [
    "${aws_subnet.public_subnet.id}",
    "${aws_subnet.public_subnet2.id}"
  ]

cross_zone_load_balancing   = true

health_check {
    healthy_threshold = 2
    unhealthy_threshold = 2
    timeout = 3
    interval = 30
    target = "HTTP:80/"
  }

listener {
    lb_port = 80
    lb_protocol = "http"
    instance_port = "80"
    instance_protocol = "http"
  }
}

#launchconfig#####################################################
resource "aws_launch_configuration" "eng114_david_aws_launch" {
  name_prefix = "eng114-david-autoscale-"
  image_id = var.app_ami
  instance_type = "t2.micro"
  key_name = var.key_id
  security_groups = ["${aws_security_group.eng114_david_sg_app_terra.id}"]
  associate_public_ip_address = true
  user_data = "${file("data.sh")}"
  
lifecycle {
    create_before_destroy = true
  }
}

#autoscaling#######################################################
resource "aws_autoscaling_group" "eng114_david_autoscale" {
  name = "${aws_launch_configuration.eng114_david_aws_launch.name}-asg"
  min_size             = 2
  desired_capacity     = 2
  max_size             = 3
  
  health_check_type    = "EC2"
  load_balancers = [
    "${aws_elb.eng114_david_loadbalancer.id}"
  ]

launch_configuration = "${aws_launch_configuration.eng114_david_aws_launch.name}"
enabled_metrics = [
    "GroupMinSize",
    "GroupMaxSize",
    "GroupDesiredCapacity",
    "GroupInServiceInstances",
    "GroupTotalInstances"
  ]
metrics_granularity = "1Minute"
vpc_zone_identifier  = [
    "${aws_subnet.public_subnet.id}",
  ]
# Required to redeploy without an outage.
  lifecycle {
    create_before_destroy = true
  }

tag {
    key                 = "Name"
    value               = "${var.environment}-123app"
    propagate_at_launch = true
  }
}

