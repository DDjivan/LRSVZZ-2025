https://nodejs.org/en/download 

Sur une machine Linux : 
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

Relancer le shell (ou `CTRL+D`)

```
nvm install 22
``````

Verifier la version de Node.js et npm : 
```bash
node -v  # Should print "v22.16.0".
nvm current  # Should print "v22.16.0".
npm -v  # Should print "10.9.2".
```

