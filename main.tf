terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 4.0"
        }
    }
}

provider "aws" {
    region = "us-east-1"
}

resource "aws_dynamodb_table" "table_flota" {
    name         = "StateFlotaDeliveryOrders"
    billing_mode = "PAY_PER_REQUEST"
    hash_key     = "cartId"
    attribute {
        name = "cartId"
        type = "S"
    }
    tags = {
        Environment = "dev"
        Project = "LogiPulse-AI"
    }
}

resource "aws_cloudwatch_event_bus" "bus_logistics" {
    name = "bus-event-logistics"
}