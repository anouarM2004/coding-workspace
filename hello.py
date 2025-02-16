import pyfiglet as fig # type: ignore
def main(prompt: str):

    print(prompt)

if __name__ == '__main__':
    prompt = fig.figlet_format("THIS IS MY TRAINING REPOSITORY", font="starwars")
    main(prompt=prompt)
