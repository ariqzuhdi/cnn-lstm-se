import requests

def download_file(url):

    try:
        response = requests.get(url)
        response.raise_for_status()

        filename = url.split("/")[-1] 

        with open(filename, 'wb') as f:
            f.write(response.content)

        print(f"File downloaded successfully: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")


for i in range (1, 32):
    if (i < 10):
        url = 'https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2023/AIS_2023_12_0'+ str[i] + '.zip'
        download_file(url)
    else:
        url = 'https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2023/AIS_2023_12_'+ str[i] + '.zip'
        download_file(url)