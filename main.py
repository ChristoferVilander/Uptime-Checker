import requests
import time

# A clear and descriptive User Agent
headers = {'User-Agent': 'Python Script for checking up-time'}

# Small script to check the availability and uptime of a given URL
class UptimeChecker:
    def __init__(self, url, log_file='up_time_log.txt'):
        self.url = url
        self.up_time = 0
        self.total_pings = 0
        self.log_file = log_file
        self.file_handle = open(self.log_file, 'a')

    def check_availability(self):
        try:
            response = requests.get(self.url)

            # Check if the response is ok (HTTP 200 OK)
            if response.status_code == 200:
                self.up_time += 1
                self.total_pings += 1
            else:
                self.total_pings += 1
                print(f"The site seem to be down")
        except requests.RequestException as e:
            print(f"An error occurred while trying to access the Web Page")

    def run(self):
        while True:
            # 10 second wait
            time.sleep(10)

            # Check the availability of the provided url
            self.check_availability()

            # Calculate the percentage uptime and print it to the log file
            percentage = (self.up_time / self.total_pings) * 100
            print(f'The uptime for {self.url} is {percentage:.2f}%', file=self.file_handle)


if __name__ == "__main__":
    # Provide which url to check
    checker = UptimeChecker(url='') #Enter url
    checker.run()
