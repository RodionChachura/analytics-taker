variable "aws_access_key" {
  default = "<AWS_ACCESS_KEY>"
}

variable "aws_secret_key" {
  default = "<AWS_SECRET_KEY>"
}

variable "region" {
  default = "<DEFAULT_REGION>"
}

variable "sentry_key" {
  default = "<SENTRY_KEY>"
}

variable "view_id" {
  default = "<VIEW_ID>"
}


variable "name" {
  default = "tf-analytics-taker"
}

variable "bucket_name" {
  default = "tf-analytics-taker"
}

variable "bucket_object_name" {
  default = "function.zip"
}

variable "handler" {
  default = "lambda.handler"
}

variable "memory_size" {
  default = "512"
}