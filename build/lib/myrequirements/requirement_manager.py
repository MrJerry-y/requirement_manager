import subprocess
import json
import click


class RequirementsManager:
    def __init__(self, requirements):
        self.requirements = requirements

    def generate_requirements_files(self, deployment_file='requirements.txt', development_file='requirements-dev.txt'):
        for req, dep in self.requirements.items():
            print(f"Package: {req}, Is Dev: {dep}")
        deployment_requirements = [
            req for req, is_dep in self.requirements.items() if is_dep]
        development_requirements = [
            req for req, is_dep in self.requirements.items() if not is_dep]

        self.write_requirements_file(deployment_file, deployment_requirements)
        self.write_requirements_file(
            development_file, development_requirements)

        print(f"Generated {deployment_file}")
        print(f"Generated {development_file}")

        self.install_requirements(deployment_file, development_file)

    def install_requirements(self, deployment_file='requirements.txt', development_file='requirements-dev.txt'):
        subprocess.run(['pip', 'install', '-r', deployment_file])
        subprocess.run(['pip', 'install', '-r', development_file])

    def write_requirements_file(self, filename, requirements):
        with open(filename, 'w') as file:
            for requirement in requirements:
                file.write(requirement + '\n')


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def main(input_file):
    """Manage requirements using myrequirements module."""
    with open(input_file) as f:
        requirements_data = json.load(f)

    manager = RequirementsManager(requirements_data)
    manager.generate_requirements_files()


if __name__ == '__main__':
    main()
