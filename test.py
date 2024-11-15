name: test_calculator.py


on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
    
jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2  

      - name: Set up Python hassanandgad
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Run tests
        run: |
          python -m unittest discover -s . -p "testCalc.py"
          
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: ${{ always() }}  

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Deploy Application
        run: |
          echo "Deploying the application..." # Replace this with actual deployment commands
