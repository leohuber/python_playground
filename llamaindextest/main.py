import os

def main():
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if openai_api_key:
        print(f'OPENAI_API_KEY: {openai_api_key}')
    else:
        print('OPENAI_API_KEY is not set')

if __name__ == '__main__':
    main()