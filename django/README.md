
### Activate virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies
```
python -m pip install Django
```

### Check version
```
django-admin --version
```

### Create new django project
```
django-admin startproject quiz_demo
```

### Run django project
```
python manage.py runserver
```

## To add questions using django shell
```
python manage.py shell
```
```
from quiz.models import Quiz, Question, Answer

# Create a Terraform quiz
terraform_quiz = Quiz.objects.create(title="Terraform Fundamentals", description="Test your knowledge of Terraform basics")

# Question 1
q1 = Question.objects.create(
    quiz=terraform_quiz,
    text="What is Terraform?",
    order=1
)
Answer.objects.create(question=q1, text="A programming language", is_correct=False)
Answer.objects.create(question=q1, text="An open-source tool for automating infrastructure deployment and management", is_correct=True)
Answer.objects.create(question=q1, text="A programming language for creating mobile applications", is_correct=False)
Answer.objects.create(question=q1, text="A cloud provider for hosting websites", is_correct=False)

# Question 2
q2 = Question.objects.create(
    quiz=terraform_quiz,
    text="What is the file extension for Terraform configuration files?",
    order=2
)
Answer.objects.create(question=q2, text=".tf", is_correct=True)
Answer.objects.create(question=q2, text=".yaml", is_correct=False)
Answer.objects.create(question=q2, text=".json", is_correct=False)
Answer.objects.create(question=q2, text=".config", is_correct=False)

# Question 3
q3 = Question.objects.create(
    quiz=terraform_quiz,
    text="Which command is used to create an execution plan in Terraform?",
    order=3
)
Answer.objects.create(question=q3, text="terraform plan", is_correct=True)
Answer.objects.create(question=q3, text="terraform apply", is_correct=False)
Answer.objects.create(question=q3, text="terraform init", is_correct=False)
Answer.objects.create(question=q3, text="terraform destroy", is_correct=False)


# Question 4
q4 = Question.objects.create(
    quiz=terraform_quiz,
    text="What does 'terraform apply' do?",
    order=4
)
Answer.objects.create(question=q4, text="Generates an execution plan", is_correct=False)
Answer.objects.create(question=q4, text="Destroys all resources managed by Terraform", is_correct=False)
Answer.objects.create(question=q4, text="Applies the changes required to reach the desired state of the configuration", is_correct=True)
Answer.objects.create(question=q4, text="Initializes the working directory for Terraform configuration", is_correct=False)

# Question 5
q5 = Question.objects.create(
    quiz=terraform_quiz,
    text="Which file is used to store Terraform state by default?",
    order=5
)
Answer.objects.create(question=q5, text="terraform.tfstate", is_correct=True)
Answer.objects.create(question=q5, text="terraform.tfvars", is_correct=False)
Answer.objects.create(question=q5, text="terraform.json", is_correct=False)
Answer.objects.create(question=q5, text="main.tf", is_correct=False)

print("Sample Terraform questions have been added to the database.")
```