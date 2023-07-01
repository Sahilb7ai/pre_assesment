import requests as rq
url = "https://stackoverflow.com/tags"
def get_data(url):
    data = rq.get(url)
    with open("data/file.html","w") as f:
        f.write(data.text)
def main():
    get_data(url)

if '__name__' == '__main__':
    try:
        main()
    except Exception as e:
        print("Inside main")
        print("The error is :",e)
    finally:
        print("Execution completed")

