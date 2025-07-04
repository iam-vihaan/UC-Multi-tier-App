resource "aws_db_instance" "employee_db" {
  identifier           = "employee-db"
  engine               = "postgres"
  instance_class       = "db.t3.micro"
  allocated_storage    = 20
  name                 = "employeedb"
  username             = "admin"
  password             = "password123"
  skip_final_snapshot  = true
  publicly_accessible  = true
}
