# HashCode 2021

## Install virtualenv

```bash
sudo apt update
sudo apt install software-properties-common virtualenv
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
```

### Generate virtualenv

```bash
virtualenv --python=/usr/bin/python3.8 venv
```

### Activate/Deactivate venv

```bash
source venv/bin/activate
deactivate
```

## Install import magic vscode

Press _ctrl+P_ and paste `ext install brainfit.vscode-importmagic`

## Compress project

```bash
zip -r hascode.zip . -x .history/\* -x \*__pycache__\* -x data/out/\*.out -x venv/\*
```
