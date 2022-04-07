from os import environ

configurations = {
    "aws_region": environ["AWS_REGION"],
    "web_hook_secret": environ["WEB_HOOK_SECRET"],
    "mysql_pw": environ["MYSQL_PW"],
    "mysql_port": environ["MYSQL_PORT"],
    "mysql_host": environ["MYSQL_HOST"],
    "environment": environ["ENVIRONMENT"],
    "stripe_secret": environ["STRIPE_SECRET"],
    "owner_email": "wanzhenglyu@crewbite.com"
}
