from connexion.resolver import RestyResolver
import connexion


if __name__ == '__main__':
    app = connexion.App(__name__, port=8080, specification_dir='swagger/')
    app.add_api('my_super_app.yaml',resolver=RestyResolver('api'))
    app.run()