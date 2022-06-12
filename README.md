# AO_Retail_Website_Monitor
# Monitor single products on AO Website and get a notification when it is back instock.

This repo will provide you a script that is able to monitor the AO retail website for a single product and send a notification to you via Webhook or SMS letting you know when its back in stock. 

The script currently has no proxy handling so please make sure that your sleep is over 300 seconds to prevent a possible IP ban, also so you aren't bombarding the site with requests. This script is simply to provide you an automated way to check if a product is back in stock so you don't have to waste your time.

I will not be covering the setting up of the AWS SNS service which is used for the SMS send out but you can find guides online that can help with that. The code for SMS functionality is already in the script you simple need to add your number to the script once you have set up the SNS service.

1)Clone this git hub repo using the HTTP method or downloading the Zip file.

2)Once you have cloned the repo you should have the following file in a folder ao_monitor.py. This is the only script you need for this to work.

3)Within the directory where you cloned the repo, open your terminal and run the following commands... a) python3 -m venv env = Initialises virtual ENV for this specific folder (You do not have to do this but I like to keep my projects separated) b) Use pip to install the following libraries aa)requests, BeautifulSoup4, time, boto3.

4)Once that has been completed open the ao_monitor.py script. you will need to update the following... a)Instock URL line 34 - This can be used for testing, navigate to the website and find an instock product and paste the URL here. b) OOS Product line 35 - This is the product which you would like to monitor, paste the URL here. c) Data variable line 40 - This is what will be sent as part of your webhook notification. d) Client.publish line 42 - If you want to send out an SMS when your product comes back in stock, uncomment this line, update the "xxx" to be your phone number and update the message. e) time.sleep ine 47 - You can update how often the script should execute here, currently its set to 2000 seconds.

5)Now all that is left to do is run the script, if you have updated the script correctly and installed the required libaries you should see one of two things printed out to your terminal. a) 200[]Out of stock - Product was out of stock on this run b)200[<span class="inStockText text-body-sm">Available</span>]In stock - Product was in stock when the script ran (Check your webhook to see if it posted a notification for you)
