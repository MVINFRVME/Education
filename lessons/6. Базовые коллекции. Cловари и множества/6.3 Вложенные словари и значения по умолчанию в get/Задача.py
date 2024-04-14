data = dict()

# До этого что-то происходит
print(data.get("server"))

data["server"] = {"host": "127.0.0.1", "port": "10"}
# До этого что-то происходит
if data.get("configuration", {}).get("ssh", {}).get("login", {}):
    print("В структуре уже есть логин")

data["configuration"] = {
    "ssh": {"access": "true", "login": "Ivan", "password": "qwerty"}
}

print(data)
