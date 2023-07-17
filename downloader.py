import requests
import datetime

base_url = "https://www.amarstock.com/data/download/CSV"

start_date = datetime.datetime(2014, 1, 25)
end_date = datetime.datetime(2022, 12, 31)

delta = datetime.timedelta(days=1)
current_date = start_date

for _ in range((end_date - start_date).days + 1):
    date_string = current_date.strftime("%Y-%m-%d")
    url = f"{base_url}?date={date_string}&QuotesType=1"
    print(f"Requesting {url}")
    response = requests.post(url)
    file_extension = ".csv"


    if response.status_code == 200:
        file_name = f"stock_data_{date_string}{file_extension}"
        with open(file_name, "wb") as file:
            file.write(response.content)
            print(f"Saved {file_name}")
    else:
        print(f"Request for {date_string} failed with status code {response.status_code}")

    current_date += delta





# 
# import asyncio
# import aiohttp
# import datetime
# import argparse
# import ssl
# from multidict import CIMultiDict


# async def fetch_data(session, url, headers, form_data):
#     async with session.post(url, headers=headers, data=form_data) as response:
#         if response.status == 200:
#             output_file = './output.csv'
#             with open(output_file, 'wb') as f:
#                 while True:
#                     chunk = await response.content.read(1024)
#                     if not chunk:
#                         break
#                     f.write(chunk)

#         print("API request failed with status code:", response.status)
#         return None, None


# async def main():
#     url = 'https://www.amarstock.com/data/download/CSV'
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'en-US,en;q=0.9',
#         'Cache-Control': 'max-age=0',
#         'Content-Length': '28',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Cookie': 'g_state={"i_l":0}; .AspNet.ApplicationCookie=w-Yd3R4PFqSUQH0pNcODZ2tcFc02Pfy9udrH0Y0l6tI0ZoWvwNE526_bMCiw_WVrzFQE9IQ_ngJEwj292kGr_kT88_hqhBEgHVS95dbQXdenGIz6NL81fY44TugfalwX1fNyCr-apD3C6IUx-HPaFBbVUU6gUhrn_exAoiDisW2cXx17LQjdJiGe0Wt2kZcm8uI8hKlMEg9_oEs0c4dflyE-8qLYA9bt57HRMfoP4F40p4ELzqsM_xcbW6MD6rLF9ESk6fDewgTj765MEIZgxCZpIZQxx6bhAzUuxHo4KR_EI_ac2o0aWfq2lWN2FopwmZW2OdIoT_G7Us6NwxHC1iqmsh0SoEAD3U7WR2AtmXc49_hx4KTvUyPAP3aSgytJnpydvp-X_m2FbQV9PJRDbO7-znHjCfGMWDDdLTlSmjNmn2F4q5kV2j-0IxU195GQgABxsL9cO2ClWhQT9-yxzVBEc03Fo-myCMiiWHRY1pjvLiu5_ve91oMKLjadCgQJHsagsw; _ga_1HY8WKE7V3=GS1.1.1689445951.2.1.1689445980.31.0.0; _ga=GA1.2.458469605.1689416234; _gid=GA1.2.871808856.1689532581',
#         'Dnt': '1',
#         'Origin': 'https://www.amarstock.com',
#         'Referer': 'https://www.amarstock.com/csv-data-download',
#         'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#         'Sec-Ch-Ua-Mobile': '?0',
#         'Sec-Ch-Ua-Platform': '"macOS"',
#         'Sec-Fetch-Dest': 'document',
#         'Sec-Fetch-Mode': 'navigate',
#         'Sec-Fetch-Site': 'same-origin',
#         'Sec-Fetch-User': '?1',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#     }

#     form_data = {
#         'QuotesType': '1',
#         # Add other form data here
#     }

#     parser = argparse.ArgumentParser()
#     parser.add_argument('--start-date', help='Start date in YYYY-MM-DD format', required=False)
#     parser.add_argument('--end-date', help='End date in YYYY-MM-DD format', required=False)
#     args = parser.parse_args()

#     start_date = args.start_date
#     end_date = args.end_date

#     # if start_date is None or end_date is None:
#     #     print("Both date is required")
#     #     return

#     # if start_date > end_date:
#     #     print("Start date cannot be greater than end date")
#     #     return
    

#     start_date = '2022-12-31'
#     end_date = '2022-12-31'


#     ssl_context = ssl.create_default_context()
#     ssl_context.check_hostname = False
#     ssl_context.verify_mode = ssl.CERT_NONE

#     conn = aiohttp.TCPConnector(ssl=ssl_context)

#     async with aiohttp.ClientSession(connector = conn) as session:
#         tasks = []
#         current_date = start_date
#         while current_date <= end_date:
#             form_data['date'] = current_date
#             task = asyncio.ensure_future(fetch_data(session, url, headers, form_data))
#             tasks.append(task)

#             # Increment current_date by 1 day
#             year, month, day = map(int, current_date.split('-'))
#             next_date = datetime.date(year, month, day) + datetime.timedelta(days=1)
#             current_date = next_date.strftime('%Y-%m-%d')

#         await asyncio.gather(*tasks)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# # run this python script using the following command: python downloader.py
# # run with flags: python downloader.py --start-date 2013-01-01 --end-date 2022-12-31