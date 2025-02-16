import pyfiglet as fig # type: ignore
def main(prompt: str):

    print(prompt)

if __name__ == '__main__':
    prompt = fig.figlet_format("Hello. This is my training repository", font="starwars")
    main(prompt=prompt)
