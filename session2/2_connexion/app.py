import connexion

items = [
    { "id": 0,
    "name": "First item"
    }
]

def search() -> list:
    return items

if __name__ == '__main__':
    app = connexion.App(__name__, port=8080, specification_dir='swagger/')
    app.add_api('my_super_app.yaml')
    app.run()