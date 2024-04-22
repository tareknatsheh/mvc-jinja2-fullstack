### Quick Start
1. Create a virtual machine:
```
python -m venv venv
```
2. Activate it:
- Windows: `venv/Scripts/activate`
- Linux: `. venv/bin/activate`

3. Instal the dependencies:
```
pip install -r requirements.txt
```

4. Run it:
```
uvicorn server:app --reload
```

### Unit Tests
Run the following:
```
python -m pytest
```